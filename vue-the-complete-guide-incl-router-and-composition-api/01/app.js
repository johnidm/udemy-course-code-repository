Vue.createApp({

    data() {
        return {
            goals: [],
            enteredValue: ''
        }
    },

    methods: {
        addGoal() {
            this.goals.push(this.enteredValue);
            this.enteredValue = '';
        }
    }

}).mount('#app');

// const buttonEl = document.querySelector('button');
// const inputEl = document.querySelector('input');
// const ulEl = document.querySelector('ul');

// const addGoal = () => {
//     const liEl = document.createElement('li');
//     liEl.textContent = inputEl.value;

//     ulEl.appendChild(liEl);

//     inputEl.value = "";
// }

// buttonEl.addEventListener('click', addGoal);
