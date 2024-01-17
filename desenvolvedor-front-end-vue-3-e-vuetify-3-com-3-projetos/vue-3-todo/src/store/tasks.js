import { defineStore } from "pinia";

import { useAlertStore } from "@/store/alert"

const alertStore = useAlertStore();

export const useTaskStore = defineStore("task", {
  state: () => ({
    tasks: [
      {
        title: "Estudar Vue",
        description: "Estudar Vue com vuetify",
      },
      {
        title: "ler um Livro",
        description: "Ler 10 páginas por dia",
      },
      {
        title: "Criar um site",
        description: "",
      },
    ],
    titleTaskCreateing: "",
    showDialogTaskFields: false,
    showDialogDelete: false,
    indexTaskSelected: 0,
  }),
  actions: {
    addTask() {
      this.tasks.push({
        title: this.titleTaskCreateing,
      });
      this.titleTaskCreateing = "";
      this.saveLocalData();
      alertStore.modifyAlert();
    },
    toggle(index) {
      this.showDialogTaskFields = !this.showDialogTaskFields;
      if (index != null) {
        this.indexTaskSelected = index;
      };
      this.saveLocalData();
    },
    toggleDelete(index) {
      this.showDialogDelete = !this.showDialogDelete;
      if (index != null) {
        this.indexTaskSelected = index;
      }
    },
    deleteTask() {
      this.tasks.splice(this.indexTaskSelected, 1);
      this.toggleDelete();
      this.saveLocalData();
    },
    saveLocalData() {
      localStorage.setItem("tasks", JSON.stringify(this.tasks));
    },
    getTasks() {
      let items = localStorage.getItem("tasks");
      if (items) {
        this.tasks = JSON.parse(items);
      }
    }
  },
});
