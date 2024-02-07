<script setup>

import { ref, onMounted, computed } from 'vue'

let temperatura = ref(0);

const showSpan = false;


const nums = [
    1, 2, 3, 4, 5, 6
]

onMounted(() => {
    temperatura.value = 10
});

const checkTemp = computed(() => {
    return temperatura.value > 21 ? 'Temperatura Alta' : 'Temperatura Baixa'
})

</script>

<template>
    <h1>Composition Page</h1>
    <h4>{{ temperatura }} graus</h4>

    <label for="tentacles">Temperatura (0-100):</label>
    <input type="number" id="tentacles" name="tentacles" min="0" max="100" v-model="temperatura" />

    <p>{{ checkTemp }}</p>

    <span v-if="showSpan">Hi, I am being shown</span>
    <span v-else>Hi, I am being hidden</span>

    <ul>
        <li v-for="num, index in nums" key="index">
            {{ num }}
        </li>
    </ul>


</template>


<style>

h1 {
    color: red;
}
</style>