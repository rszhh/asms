<template>
  <div>
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
            @click.native.prevent="deleteRow(scope.$index, tableData, scope.row)"
            type="danger"
            size="mini"
          >删除</el-button>
          <el-button type="info" size="mini" @click="putInfo(scope.row)">编辑</el-button>
        </template>
      </el-table-column>
    </el-table>
    <el-dialog title="修改信息" :visible.sync="dialogFormVisible">
      <el-form :model="form" id="cde">
        <el-form-item label="类型" :label-width="formLabelWidth">
          <el-input v-model="form.type" autocomplete="off"></el-input>
        </el-form-item>
        <el-form-item label="品牌" :label-width="formLabelWidth">
          <el-input v-model="form.brand" autocomplete="off"></el-input>
        </el-form-item>
        <el-form-item label="颜色" :label-width="formLabelWidth">
          <el-input v-model="form.color" autocomplete="off"></el-input>
        </el-form-item>
        <el-form-item label="价格" :label-width="formLabelWidth">
          <el-input v-model="form.price" autocomplete="off"></el-input>
        </el-form-item>
        <el-form-item label="出厂日期" :label-width="formLabelWidth">
          <el-input v-model="form.entrydate" autocomplete="off"></el-input>
        </el-form-item>
      </el-form>
      <div slot="footer" class="dialog-footer">
        <el-button @click="dialogFormVisible = false">取 消</el-button>
        <el-button type="primary" @click="changeInfo()">确 定</el-button>
      </div>
    </el-dialog>
  </div>
</template>

<style>
body {
  margin: 0;
}
#cde {
  width: 70%;
}
</style>

<script>
import Axios from "axios";
export default {
  data() {
    return {
      tableData: [],
      loading: true,
      dialogFormVisible: false,
      form: {
        optiontype: 1,
        carnumber: "",
        type: "",
        brand: "",
        color: "",
        price: "",
        entrydate: ""
      },
      formLabelWidth: "120px"
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
    deleteRow(index, rows, row) {
      this.$confirm("此操作将永久删除该信息, 是否继续?", "提示", {
        confirmButtonText: "确定",
        cancelButtonText: "取消",
        type: "warning"
      })
        .then(() => {
          var api = "http://39.98.108.48:5000/options";
          Axios.post(
            api,
            JSON.stringify({
              optiontype: 0,
              carnumber: row.carnumber
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
                  message: "删除成功",
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
            message: "已取消删除"
          });
        });
    },
    putInfo(row) {
      this.form.carnumber = row.carnumber;
      this.form.type = row.type;
      this.form.brand = row.brand;
      this.form.color = row.color;
      this.form.price = row.price;
      this.form.entrydate = row.entrydate;
      this.dialogFormVisible = true;
    },
    changeInfo() {
      var api = "http://39.98.108.48:5000/options";
      Axios.post(api, JSON.stringify(this.form), {
        headers: {
          "Content-Type": "application/x-www-form-urlencoded",
          Accept: "application/json"
        }
      })
        .then(res => {
          if (res.data.code === 200) {
            this.$message({
              showClose: true,
              message: "修改成功",
              type: "success"
            });
            for (let i = 0; i < this.tableData.length; i++) {
              if (this.tableData[i].carnumber === this.form.carnumber) {
                this.tableData[i].type = this.form.type;
                this.tableData[i].brand = this.form.brand;
                this.tableData[i].color = this.form.color;
                this.tableData[i].price = this.form.price;
                this.tableData[i].entrydate = this.form.entrydate;
                break;
              }
            }
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
      this.dialogFormVisible = false;
    }
  }
};
</script>