<!--
 * @Author: Corn
 * @Date: 2023-07-25 17:40:28
 * @LastEditors: corn
 * @LastEditTime: 2023-07-26 09:27:35
 * @FilePath: \725demo\src\views\Login.vue
 * @Description: 
 * 
 * Copyright (c) 2023 by corn, All Rights Reserved. 
-->
<template>
  <div class="wrapper flex-center" style="background-color: #eef3fa;">
    <div class="login-box">
      <div class="box-left flex-center">
        <img src="../assets/login.png" alt="">
        <div style="width: 100%; margin-top: -80px;">
          <h2>Learn Medical <br> Sciences with Clin-Ed.</h2>
          <h4>All your courses, lectures, tutorials <br> and study materials in one place</h4>
        </div>
      </div>
      <div class="box-right">
        <div class="top-title">
          <h1>Clin-Ed</h1>
          <p>Online Education Platform</p>
        </div>
        <div class="input-box">
          <h1>Log in</h1>
          <p>Course Name</p>
          <input type="text" placeholder="Enter course name">
          <p>Password</p>
          <input type="password" placeholder="Enter password">
          <div class="btn" @click="handleLogin">Log in</div>
          <h4 style="cursor: pointer;">Forgot your password?</h4>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
    }
  },
  methods: {
    handleLogin() {
      this.$router.push({
        path: '/home',
      });
    }
  },

}
</script>

<style lang="less" scoped>
.login-box {
  width: 1300px;
  height: 800px;
  background: #fff;
  border-radius: 20px;
  display: flex;
  justify-content: space-between;

  .box-left {
    background-color: #476b9a;
    width: 47%;
    height: 100%;
    flex-wrap: wrap;
    border-radius: 20px 0 0 20px;

    img {
      width: 410px;
      height: 410px;
    }

    color: #fff;
  }

  .box-right {
    width: 47%;
    height: 100%;
    border-radius: 0 20px 20px 0;

    .top-title {
      text-align: right;
      margin-top: 50px;
      margin-right: 20px;
      color: #333;
    }

    .input-box {
      width: 350px;
      margin: 100px auto;
      text-align: left;

      h1 {
        margin: 20px 0;
      }

      p {
        margin: 20px 0;
      }

      input {
        height: 45px;
        width: 100%;
        border: 1px solid #797979;
        outline: none;
        background: #fff;
      }

      .btn {
        width: 355px;
        height: 55px;
        line-height: 55px;
        text-align: center;
        color: #fff;
        background: #476b9a;
        cursor: pointer;
        margin: 20px 0;
      }
    }
  }
}
</style>