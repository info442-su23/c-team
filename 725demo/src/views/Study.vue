
<template>
  <div class="container">
    <div class="top-menu">
      <div :class="['menu-item', { active: index === tabIndex }]" v-for="(item, index) in arr" :key="index"
        @click="changeTab(index)">
        <i :class="item.icon"></i>
        <span>{{ item.name }}</span>
      </div>
    </div>
    <div class="content-box">
      <div class="content" v-show="tabIndex === 0">
        <div class="top-icon">
          <i class="el-icon-edit"></i>
          <i class="el-icon-star-on"></i>
        </div>
        <div style="height: 500px;">
          <el-carousel indicator-position="none" arrow="never" :autoplay="false" ref="carousel" @change="handleChange">
            <el-carousel-item v-for="item in 26" :key="item">
              <div class="text flex-center">
                {{ item }}.Wuchereria bancrofti
              </div>
            </el-carousel-item>
          </el-carousel>
        </div>
        <div class="bottom-btn flex-center">
          <div class="btn flex-center" @click="handlePre">
            <i class="el-icon-back"></i>
          </div>
          <div class="cal-index">
            {{ curIndex }}/26
          </div>
          <div class="btn flex-center" @click="handleNext">
            <i class="el-icon-right"></i>
          </div>
        </div>
      </div>
      <div class="content2" v-show="tabIndex === 1">
        <h3 style="text-align: left;">Lecturel</h3>
        <div class="lecturel-item" v-for="item in 6">
          <div class="lecturel-item-left">
            1. Wuchereria bancrofti
          </div>
          <div class="lecturel-item-left right">
            <span>
              A nematode that causes lymphatic filariasis,also known as elephantiasis .
            </span>
            <div class="top-icon">
              <i class="el-icon-edit"></i>
              <i class="el-icon-star-on"></i>
            </div>
          </div>
        </div>
      </div>
      <div class="content content3" v-show="tabIndex === 2">
        <div class="top-icon">
          <i class="el-icon-edit"></i>
          <i class="el-icon-star-on"></i>
        </div>
        <div style="height: 200px;">
          <el-carousel indicator-position="none" arrow="never" :autoplay="false" ref="carousel1">
            <el-carousel-item v-for="item in 26" :key="item">
              <div class="text flex-center">
                {{ item }}.Wuchereria bancrofti
              </div>
            </el-carousel-item>
          </el-carousel>
        </div>
        <div class="answer-box">
          <div :class="['answer-item', { 'correct': correctValue == item.value, 'wrong': wrongValue == item.value }]"
            v-for="(item, index) in answerArr" :key="index" @click="handleAnswer(item)">{{ item.label }}
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      arr: [{ name: 'Card View', icon: 'el-icon-menu' }, { name: 'List View', icon: 'el-icon-s-operation' }, { name: 'Study View', icon: 'el-icon-document' }],
      tabIndex: 2,
      curIndex: 1,
      answerArr: [{ label: 'a. quis nostrud exercitation', value: 'A' }, { label: 'b. ullamco laboris nisi ut', value: 'B' },
      { label: 'c. irure dolor in reprehende', value: 'C' }, { label: 'd. voluptate velit esse cillum', value: 'D' }],
      correctValue: '',
      wrongValue: ''
    }
  },
  methods: {
    changeTab(index) {
      this.tabIndex = index
    },
    handlePre() {
      this.$refs.carousel.prev()
    },
    handleNext() {
      this.$refs.carousel.next()
    },
    handleChange(index) {
      this.curIndex = index + 1
    },
    handleAnswer(item) {
      if (item.value == 'A' || item.value == 'C') {
        this.$message.success('Correct answer!')
        this.correctValue = item.value
        this.wrongValue = ''
        setTimeout(() => {
          this.$refs.carousel1.next()
          this.correctValue = ''
        }, 2000)
      } else {
        this.$message.error('Wrong answer! The correct is A')
        this.wrongValue = item.value
        // setTimeout(()=>{
        //   this.wrongValue =''
        // },1000)
      }
    }

  },

}
</script>

<style lang="less" scoped>
.container {
  background: #ececec;
  padding: 50px;

  .top-menu {
    width: 100%;
    display: flex;

    .menu-item {
      width: 150px;
      height: 50px;
      line-height: 50px;
      display: flex;
      justify-content: space-around;
      align-items: center;
      color: #fff;
      margin-right: 15px;
      background: #c6e8fb;
      border-radius: 10px;
      cursor: pointer;

      i {
        color: #000;
        font-size: 25px;
        cursor: pointer;
      }
    }

    .active {
      background: #2fa1ed;
    }
  }

  .content-box {
    position: relative;
  }

  .content {
    width: 1160px;
    height: 600px;
    background: #bde9fc;
    border-radius: 20px;
    margin-top: 50px;

    .top-icon {
      text-align: right;
      margin-right: 20px;

      i {
        font-size: 45px;
        color: #000;
        margin-top: 20px;
        margin-right: 15px;
        cursor: pointer;
      }
    }

    .text {
      font-size: 50px;
      color: #000;
      height: 500px;
    }

    .bottom-btn {
      width: 90%;
      height: 80px;
      margin: 60px auto;
      justify-content: space-between;

      .btn {
        width: 50px;
        height: 50px;
        border-radius: 50%;
        background: #c6e8fb;
        cursor: pointer;

        i {
          color: #fff;
          font-size: 35px;
          cursor: pointer;
        }
      }

      .cal-index {
        color: #000;
        font-size: 30px;
        font-weight: bold;
      }
    }
  }

  .content2 {
    margin-top: 50px;

    .lecturel-item {
      width: 1120px;
      height: 80px;
      background: #c2d7ef;
      display: flex;
      align-items: center;
      margin-bottom: 25px;
      cursor: pointer;

      .lecturel-item-left {
        width: 40%;
        border-right: 3px solid #000;
        height: 100%;
        line-height: 80px;
        padding-left: 30px;
        text-align: left;
        color: #000;
        font-size: 18px;
      }

      .right {
        width: 59%;
        border-right: none;
        display: flex;
        align-items: center;
        justify-content: space-between;

        span {
          width: 400px;
          margin-left: 20px;
          line-height: 20px;
        }

        .top-icon {
          i {
            font-size: 30px;
            margin-top: 20px;
            margin-right: 15px;
            cursor: pointer;
          }
        }
      }
    }
  }

  .content3 {
    height: 400px;

    .text {
      height: 200px;
    }

    .answer-box {
      width: 95%;
      display: flex;
      justify-content: space-between;
      flex-wrap: wrap;
      align-items: center;
      margin: 180px auto;

      .answer-item {
        width: 500px;
        height: 90px;
        background: #c6e8fb;
        text-align: center;
        line-height: 90px;
        padding-left: 20px;
        margin-bottom: 40px;
        border-radius: 20px;
        font-size: 30px;
        cursor: pointer;
      }

      .correct {
        background: #0ee291;
      }

      .wrong {
        background: red;
      }
    }
  }
}</style>