<template> 

  <div id="drag-form" @dragover.prevent @drop.prevent>
    <div class="request_input">  
      <input class="request_input_field" type="text" id="drag-form-request-id" v-model="request_id" placeholder="Request ID" readonly/>
    </div>
  </div>

  <li v-for="(item, index) in items" v-bind:key="index">
    <a style="text-decoration:none" :href="`http://127.0.0.1:8000/object/get?request_id=${request_id}&filename=${item}`"> {{ item }} </a>
  </li>
</template>

<script>
import axios from 'axios';
export default {
  name: 'S3FileView',
  data: () => ({
    request_id: (new URL(window.location.href)).searchParams.get("request_id"),
    items: [],
  }),
  mounted() {
      this.getFiles();
  },
  methods: {
    getFiles: function (){
      axios.get(
          'http://127.0.0.1:8000/objects/list?request_id=' + this.request_id,
      ).then(response =>{
        this.items = response.data;
        console.log(response);
      })
      .catch((error) => {
        this.$toast.show("Failed while trying to get files list: " + error.request.response,{
          type: "error",
          dismissible: true,
          duration: false,
        });

        console.log(error);
      });
    },
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
