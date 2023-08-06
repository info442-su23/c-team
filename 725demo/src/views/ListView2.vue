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
        <label class="btn">
          <input 
            type="file" 
            accept=".mp4,.mkv,.avi,.flv,.mov,.wmv,.mp3,.mp4a,.m4p,.raw,.wav,.pdf,.docx,.rtf,.txt" 
            style="display: none" 
            @change="handleMaterialUpload"
          />
          {{ selectedFileName || 'Upload new material' }}
        </label>
        <button v-if="selectedFileName" class="btn" @click="submitFile">Submit</button>
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
      selectedFileName: null,
      selectedFile: null, // To store the selected file
      csrfToken: null // To store the CSRF token
    }
  },
  async created() {
    try {
      const baseUrl = process.env.VUE_APP_FILEUPLOAD_URL;
      const response = await fetch(baseUrl + '/csrf-token', {
        method: 'GET',
      });
      const data = await response.json();
      console.log(data.token)
      this.csrfToken = data.token;
    } catch (error) {
      console.error('Error fetching CSRF token:', error);
    }
  },
  methods: {
    handleFileUpload(event) {
      const file = event.target.files[0];
      if (file) {
        this.imageSrc = URL.createObjectURL(file);
      }
    },
    handleMaterialUpload(event) {
      const file = event.target.files[0];
      if (file) {
        this.selectedFileName = file.name;
        this.selectedFile = file;
      }
    },
    async submitFile() {
      const baseUrl = process.env.VUE_APP_FILEUPLOAD_URL;
      let endpoint = '';

      if (this.selectedFileName) {
        const extension = this.selectedFileName.split('.').pop().toLowerCase();
        if (['mp4', 'mkv', 'avi', 'flv', 'mov', 'wmv'].includes(extension)) {
          endpoint = '/upload-video';
        } else if (['mp3', 'mp4a', 'm4p', 'raw', 'wav'].includes(extension)) {
          endpoint = '/upload-audio';
        } else if (['pdf', 'docx', 'rtf', 'txt'].includes(extension)) {
          endpoint = '/upload-text';
        } else {
          alert('Invalid file type');
          return;
        }

        const formData = new FormData();
        formData.append('file', this.selectedFile);
        formData.append('csrf_token', this.csrfToken);  // Add this line

        try {
          console.log(this.csrfToken)
          const response = await fetch(baseUrl + endpoint, {
            method: 'POST',
            headers: {
              'X-CSRF-TOKEN': this.csrfToken
            },
            body: formData,
          });
          const text = await response.text();
          console.log(text);
          alert('File uploaded successfully');
        } catch (error) {
          console.error('Error:', error);
          alert('An error occurred while uploading the file' + error.toString());
        }
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
</style>