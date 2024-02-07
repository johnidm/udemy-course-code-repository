<script setup>

const pokemon = defineProps(["name", "url"])

const buildImageUrl = (url) => {
    const { pathname } = new URL(url);
    const pathnames = pathname.split('/').filter(Boolean)
    const id = pathnames[pathnames.length -1];

    return `https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/dream-world/${id}.svg`
}
</script>

<template>
    <article class="card">
        <h3>{{ pokemon.name }}</h3>
        <img :alt="pokemon.name" :src="buildImageUrl(pokemon.url)" width="120px" height="120px" />   
    </article>

</template>


<style scoped>

.card {
    background: #92FE9D;
    background: linear-gradient(90deg, #92FE9D 0%, #00C9FF 100%);
    cursor: pointer;
}

</style>

