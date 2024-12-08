<script setup>
import { ref } from 'vue'
import { useFetch } from './fetch.js'

const url = ref('https://peps.python.org/api/peps.json')
const { data, error } = useFetch(url)

const search = ref('')
const fetchData = () => {
  url.value = `https://peps.python.org/api/search/?q=${search.value}`
}

</script>

<template>
  <h1>PEP Index</h1>

  <input v-model="search" placeholder="Search..." />
  <button @click="fetchData">Fetch Data</button>


  <div v-if="error">Oops! Error encountered: {{ error.message }}</div>
  <div v-else-if="data">
    Data loaded:
    <pre>{{ data }}</pre>
  </div>
  <div v-else>Loading...</div>
</template>