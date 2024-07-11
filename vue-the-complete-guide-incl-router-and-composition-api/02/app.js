const app = Vue.createApp({
    data() {
        return {
            card: {
                name: 'Johni Douglas Marangon',
                number: '1234567890',
                expiry: '12/2024',
                cvv: '123',
                index: 7,
            },
            person: {
                name: '',
                age: 0,
            },
            image: {
                src: 'https://www.google.com/images/branding/googlelogo/1x/googlelogo_color_272x92dp.png',
                alt: 'Goolge',
            },

            label: "<p style='background-color:Orange;'>Visa</p>",

            inputName: '',
        }
    },
    watch: {
        'person.name'(newVal, oldVal) {
            console.log('personName', newVal, oldVal);
        },
        'card.index'(newVal, oldVal) {
            if (newVal > 10) {
                this.card.index = 0;
            }
        }
    },
    computed: {
        fullPerson() {
            return 'I am ' + this.person.name + ' and I am ' + this.person.age + ' years old.';
        }
    },
    methods: {
        handleRandon() {
            this.card.index++;
        },
        setName(e, lastName) {
            this.inputName = e.target.value + ' ' + lastName;
        },
        handleSubmit(e) {
            alert(e.target.name.value);
        }

    }
})

app.mount('#app')
