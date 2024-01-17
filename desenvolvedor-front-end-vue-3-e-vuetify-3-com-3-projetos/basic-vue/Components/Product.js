app.component("product-display", {
  setup() {
    const productTitle = "Long Line T-Shirt";
    const productBrand = "Mychos";

    const titleWithBrand = computed(() => {
      return productTitle + " - " + productBrand;
    });

    return {
      productImageSrc: ref("./assets/t-shirt.jpeg"),
      productImageAlt: ref("longline t-shirt"),
      productQuantity: ref(10),
      productDetails: ["50% cotton", "30% polyester", "20% wool"],
      productVariant: [
        {
          id: 1,
          color: "green",
        },
        {
          id: 2,
          color: "blue",
        },
      ],
      titleWithBrand,
    };
  },
  template: `   
        <div>
            <div>
                <img v-bind:src="productImageSrc" v-bind:alt="productImageAlt" />
            </div>

            <div>
                <h1>{{titleWithBrand}}</h1>
                <p v-if="productQuantity == 0">Out of Stock</p>
                <p v-else-if="productQuantity > 0 && productQuantity < 10">
                    Almost of out
                </p>
                <p v-else>In Stock</p>

                <ul>
                    <li v-for="d in productDetails">{{d}}</li>
                </ul>

                <div
                    v-for="v in productVariant"
                    v-bind:key="v.key"
                    v-bind:style="{ backgroundColor: v.color}"
                >
                    {{v.color}}
                </div>
            </div>

            <button v-bind:disabled="productQuantity == 0" @click="$emit('add-to-cart')">
                Add To Cart
            </button>
         
    </div>
  `,
});
