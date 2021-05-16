<template lang="html">
  <div class="create-review container">
    <h1>Add a review</h1>
    <form @submit.prevent="create" enctype="multipart/form-data">
      <Dropdown
        @location="getLocation($event)"
        @rating="getRating($event)"
      ></Dropdown>
      <input v-model="title" type="text" placeholder="Title" ref="title" />
      <textarea
        v-model="content"
        name="name"
        placeholder="Write your review here."
        rows="25"
        cols="80"
      ></textarea>
      <input class="button" type="submit" value="Add a review" />
    </form>
  </div>
</template>
<script>
import Dropdown from "@/components/ReviewDropdown";
import ServicesService from "@/services/ServicesService";
import store from "@/store/index";
export default {
  name: "create_review",
  components: {
    Dropdown,
  },
  data() {
    return {
      title: "",
      location: "",
      content: "",
      rating: "",
    };
  },
  methods: {
    create() {
      var reviewData = new FormData();
      reviewData.append("title", this.title);
      reviewData.append("location", this.location);
      reviewData.append("service", store.state.selectedService.name);
      reviewData.append("content", this.content);
      reviewData.append("rating", parseInt(this.rating));
      console.log(this.title, this.location, this.content, this.rating);

      ServicesService.create(reviewData)
      .then(
        ServicesService.getService(store.state.selectedService.name).then(response => { //pings the database
        this.$store.dispatch('setServiceState', response.data); //gets information from database and adds to store, cus store is out of date even though database is
        this.$router.push({ name: 'service' }); //reroutes you back to service page
        }).catch(e => {
        this.error = e.response.data
      })
        //console.log(store.state.selectedService.locations)
        )
      //.catch((error) => {
        //alert(error.response.data.error);
      //});
    },
    getLocation(event) {
      this.location = event;
      console.log(event);
    },
    getRating(event) {
      this.rating = event;
      console.log(event);
    },
  },
  //mounted() {
  //  this.location.focus();
  //},
};
</script>

<style scoped>
form {
  max-width: 1500px;
  width: 100%;
  margin: 0 auto;
}

input,
textarea {
  display: block;
  width: 100%;
  margin: 0;
  border: none;
  background: rgb(223, 224, 221);
  padding: 15px;
  margin: 20px 0;

  -webkit-box-sizing: border-box; /* Safari/Chrome, other WebKit */
  -moz-box-sizing: border-box; /* Firefox, other Gecko */
  box-sizing: border-box; /* Opera/IE 8+ */
}
</style>
