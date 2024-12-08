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
  background-color: blue;
  color: white;
  padding: 10px 20px;
  border: none;
  border-radius: 5px;
}
</style>
