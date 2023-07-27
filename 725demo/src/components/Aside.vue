
<template>
  <div class="menu">
    <div class="head-img">
      <img src="../assets/tx.jpg" alt="" class="h-img">
      <span>ClinEd</span>
    </div>
    <el-menu class="el-menu-vertical-demo" :default-active="$route.path" router text-color="#fff"
      background-color="#3d85ad" active-text-color="#ffd04b">
      <el-menu-item index="/home">
        <i class="el-icon-s-home"></i>
        <span slot="title">Home</span>
      </el-menu-item>

      <el-menu-item index="/listview">
        <i class="el-icon-menu"></i>
        <span slot="title">Course View</span>
      </el-menu-item>
      <el-menu-item index="/listview2">
        <i class="el-icon-menu"></i>
        <span slot="title">Lecture View</span>
      </el-menu-item>
      <el-menu-item index="/study">
        <i class="el-icon-chat-round"></i>
        <span slot="title">Study Cards</span>
      </el-menu-item>

      <el-menu-item index="/home">
        <i class="el-icon-setting"></i>
        <span slot="title">Settings</span>
      </el-menu-item>

      <el-menu-item index="/login">
        <i class="el-icon-switch-button"></i>
        <span slot="title">Log out</span>
      </el-menu-item>
    </el-menu>
  </div>
</template>

<script>

export default {
  name: "Aside",
  data() {
    return {
    }
  },
  created() {

  },
  methods: {
    handleOpen(key, keyPath) {
      console.log(key, keyPath);
    },
    handleClose(key, keyPath) {
      console.log(key, keyPath);
    },
  },
}
</script>

<style lang="less"  scoped>
.el-menu-vertical-demo {
  width: 260px;
  height: calc(100vh - 160px);
}

.menu {
  width: 260px;
  background-color: #3d85ad;
}

.head-img {
  display: flex;
  align-items: center;
  justify-content: center;
  padding-top: 80px;
  margin-bottom: 30px;
}

.head-img>img {
  width: 50px;
  height: 50px;
  border-radius: 50%;
}

.head-img>span {
  color: #fff;
}

.el-menu-item {
  width: 65%;
  height: 40px;
  line-height: 40px;
  margin: 0 auto;
  text-align: left;
}

.el-menu-item>i {
  color: #fff;
}

.el-menu>.is-active {
  color: #3c84ab !important;
  background-color: #effffd !important;
  border-radius: 10px;

  i {
    color: rgb(255, 208, 75)
  }
}
</style>
