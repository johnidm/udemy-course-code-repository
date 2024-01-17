const { createApp, ref, computed } = Vue;

const app = createApp({
  setup() {
    const cartCount = ref(2);

    const addToCart = () => {
      cartCount.value += 1;
    };

    return {
      cartCount,
      addToCart,
    };
  },
});
