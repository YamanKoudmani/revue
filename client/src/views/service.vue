<template>
  <div>
    <div class="row">
      <div class="photo">
        <img src ="/assets/Knox.jpg"
          width=250px;
          height=250px;
        />
      </div>
      <div class="photo">
        <img src ="/assets/Knox_oldmain.jpg"
          width=400px;
          height=300px;
        />
      </div>
      </div>
      
        <div class="SearchPage">
          <h1>Services</h1> 
        </div>
        <div class="search">
           <SearchBox :items="services" filterby="name" />
           </div>
        <div class="student">
      <h4>Student Reviews</h4>
      <input type="button" value="Add Reviews" style="float: right; font-size:30px; ,margin:0 0 0;">
    </div>
      


    <div class="bod">
      <h2> {{currentService.name}}</h2>
      <h4> {{currentService.description}}</h4>

      <LocationsDisplay></LocationsDisplay>
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

.photo {
  float: right;
  width: 50%;
  padding: 0px;
}

/* Clear floats after image containers */
.row::after {
  content: "";
  clear: both;
  display: table;
}
.title{
  display: flex;
  flex-direction: row;
  justify-content: space-between;
  align-items: stretch;
}
.knox {
  margin:0px,0px,0;
  

}
.oldmain {
  margin:0px,50px,0;
  

}
.SearchPage{
  margin: 0px 700px;
  margin-top:0px;
  width: 800px;
  text-align: left;
  font-size: 45px;
}
.search{
  margin:0px 550px;
  margin-top:315px;
  width: 600px;
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
    margin: 600px 0px 0;
  font-size: 35px;
  font-weight: bold;
  text-align: left;
  color:darkslategrey;
 
}

</style>
