<template>
  <el-table v-loading="loading" :data="tableData" style="width: 100%" max-height="400">
    <el-table-column fixed prop="carnumber" label="汽车编号" width="100"></el-table-column>
    <el-table-column prop="type" label="类型" width="150"></el-table-column>
    <el-table-column prop="brand" label="品牌" width="150"></el-table-column>
    <el-table-column prop="color" label="颜色" width="120"></el-table-column>
    <el-table-column prop="price" label="价格" width="120"></el-table-column>
    <el-table-column prop="entrydate" label="出厂日期" width="120"></el-table-column>
    <el-table-column fixed="right" label="操作" width="180">
      <template slot-scope="scope">
        <el-button
          @click.native.prevent="saleAutomobile(scope.$index, tableData, scope.row)"
          type="success"
          size="mini"
        >售出</el-button>
      </template>
    </el-table-column>
  </el-table>
</template>

<script>
import Axios from "axios";
export default {
  data() {
    return {
      tableData: [],
      loading: true
    };
  },
  mounted() {
    this.getData();
  },
  methods: {
    getData() {
      var api = "http://39.98.108.48:5000/getinfo";
      // 1 represent have saled
      Axios.post(api, JSON.stringify({ gettype: 0 }), {
        headers: {
          "Content-Type": "application/x-www-form-urlencoded",
          Accept: "application/json"
        }
      })
        .then(res => {
          if (res.data.code === 200) {
            if (res.data.length === 0) {
              this.$message({
                showClose: true,
                message: "暂无信息",
                type: "info"
              });
            } else {
              this.tableData = res.data.items;
            }
          } else {
            this.$message({
              showClose: true,
              message: res.data.message,
              type: "error"
            });
          }
          this.loading = false;
        })
        .catch(err => {
          this.$message({
            showClose: true,
            message: err,
            type: "error"
          });
        });
    },
    saleAutomobile(index, rows, row) {
      this.$confirm("是否确定已售出?", "提示", {
        confirmButtonText: "确定",
        cancelButtonText: "取消",
        type: "warning"
      })
        .then(() => {
          var api = "http://39.98.108.48:5000/sale";
          Axios.post(
            api,
            JSON.stringify({
              carnumber: row.carnumber,
              saledate: this.getDate()
            }),
            {
              headers: {
                "Content-Type": "application/x-www-form-urlencoded",
                Accept: "application/json"
              }
            }
          )
            .then(res => {
              if (res.data.code === 200) {
                this.$message({
                  showClose: true,
                  message: "售出成功",
                  type: "success"
                });
                rows.splice(index, 1);
              } else {
                this.$message({
                  showClose: true,
                  message: res.data.message,
                  type: "error"
                });
              }
            })
            .catch(err => {
              this.$message({
                showClose: true,
                message: err,
                type: "error"
              });
            });
        })
        .catch(() => {
          this.$message({
            showClose: true,
            type: "info",
            message: "取消售出"
          });
        });
    },
    // get current date, format: YYYY-MM-DD
    getDate() {
      var date = new Date();
      var seperator1 = "-";
      var year = date.getFullYear();
      var month = date.getMonth() + 1;
      var strDate = date.getDate();
      if (month >= 1 && month <= 9) {
        month = "0" + month;
      }
      if (strDate >= 0 && strDate <= 9) {
        strDate = "0" + strDate;
      }
      var currentdate = year + seperator1 + month + seperator1 + strDate;
      return currentdate;
    }
  }
};
</script>