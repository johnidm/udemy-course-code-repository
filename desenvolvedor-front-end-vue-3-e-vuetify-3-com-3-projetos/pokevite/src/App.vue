<script setup>

</script>

<template>
  <header>
    Poke App
  </header>

  <nav>
    <router-link to="/">Home</router-link>
    <router-link to="/about">About</router-link>
    
    <router-link to="/composition">Composition</router-link>
    <router-link to="/counter">Counter</router-link>
    <router-link to="/hello-world">Hello World</router-link>
  
  </nav>

  <main>
    <router-view />
  </main>

  <footer>
    <p>
      Author: Johni Douglas Marangon
    </p>
    <p>
      {{ new Date().getFullYear() }}
    </p>
  </footer>
</template>

<style scoped>
footer {
  color: aqua;
}
</style>
