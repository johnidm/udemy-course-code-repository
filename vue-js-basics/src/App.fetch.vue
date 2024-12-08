<template>
  <div class="app">
    <h1>Python PEPs List</h1>
    <div v-if="loading" class="loading">
      Loading PEPs...
    </div>
    <div v-else-if="error" class="error">
      {{ error }}
    </div>
    <div v-else class="peps-list">
      <div v-for="(pep, number) in peps" :key="number" class="pep-item">
        <h3>PEP {{ number }}</h3>
        <p><strong>Title:</strong> {{ pep.title }}</p>
        <p><strong>Status:</strong> {{ pep.status }}</p>
        <p><strong>Type:</strong> {{ pep.type }}</p>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'

const peps = ref({})
const loading = ref(true)
const error = ref(null)

const fetchPeps = async () => {
  try {
    const response = await fetch('https://peps.python.org/api/peps.json')
    if (!response.ok) {
      throw new Error('Failed to fetch PEPs data')
    }
    const data = await response.json()
    peps.value = data
  } catch (e) {
    error.value = e.message
  } finally {
    loading.value = false
  }
}

onMounted(() => {
  fetchPeps()
})
</script>

<style scoped>
.app {
  max-width: 1200px;
  margin: 0 auto;
  padding: 20px;
}

.loading, .error {
  text-align: center;
  margin: 20px;
  font-size: 1.2em;
}

.error {
  color: red;
}

.peps-list {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
  gap: 20px;
}

.pep-item {
  border: 1px solid #ddd;
  border-radius: 8px;
  padding: 15px;
  background-color: #f9f9f9;
}

.pep-item h3 {
  margin-top: 0;
  color: #2c3e50;
}
</style> 