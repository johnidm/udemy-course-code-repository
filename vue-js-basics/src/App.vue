<script setup>
import { ref, inject, getCurrentInstance, version, useTemplateRef } from 'vue'
const greeting = ref('Hello World!')

console.log(inject('message')) // 'hello'
const app = getCurrentInstance()
console.log("Global Property", app.appContext.config.globalProperties.prefix) // 'hello'
console.log(version)

const pRef = useTemplateRef('pRef')
console.log(pRef)

</script>

<template>
  <p ref="pRef">{{ greeting }}</p>
  <p class="greeting">{{ greeting }}</p>
</template>

<style>
.greeting {
  color: red;
  font-weight: bold;
}
</style>