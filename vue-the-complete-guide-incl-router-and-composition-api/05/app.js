const app = Vue.createApp({
    data() {
        return {
            message: 'Hello World'
        }
    },
    methods: {
        // handleInput(e) {
        //     this.message = e.target.value
        // },
        handleClick() {
            console.log(this.$refs)
            this.message = this.$refs.userInput.value

        }
    },
    beforeCreate() {
        console.log('beforeCreate')
    },
    created() {
        console.log('created')
    },
    beforeMount() {
        console.log('beforeMount')
    },
    mounted() {
        console.log('mounted')
    },
    beforeUpdate() {
        console.log('beforeUpdate')
    },
    updated() {
        console.log('updated')
    },
    beforeUnmount() {
        console.log('beforeUnmount')
    },
    unmounted() {
        console.log('unmounted')
    }
})

app.mount('#app')


const app2 = Vue.createApp({
    data() {
        return {
            message: 'Hello World app 2'
        }
    }
})

app2.mount('#app2')

