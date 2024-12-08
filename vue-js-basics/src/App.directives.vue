<template>
  <div>
    <h1>{{ message }}</h1>
  </div>
  <p v-highlight>This sentence is important!</p>
  <input v-focus />
  <input />
  <input />

  <div v-color="color">HI</div>

</template>

<script setup>

const message = 'Hello World :-!'

const vHighlight = {
  mounted: (el) => {
    el.classList.add('is-highlight')
  }
}

const vFocus = {
  mounted: (el) => el.focus()
}

const vColor = {
  mounted: (el, binding) => {
    el.style.color = binding.value
  }
}

</script>

<style scoped>

.is-highlight {
  background-color: yellow;
}
</style> 
