<script setup>

import { ref, onMounted, computed } from 'vue'

let temperatura = ref(0);

onMounted(() => {
    temperatura.value = 10
});

const checkTemp = computed(() => {
    return temperatura.value > 21 ? 'Temperatura Alta' : 'Temperatura Baixa'
})

</script>

<template>
    <h1>{{ temperatura }} graus</h1>

    <label for="tentacles">Temperatura (0-100):</label>
    <input type="number" id="tentacles" name="tentacles" min="0" max="100" v-model="temperatura" />

    <p>{{ checkTemp }}</p>
</template>


<style>

h1 {
    color: red;
}
</style>