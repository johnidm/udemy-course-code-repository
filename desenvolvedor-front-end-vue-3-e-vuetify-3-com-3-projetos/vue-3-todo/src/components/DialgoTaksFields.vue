<template>
  <v-row justify="center">
    <v-dialog v-model="store.showDialogTaskFields" persistent max-height="400">
      <v-card>
        <v-card-title class="text-h5"> Edit </v-card-title>
        <v-card-text>
          <v-text-field
            v-model="props.task.title"
            clearable
            label="Title"
          ></v-text-field>
          <v-text-field
            v-model="props.task.description"
            clearable
            label="Description"
          ></v-text-field>
        </v-card-text>
        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn color="green-darken-1" variant="text" @click="store.toggle()">
            Close
          </v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
  </v-row>
</template>

<script setup>
import { useTaskStore } from "@/store/tasks";
const store = useTaskStore();

const props = defineProps({
  task: Object,
});
</script>
