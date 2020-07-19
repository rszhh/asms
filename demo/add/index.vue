<template>
  <div>
    <br />
    <el-tooltip placement="top">
      <div slot="content">在此处增加汽车信息</div>
      <el-button>添加汽车</el-button>
    </el-tooltip>
    <br />
    <br />
    <el-form
      :model="ruleForm"
      :rules="rules"
      ref="ruleForm"
      label-width="150px"
      class="demo-ruleForm"
    >
      <el-form-item label="汽车品牌" prop="brand" id="abc">
        <el-input v-model="ruleForm.brand" placeholder="请输入汽车品牌"></el-input>
      </el-form-item>
      <el-form-item label="汽车类型" prop="type">
        <el-select v-model="ruleForm.type" placeholder="请选择汽车类型">
          <el-option label="家用轿车" value="家用轿车"></el-option>
          <el-option label="SUV" value="SUV"></el-option>
          <el-option label="越野车" value="越野车"></el-option>
        </el-select>
      </el-form-item>
      <el-form-item label="汽车颜色" prop="color" id="abc">
        <el-input v-model="ruleForm.color" placeholder="请输入汽车颜色"></el-input>
      </el-form-item>
      <el-form-item label="汽车价格" prop="price" id="abc">
        <el-input v-model="ruleForm.price" placeholder="请输入汽车价格" type="number"></el-input>
      </el-form-item>
      <el-form-item label="出厂时间" required id="bcd">
        <el-col :span="11">
          <el-form-item prop="date">
            <el-date-picker
              type="date"
              placeholder="选择日期"
              v-model="ruleForm.entrydate"
              style="width: 100%;"
            ></el-date-picker>
          </el-form-item>
        </el-col>
      </el-form-item>
      <el-form-item>
        <el-button type="primary" @click="submitForm('ruleForm')">立即创建</el-button>
        <el-button @click="resetForm('ruleForm')">重置</el-button>
      </el-form-item>
    </el-form>
  </div>
</template>

<style>
#abc {
  width: 50%;
}
#bcd {
  width: 70%;
}
</style>

<script>
import Axios from "axios";
export default {
  data() {
    return {
      ruleForm: {
        type: "",
        brand: "",
        color: "",
        price: "",
        entrydate: ""
      },
      rules: {
        brand: [
          { required: true, message: "请输入汽车品牌", trigger: "blur" },
          { min: 2, max: 10, message: "长度在 2 到 10 个字符", trigger: "blur" }
        ],
        color: [
          { required: true, message: "请输入汽车颜色", trigger: "blur" },
          { min: 2, max: 10, message: "长度在 2 到 10 个字符", trigger: "blur" }
        ],
        price: [
          { required: true, message: "请输入汽车价格", trigger: "blur" },
          { min: 2, max: 10, message: "长度在 2 到 10 个字符", trigger: "blur" }
        ],
        type: [
          { required: true, message: "请选择汽车类型", trigger: "change" }
        ],
        entrydate: [
          {
            type: "date",
            required: true,
            message: "请选择日期",
            trigger: "change"
          }
        ]
      }
    };
  },
  methods: {
    submitForm(formName) {
      this.$refs[formName].validate(valid => {
        this.ruleForm.entrydate =
          this.ruleForm.entrydate.getFullYear() +
          "-" +
          (this.ruleForm.entrydate.getMonth() + 1) +
          "-" +
          this.ruleForm.entrydate.getDate();
        var api = "http://IP:5000/add";
        Axios.post(api, JSON.stringify(this.ruleForm), {
          headers: {
            "Content-Type": "application/x-www-form-urlencoded",
            Accept: "application/json"
          }
        })
          .then(res => {
            if (res.data.code !== 200) {
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

        if (valid) {
          this.$message({
            showClose: true,
            message: "提交成功",
            type: "success"
          });
        } else {
          this.$message({
            showClose: true,
            message: "未知错误",
            type: "error"
          });
          return false;
        }
      });
    },
    resetForm(formName) {
      this.$refs[formName].resetFields();
    }
  }
};
</script>