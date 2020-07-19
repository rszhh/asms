import json
import pymysql
import numpy as np
from DBUtils.PooledDB import PooledDB
from flask import Flask, request, make_response

app = Flask(__name__)


# mysql db connpool
class MysqlUtil(object):
    __pool = None

    def __init__(self):
        MysqlUtil.create_db_if_not_exists()
        self.pool = MysqlUtil.__get_conn()
        MysqlUtil.create_table_if_not_exists(self)

    @staticmethod
    def __get_conn():
        """
        @summary: staticmethod, get conn from connpool
        @return MySQLdb.connection
        """
        if MysqlUtil.__pool is None:
            __pool = PooledDB(pymysql,
                              mincached=1,
                              maxcached=10,
                              maxconnections=10,
                              host='mysql',
                              port=3306,
                              user='root',
                              passwd='123456',
                              db='test',
                              use_unicode=False,
                              blocking=False,
                              charset="utf8")
        return __pool

    # because use docker-compose, need to create a new mysql
    # before connect mysql db, need to check db 'test' if exists
    # if not exists, create a new db
    def create_db_if_not_exists():
        conn = pymysql.connect(host='mysql',
                               port=3306,
                               user='root',
                               password='123456',
                               charset='utf8')
        cursor = conn.cursor()
        sql = "CREATE DATABASE IF NOT EXISTS test"
        cursor.execute(sql)
        cursor.close()
        conn.close()

    # after check db 'test' and create connpool
    # have to check the table if exists, is not exists, create a new table
    def create_table_if_not_exists(self):
        try:
            sql = """CREATE TABLE IF NOT EXISTS `automobile_sale_info` (
                `car_number`  int(10) UNSIGNED NOT NULL AUTO_INCREMENT ,
                `type`  varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL ,
                `brand`  varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL ,
                `color`  varchar(10) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL ,
                `price`  mediumint(9) UNSIGNED NOT NULL ,
                `entry_date`  char(10) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL ,
                `sale_date`  char(10) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL ,
                `is_sale`  tinyint(4) NOT NULL ,
                PRIMARY KEY (`car_number`)
                )
                ENGINE=InnoDB
                DEFAULT CHARACTER SET=utf8 COLLATE=utf8_general_ci
                AUTO_INCREMENT=35
                ROW_FORMAT=COMPACT
                ;"""
            conn = self.pool.connection()
            with conn.cursor() as cursor:
                cursor.execute(sql)
                conn.commit()
        finally:
            cursor.close()
            conn.close()

    def select(self, sql, param=()):
        try:
            conn = self.pool.connection()
            with conn.cursor() as cursor:
                cursor.execute(sql, param)
                return cursor.fetchall()
        finally:
            cursor.close()
            conn.close()

    # insert update and delete
    def except_select(self, sql, param=()):
        try:
            conn = self.pool.connection()
            with conn.cursor() as cursor:
                res = cursor.execute(sql, param)
                if res == 1:
                    conn.commit()
                    return {"code": 200, "message": "success"}
                else:
                    ex = Exception("error")
                    raise ex
        except Exception as res:
            conn.rollback()
            return {"code": 201, "message": res.__str__()}
        finally:
            cursor.close()
            conn.close()


db = MysqlUtil()


class AutoMobile:
    def __init__(self, items):
        self.carnumber = items[0]
        self.type = items[1]
        self.brand = items[2]
        self.color = items[3]
        self.price = items[4]
        self.entrydate = items[5]
        # have been sold automobiles has on more info: saledate
        if items.__len__() == 7:
            self.saledate = items[6]


class AutoMobiles:
    def __init__(self, code, message, items):
        self.code = code
        self.message = message
        self.items = items


# handle error: TypeError: Object of type 'bytes' is not JSON serializable
class MyEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, np.ndarray):
            return obj.tolist()
        elif isinstance(obj, bytes):
            return str(obj, encoding='utf-8')
        return json.JSONEncoder.default(self, obj)


# Browser cross domain. only use once, even do not need in code any more after used
@app.after_request
def af_request(resp):
    resp = make_response(resp)
    resp.headers['Access-Control-Allow-Origin'] = '*'
    resp.headers['Access-Control-Allow-Methods'] = 'GET,POST'
    resp.headers[
        'Access-Control-Allow-Headers'] = 'x-requested-with,content-type'
    return resp


@app.route('/add', methods=['POST'])
def add():
    data = json.loads(request.get_data())
    sql = "insert into `automobile_sale_info`(`type`,`brand`,`color`,`price`,`entry_date`,`is_sale`) values(%s,%s,%s,%s,%s,%s)"
    jsonstr = db.except_select(sql,
                               (data['type'], data['brand'], data['color'],
                                data['price'], data['entrydate'], 0))
    return jsonstr


# common method to get sale/un-sale automobile info by status
# 0 => un-sale    1 => sale
@app.route('/getinfo', methods=['POST'])
def get_automobile():
    data = json.loads(request.get_data())
    sql = ""
    if data['gettype'] == 0:
        sql = "select car_number,type,brand,color,price,entry_date from automobile_sale_info where is_sale=%s"
    else:
        # have been sold infos have a one more sale date info
        sql = "select car_number,type,brand,color,price,entry_date,sale_date from automobile_sale_info where is_sale=%s"
    results = db.select(sql, (data['gettype']))
    items = []
    for res in results:
        automobile = AutoMobile(list(res))
        items.append(automobile.__dict__)
    automobiles = AutoMobiles(200, "success", items)
    jsonstr = json.dumps(automobiles.__dict__, cls=MyEncoder, indent=4)
    return jsonstr


@app.route('/sale', methods=['POST'])
def sale():
    data = json.loads(request.get_data())
    sql = "update automobile_sale_info set is_sale=1,sale_date=%s where car_number=%s"
    jsonstr = db.except_select(sql, (data['saledate'], data['carnumber']))
    return af_request(jsonstr)


@app.route('/options', methods=['POST'])
def delete_or_change():
    data = json.loads(request.get_data())
    if data['optiontype'] == 0:
        sql = "delete from `automobile_sale_info` where car_number=%s"
        jsonstr = db.except_select(sql, (data['carnumber']))
        return jsonstr
    sql = "update `automobile_sale_info` set `type`=%s,`brand`=%s,`color`=%s,`price`=%s,`entry_date`=%s where car_number=%s"
    jsonstr = db.except_select(
        sql, (data['type'], data['brand'], data['color'], data['price'],
              data['entrydate'], data['carnumber']))
    return jsonstr


@app.route('/type', methods=['POST'])
def show_salestatistics():
    sql = "select type from automobile_sale_info where is_sale=1"
    results = db.select(sql)
    saloon = 0
    suv = 0
    cross = 0
    # when judgement type should transcode, but I'm too lazy to do it
    # in fact, it doesn't have to be
    for res in results:
        # this string code represent '家用轿车'
        if res == (b'\xe5\xae\xb6\xe7\x94\xa8\xe8\xbd\xbf\xe8\xbd\xa6', ):
            saloon += 1
        elif res == (b'SUV', ):
            suv += 1
        else:
            cross += 1
    return {
        "code": 200,
        "message": "success",
        "saloon": saloon,
        "suv": suv,
        "cross": cross
	}

