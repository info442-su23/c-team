<template>
  <div class="container">
    <div class="box left-box">
      <div class="image-container">
        <input type="file" accept="image/*" @change="handleFileUpload" ref="fileInput" style="display: none" />
        <img :src="imageSrc" alt="" @click="editMode && $refs.fileInput.click()" />
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

        <div class="right-box-item">
          <button class="material-button" :disabled="!materialsUploaded">Lecture Handout</button>
          <div class="arrow-right"> > </div>
        </div>
      </div>
    </div>
    <div class="box right-box">
      <div class="content-container">
        <h3>Lecture Materials</h3>
        <div class="right-box-item" v-for="(item, index) in arr" :key="index">
          <button class="material-button" :disabled="!materialsUploaded">{{ item }}</button>
          <div class="arrow-right"> > </div>
        </div>
        <div class="btn" @click="openDialog">Upload new material</div>
        <input type="file" id="upload" value="" name="saveFile" multiple style="display: none;"
          @change="tirggerFile($event)" />
      </div>
    </div>
    <div v-show="dialogVisible" class="modal">
      <div class="header">
        <span>Uploading {{ fileArr.length }} item</span>
        <i class="el-icon-close" @click="dialogVisible = false"></i>
      </div>
      <div class="process">
        <span>Finishing upload...</span>
        <span style="cursor: pointer;color:royalblue" @click="handleCancel">Cancel</span>
      </div>
      <div class="items">
        <div v-for="(item, index) in fileArr" :key="index" class="upload-item">
          <span>
            <i class="el-icon-picture"></i>
            <span class="file-name">{{ item.name }}</span>
          </span>
          <i class="el-icon-loading"></i>
        </div>
      </div>

    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      title: 'Lecturel',
      subtitle: 'Full Lecture Transcript',
      description: 'Lorem ipsum dolor sit amet...',
      arr: ['Lecture Summary', 'Handout Summary', 'Study Cards'],
      materialsUploaded: false,
      editMode: false,
      imageSrc: require('@/assets/listview2.png'),
      dialogVisible: false,
      fileArr: [{ name: '16898432.png' }, { name: '903242232.jpg' }]
    }
  },
  methods: {
    handleFileUpload(event) {
      const file = event.target.files[0];
      if (file) {
        this.imageSrc = URL.createObjectURL(file);
      }
    },
    openDialog() {
      document.getElementById('upload').click()
    },
    tirggerFile(event) {
      this.fileArr = event.target.files
      if (this.fileArr.length) {
        this.dialogVisible = true
      }
    },
    handleCancel() {
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
  position: relative;
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

.material-button {
  background: none;
  border: none;
  padding: 0;
  font: inherit;
  cursor: pointer;
  outline: inherit;
}

.material-button:disabled {
  cursor: not-allowed;
  color: #ccc;
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

.modal {
  position: absolute;
  right: 10px;
  bottom: 10px;
  border: 1px solid #476b9a;
  width: 350px;
  min-height: 250px;
  border-radius: 15px;

  .header {
    display: flex;
    justify-content: space-between;
    padding: 15px;
    font-size: 16px;
    font-weight: bold;
  }

  .process {
    display: flex;
    justify-content: space-between;
    margin: 10px 0;
    background: #f0f2fe;
    padding: 8px 15px;
  }

  .items {
    margin-top: 10px;

    .file-name {
      width: 200px;
      white-space: nowrap;
      text-overflow: ellipsis;
      overflow: hidden;
      display: inline-block;
      text-align: left;
      padding-left: 5px;
      vertical-align: middle;
    }

    .upload-item {
      display: flex;
      justify-content: space-between;
      padding: 8px 15px;
    }

  }
}
</style>