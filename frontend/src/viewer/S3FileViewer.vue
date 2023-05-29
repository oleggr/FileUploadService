<template> 

  <div id="drag-form" @dragover.prevent @drop.prevent>
    <div class="request_input">  
      <input
          class="request_input_field"
          type="text"
          id="drag-form-request-id"
          v-model="request_id"
          placeholder="Request ID"
          v-on:keyup.enter="searchRequest"
      />
    </div>
  </div>

  <table style="width:60%">
    <tr>
      <th style="cursor: pointer" v-on:click="sortByName">Filename</th>
      <th style="width:25%;cursor: pointer;" v-on:click="sortBySize">Size</th>
      <th style="width:25%">Created at</th>
<!--      <th style="width:25%" v-on:click="sortByDate">Created at</th>-->
    </tr>

    <tr v-for="(item, index) in items" v-bind:key="index">
      <td>
        <a style="text-decoration:none" :href="`https://files.mobius-it.ru/object/get?filename=${encodeURIComponent(item.name)}`"> {{ item.name }} </a>
      </td>
      <td class="td-center"> {{ item.size }} </td>
      <td class="td-center"> {{ item.created }} </td>
    </tr>
  </table>

</template>

<script>
import axios from 'axios';
export default {
  name: 'S3FileView',
  data: () => ({
    request_id: (new URL(window.location.href)).searchParams.get("request_id"),
    items: [],
    nameSortOrder: true,
    sizeSortOrder: true,
    dateSortOrder: true,
  }),
  mounted() {
      this.getFiles();
  },
  methods: {
    getFiles: function (){
      axios.get(
          'https://files.mobius-it.ru/object/list?request_id=' + this.request_id,
      ).then(response =>{
        this.items = response.data;
        console.log(response);
      })
      .catch((error) => {
        this.$toast.show("Failed while trying to get files list. " + error.request.response,{
          type: "error",
          dismissible: true,
          duration: false,
        });

        console.log(error);
      });
    },
    searchRequest: function (){
      window.location.href = 'https://files.mobius-it.ru/view?request_id=' + this.request_id;
    },
    sortByName: function (){
      if (this.nameSortOrder) {
        this.nameSortOrder = false;
        this.items = this.items.slice().sort(function(a, b){
          return (a.name > b.name) ? 1 : -1;
        });
      } else {
        this.nameSortOrder = true;
        this.items = this.items.slice().sort(function(a, b){
          return (a.name < b.name) ? 1 : -1;
        });
      }
    },
    sortBySize: function (){
      if (this.sizeSortOrder) {
        this.sizeSortOrder = false;
        this.items = this.items.slice().sort(function(a, b){
          return (parseFloat(a.size) > parseFloat(b.size)) ? 1 : -1;
        });
      } else {
        this.sizeSortOrder = true;
        this.items = this.items.slice().sort(function(a, b){
          return (parseFloat(a.size) < parseFloat(b.size)) ? 1 : -1;
        });
      }
    },
    // sortByDate: function (){
    //   if (this.dateSortOrder) {
    //     this.dateSortOrder = false;
    //     this.items = this.items.slice().sort(function(a, b){
    //       return (a.created > b.created) ? 1 : -1;
    //     });
    //   } else {
    //     this.dateSortOrder = true;
    //     this.items = this.items.slice().sort(function(a, b){
    //       return (a.created < b.created) ? 1 : -1;
    //     });
    //   }
    // },
    startDownloading: function (filename){
      this.$toast.show(`Download of ${filename} started`,{
        type: "success",
        dismissible: true,
        duration: 4000,
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

  td {
    height: 40px;
    font-size: 16px;
  }

  .td-center {
    text-align: center;
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
