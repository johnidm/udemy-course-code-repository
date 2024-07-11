const app = Vue.createApp({
    data() {
        return {
            friends : [
                {id: 1, name: 'John', age: 20, email: 'john@example.com'},
                {id: 2, name: 'Jane', age: 25, email: 'jane@example.com'},
                {id: 3, name: 'Jim', age: 30, email: 'jim@example.com'},
                {id: 4, name: 'Jill', age: 35, email: 'jill@example.com'},
            ]
        }
    }
});

app.component('friend-card', {
    props: ['friend'],
    template: `
        <div class="card-container">
            <div class="card-items">
                <h4><b>{{ friend.name }}</b></h4>
                <p>{{ friend.age }}</p>
                <p>{{ friend.email }}</p>
            </div>
        </div>
    `
});

app.mount('#app')

