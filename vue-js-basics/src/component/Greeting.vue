<script setup>
const props = defineProps(["greetingMessage", "num", "id", "title"])
const emits = defineEmits(["someEvent"])
const model = defineModel()

const [btitle, modifiers] = defineModel("btitle", {
    set(value) {
        if (modifiers.capitalize) {
            console.log("Aqui")
            return value.charAt(0).toUpperCase() + value.slice(1)
        }
        return value
    }

})
console.log(modifiers)

console.log(btitle)


function update() {
    model.value++
}

const some = () => {
    emits("someEvent", "Doe")
}

import { useAttrs } from 'vue'

const attrs = useAttrs()

console.log(attrs)

</script>

<template>
    <span>{{ props.greetingMessage }}</span>
    <hr />
    <span>{{ props.num }}</span>
    <button @click="some">Change Message</button>
    <button @click="$emit('someEvent', 'JOhn')">Click Me</button>

    <div>
        {{ props.id }} - {{ props.title }}
    </div>

    <div>Parent bound v-model is: {{ model }}</div>
    <button @click="update">Increment</button>

    <input type="text" v-model="btitle" />
    <div class="btn-wrapper">
        <button class="btn" v-bind="$attrs">Click Me</button>
    </div>


    <header>
        <slot name="header"></slot>
    </header>
    <main>
        <slot>
            Submit <!-- fallback content -->
        </slot>
    </main>
    <footer>
        <slot name="footer"></slot>
    </footer>

    <span>Fallthrough attributes: {{ $attrs }}</span>

</template>
