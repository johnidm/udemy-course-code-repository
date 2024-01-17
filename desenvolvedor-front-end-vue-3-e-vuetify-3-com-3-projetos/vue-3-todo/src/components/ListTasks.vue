<template>
  <v-card class="mx-auto">
    <v-list lines="three" select-strategy="classic">
      <v-list-subheader>General</v-list-subheader>

      <v-list-item
        v-for="(task, index) in store.tasks"
        :key="index"
        :value="index"
      >
        <template v-slot:prepend="{ isActive }">
          <v-list-item-action start>
            <v-checkbox-btn :model-value="isActive"></v-checkbox-btn>
          </v-list-item-action>
        </template>

        <v-list-item-title>{{ task.title }}</v-list-item-title>

        <v-list-item-subtitle>
          {{ task.description }}
        </v-list-item-subtitle>

        <template v-slot:append>
          <v-menu>
            <template v-slot:activator="{ props }">
              <v-btn color="primary" v-bind="props">...</v-btn>
            </template>
            <v-list>
              <v-list-item @click="store.toggle(index)">
                <v-list-item-title>Editar</v-list-item-title>
              </v-list-item>
              <v-list-item @click="store.toggleDelete(index)">
                <v-list-item-title>Excluir</v-list-item-title>
              </v-list-item>
            </v-list>
          </v-menu>
        </template>
      </v-list-item>
    </v-list>
  </v-card>

  <DialgoTaksFields :task="store.tasks[store.indexTaskSelected]" />

  <DialgoDelete />
</template>

<script setup>

import { onMounted } from  "vue";
import { useTaskStore } from "@/store/tasks";
const store = useTaskStore();


onMounted(() => {
  store.getTasks();
})
</script>
