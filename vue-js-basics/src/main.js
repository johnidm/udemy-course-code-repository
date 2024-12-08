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

app.mount('#app')
