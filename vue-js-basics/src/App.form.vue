<template>
  <div>
    <form @submit.prevent="handleSubmit">

      <div class="form-control" :class="{ invalid: !userNameValid }">
        <input type="text" v-model="userName" @blur="validateInput" />
        <label for="userName">Name</label>
      </div>
      
    
      <input type="number" v-model="userAge" ref="userAgeInput" />
      <p>{{ userAge }}</p>
      <select v-model="userReferrer">
        <option value="google">Google</option>
        <option value="facebook">Facebook</option>
        <option value="twitter">Twitter</option>
      </select>
      <p>{{ userReferrer }}</p>
      
      <input type="checkbox" v-model="userInterests" value="news" />
      <label for="userInterests">News</label>
     
      <input type="checkbox" v-model="userInterests" value="tutorials" />
      <label for="userInterests">Tutorials</label>
  
      <input type="checkbox" v-model="userInterests" value="videos" />
      <label for="userInterests">Videos</label>
      <p>{{ userInterests }}</p>  

      <input type="radio" v-model="userGender" value="male" />
      <label for="userGender">Male</label>

      <input type="radio" v-model="userGender" value="female" />
      <label for="userGender">Female</label>
      <p>{{ userGender }}</p>

      <input type="checkbox" id="userAgree" v-model="userAgree" />
      <label for="userAgree">Agree?</label>

      <p>{{ userAgree }}</p>

      <button type="submit">Submit</button>
    </form>
  </div>
</template>

<script>
export default {
  data() {
    return {
      userName: "",
      userAge: 0,
      userReferrer: "twitter",
      userInterests: [],
      userGender: "male",
      userAgree: false,

      userNameValid: true,
    }
  },
  methods: {
    handleSubmit() {
      console.log(this.userName);
      console.log(this.userAge);
      console.log(this.userReferrer);
      console.log(this.userInterests);
      console.log(this.userGender);
      console.log(this.userAgree);
      console.log(this.$refs.userAgeInput.value);
    },
    validateInput() {
      if (this.userName === "") {
        this.userNameValid = false;
      } else {
        this.userNameValid = true;
      }
    }
  }
}
</script>

<style>

.form-control.invalid input {
  border: 2px solid red;
}

.form-control.invalid label {
  color: red;
}

</style> 