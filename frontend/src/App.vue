<template>
  <div class="container">
    <h1 align="center">Upload logs</h1>
    <DragAndDropForm/>
  </div>
</template>

<script>
import DragAndDropForm from './components/DragAndDropForm.vue'

export default {
  name: 'App',
  components: {
    DragAndDropForm
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
