<template>
  
  <v-app id="inspire">
    
    <v-navigation-drawer v-model="drawer">
      <v-list>
        <v-list-item
          prepend-avatar="https://cdn.vuetifyjs.com/images/john.png"
          title="John Leider"
          subtitle="john@google.com"
        >
          <template v-slot:append>
            <v-btn size="small" variant="text" icon="mdi-menu-down"></v-btn>
          </template>
        </v-list-item>
      </v-list>

      <v-divider></v-divider>

      <router-link v-for="(item, i) in items" :key="i" :to="item.to">
        <v-list :lines="false" density="compact" nav>
          <v-list-item :value="item" color="primary">
            <template v-slot:prepend>
              <v-icon :icon="item.icon"></v-icon>
            </template>

            <v-list-item-title :textContent="item.text"></v-list-item-title>
          </v-list-item>
        </v-list>
      </router-link>
    </v-navigation-drawer>

    <v-app-bar>
      <v-app-bar-nav-icon @click="drawer = !drawer"></v-app-bar-nav-icon>

      <v-app-bar-title>To Do List</v-app-bar-title>
    </v-app-bar>

    <v-main>
        <Alert v-if="store.showAlert" />
      <router-view />
    </v-main>
  </v-app>
</template>

<script setup>
import { ref } from "vue";

import { useAlertStore } from "@/store/alert"

const store = useAlertStore();


const drawer = ref(null);

const items = [
  { text: "Home", icon: "mdi-folder", to: "/" },
  { text: "About", icon: "mdi-account-multiple", to: "/about" },
];
</script>

<style scoped>
a {
  text-decoration: none;
  color: #505050;
}
</style>