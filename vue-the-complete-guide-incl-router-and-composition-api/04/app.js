const getRandomNumber = (min, max) => {
    return Math.floor(Math.random() * (max - min + 1) + min);
}


const app = Vue.createApp({
    data() {
        return {
            playerHealth: 100,
            monsterHealth: 100,
            currentRound: 0,

        }
    },
    computed: {
        monsterBarStyle() {
            return { width: this.monsterHealth + '%' }
        },
        playerBarStyle() {
            return { width: this.playerHealth + '%' }
        },
        mayUseSpAttach() {

            return this.currentRound % 3 !== 0;
        }
    },
    methods: {
        attackMonster() {
            this.currentRound++;
            const attackValue = getRandomNumber(5, 12);
            this.monsterHealth -= attackValue;
            this.attackPlayer();
        },
        attackPlayer() {
            const attackValue = getRandomNumber(8, 15);
            this.playerHealth -= attackValue;
        },
        specialAttack() {
            this.currentRound++;
            const attackValue = getRandomNumber(10, 25);
            this.attackMonster -= attackValue;
            this.attackPlayer()
        },
        healAttack() {

            if ()

        }
    }
});

app.mount('#app');
