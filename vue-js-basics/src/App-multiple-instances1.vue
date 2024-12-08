<template>
  <button @click="increment">Click me</button>
  <p>{{ count }}</p>
</template>

<script>

export default {
  data() {
    return { count: 0 };
  },
  methods: {
    increment() {
      this.count++;
    }
  }
}

</script>

<style scoped>
button {
  background-color: red;
  color: white;
  padding: 10px 20px;
  border: none;
  border-radius: 5px;
}
</style>


<!-- 
main.js

import App1 from './App-multiple-instances1.vue'
import App2 from './App-multiple-instances2.vue'

createApp(App1).mount('#app-1') 
createApp(App2).mount('#app-2') 


index.html

<div id="app-1"></div>
<div id="app-2"></div>

-->


