<template>
  <div class="container">
    <div class="box left-box">
      <div class="image-container">
        <input 
          type="file" 
          accept="image/*" 
          @change="handleFileUpload" 
          ref="fileInput"
          style="display: none" 
        />
        <img 
          :src="imageSrc" 
          alt="" 
          @click="editMode && $refs.fileInput.click()" 
        />
      </div>
      <div class="content-container">
        <h3 v-if="!editMode">{{ title }}</h3>
        <input v-else type="text" v-model="title" />

        <h4 v-if="!editMode">{{ subtitle }}</h4>
        <input v-else type="text" v-model="subtitle" />

        <p v-if="!editMode" class="description-text">{{ description }}</p>
        <textarea v-else class="description-text" v-model="description"></textarea>

        <button v-if="!editMode" class="edit-button" @click="editMode = true">✎</button>
        <button v-else class="save-button" @click="editMode = false">✔️</button>
      </div>
    </div>
    <div class="box right-box">
      <div class="content-container">
        <h3>Course Overview</h3>
        <div class="right-box-item" v-for="(item,index) in arr" :key="index">
          <div>{{item}}</div>
          <div class="arrow-right"> > </div>
        </div>
        <div class="btn">Add new lecture</div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      title: 'Medical 101',
      subtitle: 'Course Description',
      description: 'in this course, you will learn the foundations of medical sciences. We will cover topics such as anatomy, medical terminology, and clinical skills. This course is designed to provide you with a solid understanding of the medical field.',
      arr: ['Lecture 1','Lecture 2','Lecture 3'],
      editMode: false,
      imageSrc: require('@/assets/listview1.png')
    }
  },
  methods: {
    handleFileUpload(event) {
      const file = event.target.files[0];
      if (file) {
        this.imageSrc = URL.createObjectURL(file);
      }
    }
  }
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
    cursor: pointer;
  }
}

.content-container {
  padding: 20px;

  .description-text {
    margin: 0; 
    line-height: 25px;
    word-wrap: break-word;
  }

  .edit-button {
    background: none;
    border: none;
    font-size: 1.5rem;
    cursor: pointer;
    margin-left: auto;
  }

  .save-button {
    background: none;
    border: none;
    font-size: 1.5rem;
    cursor: pointer;
    margin-left: auto;
    color: green;
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