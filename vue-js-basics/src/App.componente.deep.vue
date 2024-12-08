<template>
  <div>
    <h1>{{ message }}</h1>

    <h3> {{ countModel }}</h3>

    <Greeting greeting-message="hello Jon" num="dez" v-bind="post" @some-event="callback"
      v-model:btitle.capitalize="bookTitle" v-model="countModel" class="large" @click="callback">
      <template v-slot:header>
        <!-- content for the header slot -->
        <p>Header</p>
      </template>
      <!-- 
      <template #footer>
        <p>Here's some contact info</p>
      </template> -->

      <template v-slot:footer>
        <!-- content for the header slot -->
        <p>Footer</p>
      </template>
      <!-- <p>Esse é um paragrafo</p> -->
    </Greeting>

  </div>
</template>

<script setup>
import { ref } from 'vue'

const countModel = ref(9)

const bookTitle = ref("Self-defence")

const callback = (n) => {
  alert(n)
}

const message = ref('John')
const post = {
  id: 1,
  title: 'My Journey with Vue'
}
</script>

<style>
.large {
  font-size: xx-large;
}
</style>