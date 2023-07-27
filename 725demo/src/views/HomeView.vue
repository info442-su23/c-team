<template>
  <div class="content-wrapper">
    <div class="input-search">
      <input type="text" v-model="searchValue" class="input" placeholder="Search...">
      <i class="el-icon-search"></i>
    </div>
    <div class="course">
      <div class="course-title">
        Your course <span class="course-title-add">Add course</span>
      </div>
      <div class="carousel-box">
        <div class="btn" style="right: -70px;" @click="handleNext"> > </div>
        <div class="btn" style="left: -70px;" @click="handlePre"> &lt </div>
        <el-carousel indicator-position="none" arrow="never" :autoplay="false" ref="carousel">
          <el-carousel-item v-for="item in 4" :key="item">
            <div style="margin-left:50px;width: 90%;height: 100%; display: flex; justify-content: space-between;">
              <div class="carousel-left">
                <img src="../assets/yiliao.jpg" alt="">
                <div class="modal">
                  <p style="color:#fff;padding-left: 15px;">Introduction {{ item }}</p>
                </div>
              </div>
              <div class="carousel-right">
                <div class="carousel-right-detail">
                  <img src="../assets/office.png" alt="" class="carousel-img">
                  <p>Add course to you clied</p>
                  <div class="add-btn">Add Course</div>
                </div>
              </div>
            </div>
          </el-carousel-item>
        </el-carousel>
      </div>
    </div>
    <div class="middle-content">
      <div class="middle-content-item">
        <div style="font-size: 18px; text-align: left;">ClinEd Quiz <span
            style="font-size: 14px; cursor: pointer;color: #559cc6;">See
            All</span></div>
        <div class="item-detail flex-center" v-for="item in 3">
          <div style="width: 50%;cursor: pointer;" class="flex-center" @click="goOtherPage">
            <img src="../assets/tx.jpg" alt="">
            <div style="margin-left: 20px;">
              <span style="color: #fff;margin-bottom: 2px;display: inline-block;">Introduction</span>
              <el-progress :percentage="percentage" define-back-color="#527a99" :show-text="false" :color="customColor"
                style="width: 180px;"></el-progress>
            </div>
          </div>
          <div style="width: 100px;margin-right: 10px;color:#fff;font-weight: bold;">12/39</div>
        </div>
      </div>
      <div class="middle-content-item">
        <span style="font-size: 18px;display: inline-block; width: 100%; text-align: left;">Study Goals</span>
        <div class="circle-line">
          <span class="num">9/10</span>
          <el-progress type="dashboard" color="#85ccfe" :stroke-width="15" :percentage="88"
            :show-text="false"></el-progress>
        </div>
        <div class="bar">
          <div id="main" style="width: 450px;height: 230px;"></div>
        </div>
      </div>
    </div>
    <div class="bottom-content">
      <span style="font-size: 18px;display: inline-block; text-align: left;">Suggested Courses</span>
      <div @click="goOtherPage" style="width: 100%;justify-content: space-between;margin-top: 20px; cursor: pointer;"
        class="flex-center">
        <div class="bottom-content-item" v-for="item in 5">
          <div class="bottom-top">
            <div style="width:50%">
              <img src="../assets/tx.jpg" alt=""
                style="width: 30px;height: 30px;border-radius: 50%;vertical-align: middle;">
              <span style="color:#fff;font-size: 15px;">Greg Hay</span>
            </div>
            <div style="width: 45%;">
              <div class="cards"> 82 cards</div>
              <span style="color:#fff;font-size: 15px;"><i class="el-icon-setting"></i>6.7K</span>
            </div>
          </div>
          <div style="color: #fff;">
            <h2>Bio 679</h2>
            <p>XXXXXXXXXXXXXXXXXX</p>
            <p>XXXXXXXXXXXXXXXXXX</p>
            <p>XXXXXXXXXXXXXXXXXX</p>
            <p>XXXXXXXXXXXXXXXXXX</p>
            <p>XXXXXXXXXXXXXXXXXX</p>
            <p>XXXXXXXXXXXXXXXXXX</p>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import * as echarts from 'echarts';
export default {
  name: 'HomeView',
  data() {
    return {
      searchValue: '',
      percentage: 20,
      customColor: '#91cdea',
    }
  },
  created() {
  },
  mounted() {
    this.drawBar();
  },
  methods: {
    drawBar() {
      var chartDom = document.getElementById('main');
      var myChart = echarts.init(chartDom);
      var option;

      option = {
        xAxis: {
          type: 'category',
          data: ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'],
          axisTick: {
            show: false
          }
        },
        yAxis: {
          type: 'value',
          show: false
        },
        series: [
          {
            data: [100, 170, 120, 50, 30, 90, 110],
            type: 'bar',
            barWidth: 12,
            itemStyle: {
              color: '#b8d5e5'
            }
          },
          {
            data: [120, 200, 150, 80, 70, 110, 130],
            type: 'bar',
            barWidth: 12,
            itemStyle: {
              color: '#61a9d4'
            }
          }
        ]
      };
      option && myChart.setOption(option);
    },
    handlePre() {
      this.$refs.carousel.prev()
    },
    handleNext() {
      this.$refs.carousel.next()
    },
    goOtherPage() {
      alert('go other page')
    }
  },
}
</script>
<style lang="less" scoped>
.flex-center {
  display: flex;
  align-items: center;
}

