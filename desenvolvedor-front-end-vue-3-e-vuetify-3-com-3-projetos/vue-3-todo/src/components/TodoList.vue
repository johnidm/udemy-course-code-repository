<template>
  <v-text-field
    clearable
    label="Add Task"
    :rules="rules"
    v-model="store.titleTaskCreateing"
    @keyup.enter="store.addTask"
  ></v-text-field>

  <ListTasks />
</template>

<script setup>
import { useTaskStore } from "@/store/tasks"

const store = useTaskStore();


const rules = [

  value => {
    if (value.length > 5) return true;

    return "Campo com tamanho mínimo de 5 caracteres"
  }
]
</script>