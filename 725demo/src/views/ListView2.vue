<template>
  <div class="container">
    <div class="box left-box">
      <div class="image-container">
        <img src="../assets/listview2.png" alt="">
      </div>
      <div class="content-container">
        <h3>Lecturel</h3>
        <h4>Full Lecture Transcript</h4>
        <p class="description-text">Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do
          eiusmod tempor incididunt ut labore et dolore magna aliqua. Utenim ad minim veniam, quis nostrud exercitation
          ullamco laboris nisiut aliquip ex ea commodo consequat, Duis gute irure dolor inreprehenderit in voluptate velit
          esse cillum dolore eu fugiat nullopariatur. Excepteur sint occaecat cupidatat non proident, sunt inculpa qui
          officia deserunt mollit anim id est laborum.</p>
        <div class="right-box-item">
          <div>Lecture Handout</div>
          <div class="arrow-right"> > </div>
        </div>
      </div>
    </div>
    <div class="box right-box">
      <div class="content-container">
        <h3>Lecture Materials</h3>
        <div class="right-box-item" v-for="(item, index) in arr" :key="index">
          <div>{{ item }}</div>
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
      arr: ['Lecture Summary', 'Handout Summary', 'Study Cards']
    }
  },
}
</script>

<style lang="less" scoped>
.container {
  display: flex;
  justify-content: space-between;
  align-items: stretch; 
  background: #ececec;
  height: 100vh; 
}

.box {
  flex: 1;
  background: #fff;
  display: flex;
  flex-direction: column; 
}

.image-container {
  img {
    width: 100%;
    height: auto;
  }
}

.content-container {
  padding: 20px;

  .description-text {
    margin: 0; 
    line-height: 25px;
    word-wrap: break-word;
  }
}

.right-box-item {
  display: flex;
  justify-content: space-between;
  background: #c2d7ef;
  margin: 10px 0;
  padding: 20px;
  align-items: center;
  .arrow-right {
    margin-right: 20px;
    cursor: pointer;
  }
}

.right-box {
  background: #ececec;
}

.btn {
  display: inline-block;
  width: 100%;
  line-height: 45px;
  margin-top: 20px;
  background: #476b9a;
  color: #fff;
  text-align: center;
  font-weight: bold;
  cursor: pointer;
}
</style>