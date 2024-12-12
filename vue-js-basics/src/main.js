import { createApp } from 'vue'
import App from './App.vue'

import Greeting from './component/Greeting.vue'

const app = createApp(App)

app.component("Greeting", Greeting)

// app.directive('color', (el, binding) => {
//     // this will be called for both `mounted` and `updated`
//     // console.log(binding.value)
//     // el.style.color = binding.value
// })

app.provide('message', 'Morning')

console.log(app.config)

app.config.errorHandler = (err, instance, info) => {
    console.log(" Error ", err, instance, info)
  }

app.config.globalProperties.prefix = 'HE'


app.mount('#app')
