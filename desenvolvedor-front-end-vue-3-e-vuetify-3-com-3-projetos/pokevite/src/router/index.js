import { createRouter, createWebHistory } from 'vue-router'

import HelloWorld from '../components/HelloWorld.vue'
import Composition from '../components/Composition.vue'
import Counter from '../components/Counter.vue'
import Home from '../components/Home.vue'

const routes = [
    {
        path: '/',
        name: 'home',
        component: Home
    },
    // {
    //     path: '/about',
    //     name: 'about',
    //     component: About
    // },
    {
        path: '/counter',
        name: 'counter',
        component: Counter
    },
    {
        path: '/composition',
        name: 'composition',
        component: Composition
    },
    {
        path: '/hello-world',
        name: 'hello-world',
        component: HelloWorld
    },

]

const router = createRouter({
    history: createWebHistory(),
    routes
})

export default router