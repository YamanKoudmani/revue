<template>
  <div class="container">
    <div class="title">
      <div class="t-obj">
        <div class="image1">
        <img src="/assets/Knox.jpg" width="250px;" height="250px;" />
        </div>
      </div>
      <div class="t-obj">
        <div class="SearchPage">
          <h1>Services</h1>
        </div>
        <div class="image">
        <img src="/assets/Knox_oldmain.jpg" width="450px;" height="300px; " />
        </div>
      
        </div>
        
      
    </div>
<div class="searchbox">
          <SearchBox :items="services" filterby="name" />
          </div>
    <div class="bod">
      <h2>{{ currentService.name }}</h2>
      <h4>{{ currentService.description }}</h4>

      <LocationsDisplay></LocationsDisplay>
    </div>

    <div class="student">
      <h5>Student Reviews</h5>
      
      
      <input
        type="button"
        value="Add Reviews"
        style="float: right; font-size:20px;font-weight: bold; ,margin:0 0 0;"
        @click="$router.push({ name: 'create_review' })"
      />
      <span
        class="reviewsTop"
        v-for="location in currentService.locations"
        v-bind:key="location"
      >
        {{ location.name }} <br />
        <ul class="reviewsMiddle">
          <li v-for="Review in location.reviewList" v-bind:key="Review">
            {{ Review.username }} <br />
            {{ Review.title }} <br />
            {{ Review.content }} <br /><br />
          </li>
        </ul>
      </span>

      
    </div>
  </div>
</template>

<script>
import SearchBox from "@/components/SearchBox";
import ServicesService from "@/services/ServicesService";
import LocationsDisplay from "@/components/LocationsDisplay";
import store from "@/store/index";
export default {
  name: "Service",
  components: {
    SearchBox,
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
  },
  watch: {
    $route() {
      this.fetchData();
    },
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
  },
};
</script>

<style scoped>
.reviewsTop {
  font-size: 24px;
}
.reviewsMiddle {
  font-size: 16px;
}
.title {
  display: flex;
  flex-direction: row;
  justify-content: space-between;
  align-items: stretch;
}
.t-obj {
  flex: 1;
}

.image {
  margin: -318px 1220px;
  
 
}.image1 {
  margin: -10px -20px;
  
 
}

.SearchPage {
  margin: 0px 450px;
  margin-top: 0px;
  width: 800px;
  text-align: left;
  font-size: 45px;
}
.searchbox {
  margin: 20px 400px;
  margin-top: 60px;
  width: 900px;
  
  
  
}
.search {
  margin: 0px 500px;
  margin-top: 250px;
  width: 640px;
  
}
.bod {
  margin: 150px 30px 0;
  font-size: 30px;
  font-weight: bold;
  text-align: left;
  color: darkslategrey;
  color:white;
}

.locate {
  margin: 125px 30px 0;
  font-size: 45px;
  font-weight: bold;
  text-align: left;
  color: darkslategrey;
}
.student {
  margin: 35px 30px 0;
  font-size: 25px;
  font-weight: bold;
  text-align: left;
  color: darkslategrey;
  color:white;
}
h1{
color:white;
font-family:Impact, Haettenschweiler, 'Arial Narrow Bold', sans-serif;
font-size: 120px;
}
h2{
  color:white;
}
.h4{
  color:white;
}
h5{
  color:white;
  font-size: 40px;
  font-weight: bold;
}
.container{
  background-color:black;
  
background-image: url('/assets/o.jpg');
background-size:1900px 1150px ;
background-repeat: no-repeat;


  
 

}
input[type=button]{
  display: inline-block;
  background: linear-gradient(45deg, #87adfe,#ff77cd);
  border-radius:100px;
  padding:10px 20px;
  box-sizing: border-box;
  text-decoration:seashell;
  color: #fff;
  box-shadow: 3px 8px 22px rgba(94,28,68,0.15);
   text-shadow: 0 1px 1px rgba(207, 35, 35, 0.2);

}
input[type=button]:hover{
  background:turquoise;
  
}


</style>