.flex {
  display: flex;
}

#app {
  width: 100%;
  height: 100vh;
  display: flex;
}

.content-wrapper {
  width: calc(100% - 260px);
  height: 100%;
  overflow-y: auto;
}

.input-search {
  width: 1100px;
  height: 50px;
  margin-left: 120px;
  margin-top: 15px;
  position: relative;
  background: #effffe;
  border-radius: 10px;
}

.input {
  border: none;
  outline: none;
  width: 90%;
  background: #effffe;
  height: 100%;
  border-radius: 10px;
  color: #000;
  margin-left: 45px;
}

.el-icon-search {
  font-size: 20px;
  position: absolute;
  left: 20px;
  top: 15px;
}

.course {
  margin-top: 10px;
}

.course-title {
  font-size: 18px;
  color: #000;
  margin: 5px 0;
  margin-left: 120px;
  text-align: left;
}

.course-title-add {
  color: #83b7cc;
  font-size: 15px;
}

.carousel-box {
  width: 85%;
  margin: 0 auto;
  position: relative;
}

.carousel-box .btn {
  position: absolute;
  top: 50%;
  transform: translateY(-50%);
  width: 50px;
  height: 50px;
  color: #fff;
  cursor: pointer;
  line-height: 50px;
  text-align: center;
  background: #3c84ab;
  z-index: 99;
  border-radius: 10px;
  font-size: 18px;
}

.carousel-left,
.carousel-right {
  width: 43%;
  height: 100%;
  border-radius: 20px;
  position: relative;
}

.carousel-left>img {
  width: 100%;
  height: 100%;
  border-radius: 20px;
}

.modal {
  border-radius: 20px;
  position: absolute;
  bottom: 0;
  left: 0;
  height: 50%;
  width: 100%;
  z-index: 2;
  background: linear-gradient(#418baf, transparent);
}

.carousel-right {
  background: linear-gradient(#418baf, transparent);
  /* box-shadow: 2px 2px 2px 2px #999; */
  display: flex;
  justify-content: center;
  align-items: center;
}

.carousel-right-detail {
  width: 200px;
  height: 100%;
}

.carousel-img {
  width: 120px;
  height: 100px;
  padding-top: 20px;
  margin-left: 40px;
}

.carousel-right-detail>p {
  color: #fff;
  text-align: center;
  font-size: 14px;
}

.carousel-right-detail>.add-btn {
  color: #fff;
  text-align: center;
  width: 100%;
  height: 30px;
  line-height: 30px;
  cursor: pointer;
  background: #3e83a9;
  border-radius: 10px;
}

.el-carousel {
  border-radius: 20px;
}

.middle-content,
.bottom-content {
  width: 85%;
  margin: 20px auto;
  height: 260px;
  display: flex;
  justify-content: space-between;
}

.middle-content-item {
  width: 47%;
}

.item-detail {
  width: 100%;
  height: 70px;
  background: linear-gradient(#5ca3cd, #7ec6f6);
  border-radius: 10px;
  margin: 5px 0;
  justify-content: space-between;
}

.item-detail>div>img {
  width: 50px;
  height: 50px;
  border-radius: 50%;
  margin-left: 10px;
}

.circle-line {
  width: 20%;
  position: relative;
  margin-top: 50px;
  display: inline-block;
  vertical-align: top;
}

.num {
  font-size: 23px;
  font-weight: bold;
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
}

.bar {
  width: 75%;
  height: 230px;
  display: inline-block;
  margin-left: 17px;
}

.bottom-content {
  flex-wrap: wrap;
}

.bottom-content-item {
  width: 240px;
  height: 300px;
  background: linear-gradient(#5292b5, transparent);
  border-radius: 20px;
  padding: 6px;
}

.bottom-content-item>p {
  color: #fff;
}

.el-menu-item {
  width: 65%;
  height: 40px;
  line-height: 40px;
  margin: 0 auto;
}

.el-menu-item>i {
  color: #fff;
}

.el-menu>.is-active {
  color: #3c84ab !important;
  background-color: #effffd !important;
  border-radius: 10px;
}

.bottom-top {
  width: 100%;
  height: 50px;
  display: flex;
  align-items: center;
  justify-content: space-between;
}

.cards {
  width: 50px;
  height: 20px;
  text-align: center;
  line-height: 20px;
  color: #fff;
  background-color: #85cdfd;
  border-radius: 5px;
  cursor: pointer;
  font-size: 11px;
  display: inline-block;
}
</style>
