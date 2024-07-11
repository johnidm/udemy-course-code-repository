import { createApp } from 'vue';

import FriendContact from './components/FriendContact.vue'
import App from './App.vue';

var app = createApp(App)

app.component('friend-contact', FriendContact)

app.mount('#app');
