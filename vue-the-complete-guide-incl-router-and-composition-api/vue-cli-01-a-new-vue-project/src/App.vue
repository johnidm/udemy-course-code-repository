<template>
    <section>
        <h2>My Friends</h2>
        <ul>
            <li v-for="friend in friends" :key="friend">{{ friend }}</li>
        </ul>

        <friend-contact></friend-contact>

    </section>


</template>

<script>

export default {
    data() {
        return {
            friends: ['Max', 'Manuel', 'Julie', 'Julien']
        }
    }
}

</script>


<style>

* {
    box-sizing: border-box;
    font-family: Arial, sans-serif;
}

</style>

