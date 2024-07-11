const app = Vue.createApp({

    data() {

        return {
            boxASelected: false,
            boxBSelected: false,
            boxCSelected: false,
        }
    },

    computed: {
        boxAClass() {
            return { actived: this.boxASelected }
        },
        boxBClass() {
            return { actived: this.boxBSelected }
        },
        boxCClass() {
            return { actived: this.boxCSelected }
        },
        
    },

    methods: {
        boxSelected(box) {
            
            if (box === 'A') {
                this.boxASelected = !this.boxASelected
            } else if (box === 'B') {
                this.boxBSelected = !this.boxBSelected
            } else if (box === 'C') {
                this.boxCSelected = !this.boxCSelected
            }
        }
    }

})

app.mount('#app')
