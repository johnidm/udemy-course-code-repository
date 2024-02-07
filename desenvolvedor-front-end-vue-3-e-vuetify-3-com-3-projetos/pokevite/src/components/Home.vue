<script setup>

import { onMounted, reactive, ref, computed } from 'vue';

import ListPokemon from '../components/ListPokemon.vue';
import CardPokemonSelected from '../components/CardPokemonSelected.vue';

let pokemons = reactive(ref([]));
let selected = ref({});
let search = ref('');
let loading = ref(false);

const cache = {};

const fetchData = async (url) => {
    return await fetch(url)
        .then(res => res.json())
        .then(res => res);
}

const filteredItems = computed(() => {
    if (pokemons.value && search.value) {
        return pokemons.value.filter(pokemon => {
            return pokemon.name.toLowerCase().includes(search.value);
        })
    }

    return pokemons.value;
})

const selectPoke = async (pokemon) => {
    try {
        loading.value = true;

        const url = pokemon.url;

        selected.value = cache[url];
        if (!selected.value) {
            selected.value = await fetchData(pokemon.url);
            cache[url] = selected.value;
        }
    }
    finally {
        loading.value = false;
    }
}

onMounted(() => {
    fetch("https://pokeapi.co/api/v2/pokemon/")
        .then((res => res.json()))
        .then((res => {
            pokemons.value = res.results;
        }))
})

</script>

<template>
    <section>
        <h1>Home Page</h1>

        <div>
            <label>Nome do Pokemon</label>
            <input v-model="search" type="text" name="search">
        </div>

        <div>
            <button>Pesquisar</button>
        </div>
        <div>
            <CardPokemonSelected :name="selected?.name" :height="selected?.height" :weight="selected?.weight"
                :loading="loading" />
        </div>

        <div>
            <ListPokemon v-for="(item, index) in filteredItems" @click="selectPoke(item)" :key="index" :url="item.url"
                :name="item.name" />
        </div>

    </section>
</template>

<style scoped></style>