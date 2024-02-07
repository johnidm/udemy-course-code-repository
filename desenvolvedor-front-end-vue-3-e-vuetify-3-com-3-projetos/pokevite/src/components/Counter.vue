<script setup>
import { ref } from 'vue'

let counter = ref(0);

</script>

<template>
    <h1>Counter Page</h1>
    <div>
        <button @click="counter++">Increase counter</button>
        <p>{{ counter }}</p>
    </div>
</template>

<style scoped>
button {
    color: blue;
}

p {
    color: brown;
}
</style>