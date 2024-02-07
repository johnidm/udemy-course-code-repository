import { createApp } from 'vue'
import 'simpledotcss/simple.min.css'
import 'animate.css';
import './style.css'
import App from './App.vue'
import router from './router'

createApp(App).use(router).mount('#app')
