<template>
  <div class="alert-notification ">
    <v-alert
      closable
      icon="$vuetify"
      title="Alert title"
      text="Taks created success."
      type="success"
    ></v-alert>
  </div>
</template>


<style scoped>
.alert-notification {
  position: fixed;
  z-index: 1;
  bottom: 50px;
  width: 100%;
  padding: 0 30%;
}
</style>