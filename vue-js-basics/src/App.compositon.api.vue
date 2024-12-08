<template>
  <button @click="increment">Click me</button>
  <p>{{ count }}</p>
</template>

<script setup>
import { ref } from 'vue';

const count = ref(0);

function increment() {
  count.value++;
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
