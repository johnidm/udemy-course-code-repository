<template>
  <p>
    Ask a yes/no question:
    <input v-model="question" :disabled="loading" />
  </p>
  <p>{{ answer }}</p>


  <input ref="my-input">

  <Count :init-value="10" @show="showValue" />
  <Count init-value="20" />
  <Count :initValue="80" />

  <Count>
    <p>Something bad happened.</p>
  </Count>

</template>

<script setup>
import { ref, watch, useTemplateRef, onMounted } from 'vue'
import Count from './component/Count.vue'

const input = useTemplateRef('my-input')

const showValue = (value) => {
  alert(value)
}

onMounted(() => {
  input.value.focus()
})

const question = ref('')
const answer = ref('Questions usually contain a question mark. ;-)')
const loading = ref(false)

// watch works directly on a ref
watch(question, async (newQuestion, oldQuestion) => {
  console.log(newQuestion, oldQuestion)
  if (newQuestion.includes('?')) {
    loading.value = true
    answer.value = 'Thinking...'
    try {
      const res = await fetch('https://yesno.wtf/api')
      answer.value = (await res.json()).answer
    } catch (error) {
      answer.value = 'Error! Could not reach the API. ' + error
    } finally {
      loading.value = false
    }
  }
})
</script>

<style>

p {
  color: red;
}

</style>