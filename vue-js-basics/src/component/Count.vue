<script setup>
import { ref } from 'vue'
// const props = defineProps(['initValue'])
const props = defineProps([{ 
  initValue: Number,
}])
const emit = defineEmits(['show'])

const count = ref(props.initValue || 0)
emit('show', count.value)

</script>

<template>
  <button @click="count++">You clicked me {{ count }} times.</button>
  <button @click="$emit('show', count)">Show</button>
  <slot />
</template>
