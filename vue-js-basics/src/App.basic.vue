<template>
  <div>
    <div class="static" :class="{ active: !isDisabled, 'error': hasError }">
      <h1>{{ message }}</h1>
    </div>

    <div :style="styleObject">

      Click ME
    </div>


    <div v-if="type === 'A'">
      A
    </div>
    <div v-else-if="type === 'B'">
      B
    </div>
    <div v-else-if="type === 'C'">
      C
    </div>
    <div v-else>
      Not A/B/C
    </div>

    <button @click="awesome = !awesome">Toggle</button>

    <h1 v-if="awesome">Vue is awesome!</h1>
    <h1 v-else>Oh no 😢</h1>

    <p :class="[isActive ? 'active' : 'deactive',]">Bom dia

    </p>

    <p>{{ span }}</p>
    <p v-html="span"></p>

    <div v-bind:id="id">
      <p>This is a paragraph with an {{ id }}.</p>
    </div>

    <div :id="id">
      <p>This is a paragraph with an {{ id }}.</p>
    </div>

    <div :data-uuid="id">
      <p>This is a paragraph with an {{ id }}.</p>
    </div>
    <div v-bind:data-uuid="id">
      <p>This is a paragraph with an {{ id }}.</p>
    </div>

    <button :disabled="isDisabled">Click me</button>

    <button v-bind="buttonAttr" @click="message = 'Hello World!'">My Button</button>

    <p v-bind:title="getTitle('date')"></p>

    <p v-if="seen">Now you see me</p>

    <a v-bind:href="url"> LINK </a>

    <button v-on:click="doSomething">Do Something </button>


    <h2>Task</h2>
    <h5>{{ task.name }}</h5>
    <p v-for="item in task.items">{{ item }}</p>

    <p> Total Items: {{ totalItems }} </p>
    <button @click="addItem('Take a nap')">Add</button>

  </div>

  <template v-if="ok">
    <h1>Title</h1>
    <p>Paragraph 1</p>
    <p>Paragraph 2</p>
  </template>

  <h1 v-show="ok">Hello!</h1>
</template>

<script setup>
import { ref, reactive, computed } from 'vue'

const ok = ref(true)
const awesome = ref(true)

const type = ref('A')

function  addItem(itemName) {
  task.items.push(itemName)
}


const totalItems = computed(() => {
  return task.items.length
})



const task = reactive({
  name: "Daily Routine",
  items: [
    "wake up at 6 a.m",
    "take a shower",
    "have a breakfast",
  ]
})


function getTitle(prefix) {
  return `MyTitle-${prefix}`
}

function  doSomething() {
  alert("I am doing something")
}

const url = "https://google.com"

const message = ref('John Doe!')

console.log(message.value)


const span = '<span style="color: red">This should be red.</span>'

const id = crypto.randomUUID()

const isDisabled = ref(false)
const hasError = ref(true)

const isActive = ref(false)

const styleObject = reactive({
  color: 'green',
  fontSize: '30px'
})

const buttonAttr = {
  id: "id-1",
  class: "wrapper",
  style: 'background-color:green',
  dataRule: 'ref345',
}

</script>

<style>
h1 {
  color: red;
  font-family: 'Courier New', Courier, monospace;
}

div.active {
  border: 6px dotted;
}

div.error {
  border-color: red;
}

div.static {
  background-color: aqua;
}

p.active {
  color: blueviolet;
}

p.deactive {
  text-decoration: overline;
}
</style>
