// Utilities
import { defineStore } from "pinia";

export const useAlertStore = defineStore("alert", {
  state: () => ({
    showAlert: false,
  }),

  actions: {
    modifyAlert() {
      this.showAlert = true;
      setTimeout(() => {
        this.showAlert = false;
      }, 1000);
    },
  },
});
