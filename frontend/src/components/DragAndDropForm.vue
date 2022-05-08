<template> 

  <div id="drag-form" @dragover.prevent @drop.prevent>

    <label for="request_id">Request ID: </label>
    <input type="text" id="drag-form-request-id" v-model="request_id"/>
   

    <input id="drag-form-input" style="display:none" type="file" multiple @change="uploadFile"/>
    <div
    @drop="dragFile"
    @dragover.prevent="dragover"
    @dragleave.prevent="dragleave"
    id="drag-field"
    >
      Drag & drop to upload
      <div>or browse</div>
      <div v-if="File.length">
        <ul v-for="file in File" :key="file">
          <li>{{file.name}}</li>
        </ul>
      </div>
    </div>
  </div>

  <button class="google-button" v-on:click="clickHandler">Send</button>
  
  <p>{{ request_id }}</p>

</template>

<script>
import axios from 'axios';
export default {
  name: 'DragAndDropForm',
  data: () => ({
    File: [],
    request_id: String()
  }),
  methods: {
    uploadFile(e) {
      this.File = e.target.files;
    },
    dragFile(e) {
      this.File = e.dataTransfer.files;
      e.currentTarget.classList.remove("drag-field-file-hover")
    },
    dragover(e){
      e.currentTarget.classList.add("drag-field-file-hover")
    },
    dragleave(e){
      e.currentTarget.classList.remove("drag-field-file-hover")
    },
    clickHandler: function (e){
      console.log(e)
      console.log(this)
      console.log("-------")
      console.log([...this.File])
      
      let formData = new FormData();
      formData.append('request_id', this.request_id);
      for (let i=0; i < this.File.length; i++){
        axios.post('http://127.0.0.1:8000/upload', 
          {
            'request_id': this.request_id,
            'file': this.File[i]
          },
          {
            headers: {
              'Content-Type': 'multipart/form-data'
            }
          }
        ).then(response =>{
          console.log(response);
        });
      }
    }
  }
}
</script>

<style scoped>
  #drag-form-request-id{
    padding: 5px;
    margin-bottom: 10px;
    border-radius: 5px;
    border: 1px solid #000;
  }
  #drag-form {
  }

  #drag-field {
    display: flex;
    justify-content: center;
    align-items: center;
    flex-direction: column;
    background-color: #fff;
    border: 3px dashed palevioletred;
    border-radius: 10px;
    padding: 10px;
    width: 40vw;
    height: 400px;
  }

  #drag-field:hover {
    border: 3px solid palevioletred;
  }

  .drag-field-file-hover {
    background-color: #000 !important;
  }

  .google-button {
    align-items: center;
    border: none;
    display: inline-flex;
    justify-content: center;
    outline: none;
    position: relative;
    z-index: 0;
    -webkit-font-smoothing: antialiased;
    background: none;
    border-radius: 4px;
    cursor: pointer;
    padding: 0 8px;
    white-space: pre-wrap;
    font-size : 20px; width: 5%;
  }

  .google-button::before {
    content: '';
    display: block;
    opacity: 0;
    position: absolute;
    transition-duration: .15s;
    transition-timing-function: cubic-bezier(0.4,0.0,0.2,1);
    z-index: -1;
    bottom: 0;
    left: 0;
    right: 0;
    top: 0;
    background: #4285f4;
    border-radius: 4px;
    transform: scale(0);
    transition-property: transform,opacity;
  }

  .google-button:hover::before {
    opacity: .06;
    transform: scale(2);
  }
</style>
