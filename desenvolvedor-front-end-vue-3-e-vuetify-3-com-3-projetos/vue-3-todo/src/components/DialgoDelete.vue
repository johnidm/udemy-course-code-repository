<template>
  <v-row justify="center">
    <v-dialog v-model="store.showDialogDelete" persistent max-height="400">
      <v-card>
        <v-card-title class="text-h5"> Delete </v-card-title>
        <v-card-text> </v-card-text>
        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn color="green-darken-1" variant="text" @click="store.toggleDelete()">
            Close
          </v-btn>
          <v-btn
            color="green-darken-1"
            variant="text"
            @click="store.deleteTask()"
          >
            Confirm
          </v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
  </v-row>
</template>

<script setup>
import { useTaskStore } from "@/store/tasks";
const store = useTaskStore();
</script>
