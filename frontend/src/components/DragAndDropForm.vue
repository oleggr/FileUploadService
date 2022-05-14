<template> 

  <div id="drag-form" @dragover.prevent @drop.prevent>
    <div class="request_input">  
      <input class="request_input_field" type="text" id="drag-form-request-id" v-model="request_id" placeholder="Request ID"/>
    </div>

    <input id="drag-form-input" style="display:none" ref="file" type="file" multiple @change="uploadFile"/>
    <div
    @click="$refs.file.click()"
    @drop="dragFile"
    @dragover.prevent="dragover"
    @dragleave.prevent="dragleave"
    id="drag-field"
    >
      Drag & drop to upload
      <div>or browse</div>
      <div v-if="File.length">
        <ul v-for="(file, index) in File" :key="file" :index="index">
          <li>{{file.name}} <button v-on:click="()=>deleteHandler(index)" class="google-button-cross">X</button></li>
        </ul>
      </div>
    </div>
  </div>

  <button class="google-button" v-on:click="clickHandler">Send</button>

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

      let formData = new FormData();
      formData.append('request_id', this.request_id);
      for (let i=0; i < this.File.length; i++){
        axios.post('https://files.mobius-it.ru/upload?request_id=' + this.request_id,
          {
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

      this.request_id = ""
      this.File = []
    },
    deleteHandler: function (index){
      this.File=[...this.File].filter((x,i)=>i!=index)
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
    border: 3px dashed #25609c;
    border-radius: 10px;
    padding: 10px;
    width: 40vw;
    height: 400px;
  }

  #drag-field:hover {
    border: 3px solid #25609c;
    background-color: #deefff !important;
  }

  .drag-field-file-hover {
    background-color: #deefff !important;
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
    background: #25609c;
    border-radius: 4px;
    transform: scale(0);
    transition-property: transform,opacity;
  }

  .google-button:hover::before {
    opacity: .1;
    transform: scale(2);
  }

  .google-button-cross {
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

  .google-button-cross::before {
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
    background: #25609c;
    border-radius: 4px;
    transform: scale(0);
    transition-property: transform,opacity;
  }

  .google-button-cross:hover::before {
    opacity: .1;
    transform: scale(1);
  }

  .request_input {
    text-align: center;
    margin-left: auto;
    margin-right: auto;
  }

  .request_input_field {
    width: 40vw;
    text-align: center;
    font-size: 16px;
  }

  ul {
    padding-left: 0;
  }

  li {
   list-style-type: none;
   text-align: center;
  }
</style>
