<template>
  <div class="container">
    <h1 align="center">View files</h1>
    <S3FileViewer/>
  </div>
</template>

<script>
import S3FileViewer from './S3FileViewer.vue'

export default {
  name: 'App',
  components: {
    S3FileViewer
  }
}
</script>

<style>
#app {
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  color: #2c3e50;
  margin-top: 30px;
  width: 100vw;
}

* {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  padding: 0;
  margin: 0;
}

.container {
  display: flex;
  justify-content: center;
  align-items: center;
  gap: 15px;
  width: 100vw;
  flex-direction: column;
}

</style>
