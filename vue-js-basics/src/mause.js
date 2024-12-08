// mouse.js
import { ref, onMounted, onUnmounted } from 'vue'

// by convention, composable function names start with "use"
export function useMouse() {
  // state encapsulated and managed by the composable
  const x = ref(0)
  const y = ref(0)

  // a composable can update its managed state over time.
  function update(event) {
    x.value = event.pageX
    y.value = event.pageY
  }

  // a composable can also hook into its owner component's
  // lifecycle to setup and teardown side effects.
  onMounted(() => window.addEventListener('mousemove', update))
  onUnmounted(() => window.removeEventListener('mousemove', update))

  // expose managed state as return value
  return { x, y }
}

// App.vue
// <script setup>
// import { useMouse } from './mause.js'

// const { x, y } = useMouse()
// </script>

// <template>Mouse position is at: {{ x }}, {{ y }}</template>


// event.js
// import { onMounted, onUnmounted } from 'vue'

// export function useEventListener(target, event, callback) {
//   // if you want, you can also make this
//   // support selector strings as target
//   onMounted(() => target.addEventListener(event, callback))
//   onUnmounted(() => target.removeEventListener(event, callback))
// }


// mouse.js
// import { ref } from 'vue'
// import { useEventListener } from './event'

// export function useMouse() {
//   const x = ref(0)
//   const y = ref(0)

//   useEventListener(window, 'mousemove', (event) => {
//     x.value = event.pageX
//     y.value = event.pageY
//   })

//   return { x, y }
// }