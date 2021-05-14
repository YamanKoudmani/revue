<template>
  <div class="flex-container">
    <div class="flex-row">
      <div class="col-sm">
        <img src="@/assets/Knox.jpg" class="title-image" style="float:left" />
      </div>
      <div class="col-sm">
        <p>Services</p>
      </div>
      <div class="col-sm">
        <img class="title-image" src="@/assets/knoxfinal.png" style="float:right" />
      </div>
    </div>
      <div class="tota">
    <div class="searchbox">
      <SearchBox :items="services" filterby="name" /> 
    </div>
    </div>
    <div class="bod">
      <h1>{{ currentService.name }}</h1>
      <h4>{{ currentService.description }}</h4> <br />
      <LocationsDisplay :currService="currentService"> </LocationsDisplay>
    </div>
     
    <div class="student">
      <h5>Student Reviews</h5>

      <span
        class="reviewsTop"
        v-for="location in currentService.locations"
        v-bind:key="location"
      >
        <h2>{{ location.name }}</h2> <br />
        <ul class="reviewsMiddle">
          <li class="reviewsMiddleBlock" v-for="Review in location.reviewList" v-bind:key="Review">
          <br />
            <p>{{ Review.username }} </p>
            <div class="flex-list">
            <div class="ReviewTitle"> <p> {{ Review.title }} </p></div>
            <Rating class="ReviewRating" :value="Review.rating"></Rating>
            </div> 
            <p> {{ Review.content }} </p>
          </li>
        </ul>
      </span>
      <input
        type="button"
        value="Add Reviews"
        style="float: right; font-size:20px;font-weight: bold; ,margin:0 0 0;"
        @click="$router.push({ name: 'create_review' })"
      />

    </div>
  </div>
</template>

<script>
import SearchBox from "@/components/SearchBox";
import ServicesService from "@/services/ServicesService";
import Rating from "@/components/Rating";
import store from "@/store/index";
import LocationsDisplay from '../components/LocationsDisplay.vue';
export default {
  name: "Service",
  components: {
    SearchBox,
    Rating,
    LocationsDisplay,
  },
  data() {
    return {
      services: [],
      currentService: [],
    };
  },
  mounted() {
    this.services = this.fetchData();
    this.currentService = store.state.selectedService;
    this.timer = setInterval(this.fetchCurrentService, 1000);

  },
  methods: {
    fetchData() {
      ServicesService.list()
        .then((response) => {
          this.services = response.data;
        })
        .catch((e) => {
          this.error = e.response.data;
        });
    },
    fetchCurrentService(){
      this.currentService = store.state.selectedService;
    }
  },
};

</script>

<style scoped>
.flex-container {
  background-color: rgba(69,49,72,255);
  background-image: url("~@/assets/o.jpg");
  background-size: 1900px 1150px;
  background-repeat: no-repeat;
  display: flex;
  flex-wrap: wrap;
  width: 100%;
  height: 100%;
}
.flex-row{
display:flex;
flex-direction: row;
width: 100%;
height: 100%;
flex-wrap: wrap;
}
.title-image {
  object-fit: cover;
  max-height: 100%;
  max-width:100%;
  margin: 10px;
  border-radius: 25px;

}
.col-sm {
  font-size: 120px;
  font-weight: bold;
  color: white;
  text-align: center;
  max-height: 300px;
  margin: 5px;
  flex: 1;
}
.tota{

  width: 100%;
}
.searchbox {
  margin: auto;
   width: 50%;
  height: 100px;
 
}

.bod {
 
  margin: 0px 30px 0;
  font-size: 30px;
  font-weight: bold;
  text-align: left;
  color: red;
  color: white;

  height: auto;
}

.locate {
  margin: 125px 30px 0;
  font-size: 45px;
  font-weight: bold;
  text-align: left;
  color: darkslategrey;
}
.student {
  margin: 35px  0;
  padding: 30px;
  font-size: 25px;
  font-weight: bold;
  text-align: left;
  color: darkslategrey;
  color: white;
  background-color: #432f48;
  width: 100%;
}
.reviewsTop{
  margin: 10px;
  border: red;
  
  border-width: thick;
 
}
.reviewsMiddle{
  margin: 20px;
  list-style-type: none;
}
.reviewsMiddleBlock{
  border-bottom: 3px solid;
}
h1 {
  color: white;
  font-weight: bold;
  font-size: 100px;
}
.h4 {
  color: white;
  font-size: 25px;
}
h5 {
  color: white;
  font-size: 40px;
  font-weight: bold;
}

.flex-list{
  display: flex;
}
.ReviewTitle{
  flex: 50%;
}
.ReviewRating{
  flex: 50%;
}
.knox-oldmain {
  width: 450px;
  height: 300px;
}
input[type="button"] {
  display: inline-block;
  background: linear-gradient(45deg, #87adfe, #ff77cd);
  border-radius: 100px;
  padding: 10px 20px;
  margin: 30px;
  box-sizing: border-box;
  text-decoration: seashell;
  color: #fff;
  box-shadow: 3px 8px 22px rgba(94, 28, 68, 0.15);
  text-shadow: 0 1px 1px rgba(207, 35, 35, 0.2);
}
input[type="button"]:hover {
  background: turquoise;
}
</style>
