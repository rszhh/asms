<template>
  <d2-container>
    <template slot="header">汽车类型销售统计</template>
    <div class="inner">
      <ve-pie :data="chartData" v-bind="pubSetting"></ve-pie>
    </div>
  </d2-container>
</template>

<script>
import Axios from "axios";
import list from "@/views/list.js";
export default {
  mixins: [list],
  data() {
    return {
      chartData: {
        columns: ["type", "froportion"],
        rows: [
          { type: "家用轿车", froportion: 0 },
          { type: "SUV", froportion: 0 },
          { type: "越野车", froportion: 0 }
        ]
      }
    };
  },
  mounted() {
    this.getData();
  },
  methods: {
    getData() {
      var api = "http://IP:5000/type";
      Axios.post(api)
        .then(res => {
          if (res.data.code === 200) {
            if (res.data.length === 0) {
              this.$message({
                showClose: true,
                message: "暂无信息",
                type: "info"
              });
            } else {
              this.chartData.rows[0].froportion = res.data.saloon;
              this.chartData.rows[1].froportion = res.data.suv;
              this.chartData.rows[2].froportion = res.data.cross;
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

<style lang="scss" scoped>
.inner {
  position: absolute;
  top: 20px;
  right: 20px;
  bottom: 20px;
  left: 20px;
}
</style>

