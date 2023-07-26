<template>
  <div class="container">
    <div class="top-menu">
      <div :class="['menu-item', { active: index === tabIndex }]" v-for="(item, index) in arr" :key="index"
        @click="changeTab(index)">
        <i :class="item.icon"></i>
        <span>{{ item.name }}</span>
      </div>
    </div>
    <div class="content" v-show="tabIndex===0">

    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      arr: [{ name: 'Card View', icon: 'el-icon-menu' }, { name: 'List View', icon: 'el-icon-s-operation' }, { name: 'Study View', icon: 'el-icon-document' }],
      tabIndex: 0
    }
  },
  methods: {
    changeTab(index) {
      this.tabIndex = index
    }
  },

}
</script>

<style lang="less" scoped>
.container {
  background: #ececec;
  padding: 50px;
  border: 1px solid #000;

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
      }
    }

    .active {
      background: #2fa1ed;
    }
  }
}</style>