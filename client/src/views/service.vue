<template>
  <div>
    <div class="title">
      <div class="t-obj">
        <img src ="/assets/Knox.jpg"
          width=250px;
          height=250px;
        />
      </div>
      <div class="t-obj">
        <img src ="/assets/Knox_oldmain.jpg"
          width=400px;
          height=300px;
        />
      </div>
      <div class="t-obj">
        <div class="SearchPage">
          <h1>Services</h1> 
          <SearchBox :items="services" filterby="name" />
        </div>
      </div>
    </div>

    <div class="bod">
      <h2> {{currentService.name}}</h2>
      <h4> {{currentService.description}}</h4>

      <LocationsDisplay></LocationsDisplay>

    </div>

    <div class="student">
      <h4>Student Reviews</h4>
        <span class="reviewsTop" v-for="location in currentService.locations" v-bind:key="location">
        {{location.name}} <br>
        <ul class="reviewsMiddle">
          <li v-for="Review in location.reviewList" v-bind:key="Review">
          {{Review.username}} <br> {{Review.title}} <br> {{Review.content}} <br><br>
          </li>
        </ul>
      </span>

      <input type="button" value="Add Reviews" style="float: right; font-size:30px; ,margin:0 0 0;">
    </div>

  </div>
</template>

<script>
import SearchBox from '@/components/SearchBox'
import ServicesService from '@/services/ServicesService'
import LocationsDisplay from '@/components/LocationsDisplay'
import store from '@/store/index'
export default {
  name: 'Service',
      components: { 
        SearchBox, LocationsDisplay
    },
    data(){
        return {
        services: [],
        currentService: []
      };
    },
    mounted(){
        this.services = this.fetchData()
        this.currentService = store.state.selectedService;
    },
    watch: {
      $route() {
          this.fetchData()
      }
    },
    methods: {
      fetchData() {
        ServicesService.list()
          .then(response => {
            this.services = response.data
          })
          .catch(e => {
            this.error = e.response.data
          })
      },
    },
}
</script>

<style scoped>
.reviewsTop{
  font-size: 24px;
}
.reviewsMiddle{
  font-size: 16px;
}
.title{
  display: flex;
  flex-direction: row;
  justify-content: space-between;
  align-items: stretch;
}
.t-obj {
  flex: 1;
}
.SearchPage{
  margin: 0px auto;
  margin-top:0px;
  width: 800px;
  text-align: left;
  font-size: 45px;
}
.search{
  margin:0px 500px;
  margin-top:250px;
  width: 640px;
}
.bod{
  margin: 400px 10px 0;
  font-size: 30px;
  font-weight: bold;
  text-align: left;
  color:darkslategrey;
}

.locate{
    margin: 125px 10px 0;
  font-size: 30px;
  font-weight: bold;
  text-align: left;
  color:darkslategrey;
}
.student{
    margin: 200px 10px 0;
  font-size: 35px;
  font-weight: bold;
  text-align: left;
  color:darkslategrey;
}

</style>
