<template>
  <div>
    <h1>Hi</h1>
    <ul>
      <li v-for="({ message, order }, index) in items" :key="index">
        {{ message }} - {{ order }} - {{ index }}
      </li>
    </ul>


    <ul>
      <li v-for="value, key in person" :key="key">
        {{ key }} - {{ value }}
      </li>
    </ul>

    <template v-for="todo in todos" :key="todo.name">

      <p v-if="!todo.isComplete">
        {{ todo.name }}
      </p>

    </template>

    <button @click="count++">Add 1</button>
    <p>Count is: {{ count }}</p>
  </div>

  <button @click="greet">Greet</button>

  <button @click="say('hello')">Say hello</button>
  <button @click="say('bye')">Say bye</button>

  <button @click="warn('Form cannot be submitted yet.', $event)">Submit</button>

  <input @keyup.alt.enter="clear" />

  <p>Message is: {{ message }}</p>
  <input v-model="message" placeholder="edit me" />

  <textarea v-model="text"></textarea>
  <p style="white-space: pre-line;">{{ text }}</p>

  <div>Checked names: {{ checkedNames }}</div>

  <input type="checkbox" id="jack" value="Jack" v-model="checkedNames" />
  <label for="jack">Jack</label>

  <input type="checkbox" id="john" value="John" v-model="checkedNames" />
  <label for="john">John</label>

  <input type="checkbox" id="mike" value="Mike" v-model="checkedNames" />
  <label for="mike">Mike</label>

  <input type="checkbox" id="checkbox" v-model="checked" />
  <label for="checkbox">{{ checked }}</label>

  <div>Picked: {{ picked }}</div>

  <input type="radio" id="one" value="One" v-model="picked" />
  <label for="one">One</label>

  <input type="radio" id="two" value="Two" v-model="picked" />
  <label for="two">Two</label>

  <div>Selected: {{ selected }}</div>

  <select v-model="selected">
    <option disabled value="">Please select one</option>
    <option>A</option>
    <option>B</option>
    <option>C</option>
  </select>

  <select v-model="selectedList">
    <option v-for="option in optionsList" :value="option.value">
      {{ option.text }}
    </option>
  </select>

  <div>Selected: {{ selectedList }}</div>

  <select v-model="selectedObject">
    <!-- inline object literal -->
    <option :value="{ number: 123 }">123</option>
    <option :value="{ number: 456 }">456</option>
  </select>

  <div>Selected: {{ selectedObject }}</div>

</template>

<script setup>
import { ref } from 'vue'

const picked = ref('One')

const selectedObject = ref({})
const selectedList = ref('A')

const optionsList = ref([
  { text: 'One', value: 'A' },
  { text: 'Two', value: 'B' },
  { text: 'Three', value: 'C' }
])

const selected = ref('')
const checked = ref(false)
const checkedNames = ref([])
const text = ref('')
const message = ref('Hello Vue!')

const clear = (event) => {
  console.log('clear')
}

const warn = (message, event) => {
  // now we have access to the native event
  if (event) {
    event.preventDefault()
  }
  alert(message)
}

const count = ref(0)

const name = ref('Vue.js')

const say = (message) => {
  alert(message)
}

const greet = (event) => {
  alert(`Hello ${name.value}!`)
  // `event` is the native DOM event
  if (event) {
    alert(event.target.tagName)
  }
}

const items = ref([{ message: 'Foo', order: 1 }, { message: 'Bar', order: 2 }])

const person = ref({ name: 'John', age: 30 })

const todos = ref([{ name: 'Buy milk', isComplete: false }, { name: 'Buy bread', isComplete: true }])

</script>

<style scoped></style>