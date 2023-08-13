
<template>
  <div class="container">
    <div class="left-tree">
      <div style="color: #fff;text-align: left;padding-left: 10px;height: 70px;">
        <h3>Edit Table of Contents:</h3>
        <input type="text"
          style="border: 1px solid #534e5c;background: transparent;height: 30px;outline: none;color: #fff;">
          <el-button  round style="float: right; margin-right: 15px;" @click="goHome">Home</el-button>
      </div>
      <el-tree :data="treeData" :props="defaultProps" @node-click="handleNodeClick"></el-tree>
    </div>
    <div class="right-content">
      <h2>{{ $route.query.name }}</h2>
      <div class="content-item">
        <h3>1. Gram Negative Bacteria</h3>
        <p>"Loremm ipsum dalor slt amet, consectetur adipiscing elit, sed do elusmod temporincididunt ut labore et dolore
          magna aliqua. Ut enim ad minim veniam, quis nostrudexercitation ullamco laboris nisi ut aliquip ex ea commodo
          consequat. Duis aute iruredolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla
          pariaturExcepteur sint occaecat cupidatat non proident. sunt in culpa qui officia deserunt mollitanim id ost
          Inborum .</p>
        <p>Sed ut perspiciatis unde arnnis iste natus erro sit voluptaterm accusantium dolorernqudlaudantium, totam rerm
          aperiam, eaque ipsa qune ab illo irventore yeritatis et quasi</p>
      </div>
      <div class="content-item">
        <h3>2. Gram Positive Bacteria</h3>
        <p>"" Loremn ipsum dalor sit amet, consectetur adipiscing elit, sed do eiusmod temporincididunt ut labore et
          dolore magna aliqua, Ut enim ad minim veniam, quis nostrudexercitation ullamco laboris nisi ut aliquip ex ea
          commado cansequat. Duis aute iruredolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla
          pariatur .Excepteur sint occaecat cupidatat nan proident. sunt in culpa guf officla deserunt mallitanimm id est
          laborum .</p>
        <p>Sed ut perspiciatis unde arnnis iste natus erro sit voluptaterm accusantium dolorernqudlaudantium, totam rerm
          aperiam, eaque ipsa qune ab illo irventore yeritatis et quasi</p>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      treeData: [{
        label: 'a.peptidoglycan',
        children: [{
          label: 'i. peptidoglycan synthesis',
        },
        {
          label: 'ii. peptidoglycan synthesis',
        },
        {
          label: 'iii. peptidoglycan synthesis',
        }]
      },
      {
        label: 'b.peptidoglycan',
        children: [{
          label: 'i. peptidoglycan synthesis',
        },
        {
          label: 'ii. peptidoglycan synthesis',
        },
        {
          label: 'iii. peptidoglycan synthesis',
        }]
      },
      {
        label: 'c.peptidoglycan',
        children: [{
          label: 'i. peptidoglycan synthesis',
        },
        {
          label: 'ii. peptidoglycan synthesis',
        },
        {
          label: 'iii. peptidoglycan synthesis',
        }]
      },

      ],
      defaultProps: {
        children: 'children',
        label: 'label'
      }
    }
  },
  methods: {
    handleNodeClick(data) {
      console.log(data);
    },
    goHome(){
      this.$router.push({
        path: '/'
      });
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

  .left-tree {
    width: 20%;
    background-color: #2f2144;
  }
}

.el-tree {
  background: #2f2144;
  color: #fff;
}

v::deep .is-current {
  color: #000;
}

.right-content {
  flex: 1;
  padding: 5px 20px;
  background-color: #fff;

  h2 {
    text-align: left;
  }

  .content-item {
    width: 75%;
    text-align: left;
    padding-left: 15px;
    margin-bottom: 30px;

    h3 {
      padding-left: 25px;
    }

    p {
      line-height: 25px;
    }
  }
}</style>