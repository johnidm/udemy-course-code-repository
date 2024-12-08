// // fetch.js
// import { ref } from 'vue'

// export function useFetch(url) {
//   const data = ref(null)
//   const error = ref(null)

//   fetch(url)
//     .then((res) => res.json())
//     .then((json) => (data.value = json))
//     .catch((err) => (error.value = err))

//   return { data, error }
// }

import { ref, watchEffect, toValue } from 'vue'

export function useFetch(url) {
  const data = ref(null)
  const error = ref(null)

  const fetchData = () => {
    // reset state before fetching..
    data.value = null
    error.value = null

    fetch(toValue(url))
      .then((res) => res.json())
      .then((json) => (data.value = json))
      .catch((err) => (error.value = err))
  }

  watchEffect(() => {
    fetchData()
  })

  return { data, error }
}

{/* <script setup>
import { useFeatureA } from './featureA.js'
import { useFeatureB } from './featureB.js'
import { useFeatureC } from './featureC.js'

const { foo, bar } = useFeatureA()
const { baz } = useFeatureB(foo)
const { qux } = useFeatureC(baz)
</script> */}