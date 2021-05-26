<template lang="html">
  <div class="confirmation_page">
    <img
      class="confirm_icon"
      alt="confirm icon is here"
      src="@/assets/Verification.jpg"
    />
    <div class="announce">
      <p>
        Thank you for signing up please check your email address to verify your
        account.
      </p>
    </div>
    <input type="button" value="Home Page" class="logout" @click="logout()" />
  </div>
</template>

<script>
import AuthenticationService from "@/services/AuthenticationService";
export default {
  name: "Confirmation",
  methods: {
    logout() {
      this.$store.dispatch("setToken", null);
      this.$store.dispatch("setUser", null);
      this.$router.push({ name: "Search-Page" });
    },
  },
  mounted() {
    AuthenticationService.confirmation();
  },
};
</script>
<style scoped lang="css">
.confirm_icon {
  display: block;
  margin-left: auto;
  margin-right: auto;
  width: 200px;
}

.announce {
  width: 50%;
  margin: auto;
  text-align: center;
  border: 3px solid rgb(23, 92, 93);
  border-radius: 20px;
}

.logout {
  float: right;
  display: inline-block;
  background: linear-gradient(45deg, #77aa99, #77ff95);
  border-radius: 100px;
  padding: 10px 20px;
  box-sizing: border-box;
  text-decoration: rgb(5, 5, 5);
  font-weight: bold;
  color: rgb(12, 12, 12);
  box-shadow: 3px 8px 22px rgba(94, 28, 68, 0.15);
  text-shadow: 0 1px 1px rgba(207, 35, 35, 0.2);
}
</style>
