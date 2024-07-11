<template>

<section>
    <h2>{{ friend }}</h2>
    <button @click="toggleInfo"> {{ toggle ? 'Hide' : 'Show' }} Details </button>
    <div v-if="toggle">
        <p>Phone: {{ phone }}</p>
        <p>Email: {{ email }}</p>
    </div>
</section>

</template>

<script>

export default {
    data() {
        return {
            friend: 'Max',
            phone: '12345',
            email: 'max@test.com',
            toggle: false,
        }
    },
    methods: {
        toggleInfo() {
            this.toggle = !this.toggle
        }
    }
}
</script>
