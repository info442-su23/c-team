<template>
  <div class="container">
    <div class="left-box">
      <div class="left-box-top">
        <img src="../assets/listview1.png" alt="">
      </div>
      <div class="left-box-bottom">
        <h3>Medical 101</h3>
        <h4>Course Description</h4>
        <p style="margin: 0; line-height: 25px;">in this course, vou will learn the foundations of medical sciences.
          Wewill cover topics such as anatomy,
          medical terminology, and clinicaskills. This course is designed to provide you with a solidunderstanding of the
          medical field.</p>
      </div>
    </div>
    <div class="right-box">
      <div class="right-box-content">
        <h3>Course Overview</h3>
        <div class="right-box-item" v-for="(item,index) in arr" :key="index">
          <div style="margin-left: 20px;">{{item}}</div>
          <div class="arrow-right"> > </div>
        </div>
        <div class="btn">Enroll now</div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      arr: ['Study Guide','Text Books','Lecture 1','Lecture 2','Lecture 3']
    }
  },

}
</script>

<style lang="less" scoped>
.container {
  background: #ececec;
  display: flex;
  justify-content: space-between;
  align-items: center;

  .left-box {
    width: 47%;
    height: 100%;
    background: #fff;

    .left-box-top {
      width: 650px;
      height: 380px;
      margin: 50px auto;

      img {
        width: 100%;
        height: 100%;
      }
    }

    .left-box-bottom {
      width: 650px;
      margin: 50px auto;
      text-align: left;
    }
  }

  .right-box {
    width: 47%;
    height: 100%;

    .right-box-content {
      margin: 20px auto;
      width: 80%;
      height: 800px;
      text-align: left;
      .btn{
        width: 100%;
        height: 45px;
        line-height: 45px;
        color: #fff;
        background: #476b9a;
        font-weight: bold;
        text-align: center;
        cursor: pointer;
        margin-top: 200px;
      }
    }
    .right-box-item{
      height: 80px;
      display: flex;
      justify-content: space-between;
      align-items: center;
      background: #c2d7ef;
      line-height: 80px;
      margin: 10px 0;
      font-weight: bold;
      .arrow-right{
        width: 50px;
        height: 50px;
        line-height: 50px;
        text-align: center;
        color: #000;
        border: 1px solid #000;
        border-radius: 3px;
        cursor: pointer;
        margin-right: 20px;
      }
    }

  }
}
</style>