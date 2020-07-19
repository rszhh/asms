<template>
  <div>
    <el-table v-loading="loading" :data="saleInfo" style="width: 100%" max-height="400">
      <el-table-column fixed prop="totalnumber" label="已售出总数量" width="120"></el-table-column>
    </el-table>
    <el-table v-loading="loading" :data="tableData" style="width: 100%" max-height="400">
      <el-table-column fixed prop="carnumber" label="汽车编号" width="120"></el-table-column>
      <el-table-column prop="type" label="类型" width="120"></el-table-column>
      <el-table-column prop="brand" label="品牌" width="120"></el-table-column>
      <el-table-column prop="color" label="颜色" width="120"></el-table-column>
      <el-table-column prop="price" label="价格" width="120"></el-table-column>
      <el-table-column prop="entrydate" label="出厂日期" width="150"></el-table-column>
      <el-table-column prop="saledate" label="售出日期" width="150"></el-table-column>
    </el-table>
  </div>
</template>

<script>
import Axios from "axios";
export default {
  data() {
    return {
      tableData: [],
      loading: true,
      saleInfo: []
    };
  },
  mounted() {
    this.getData();
  },
  methods: {
    getData() {
      var api = "http://39.98.108.48:5000/getinfo";
      // 1 represent have saled
      Axios.post(api, JSON.stringify({ gettype: 1 }), {
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
              let total = {
                totalnumber: res.data.items.length
              };
              // add total to saleInfo
              // can not use this.saleInfo = total
              this.saleInfo.push(total);
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
    }
  }
};
</script>