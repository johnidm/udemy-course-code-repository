<script setup>

const props = defineProps({
    name: {
        type: String,
        default: "withou name"
    },
    weight: {
        type: Number,
        default: 0
    },
    height: {
        type: Number,
        default: 0
    },
    loading: {
        type: Boolean,
        default: false
    }
});

</script>

<template>
    <article :class="props?.loading ? '' : 'animate__animated animate__flipInY'">
        <h4> {{ props?.name }}</h4>

        <h6>Altura: {{ props?.height }}</h6>
        <h6>XP: {{ props?.weight }}</h6>
    </article>
</template>

<style scoped></style>

