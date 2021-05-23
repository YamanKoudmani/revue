<template>

  <div class="container">
   
  <div class="header">
    <h1>Knox Rate-A-Service</h1></div>
    <div class="SearchPage">
      <SearchBox :items="services" filterby="name" />
    </div>
    <br><br><br><br><br>
    <ul>
    <li class="serviceList" v-for="service in services" :key="service">{{service.name}}</li> 
    </ul>
    <div class="size">
      <slideshow/>
    </div>
  

    
    </div>
</template>

<script>
import SearchBox from '@/components/SearchBox'
import ServicesService from '@/services/ServicesService'
import slideshow from '@/components/slideshow.vue';

//import services from '@/assets/services.js'
export default {
    name: 'Search-Page',
    data(){
        return {
            services: []
        };
    },
    components: { 
      SearchBox,
        slideshow
    },
    mounted(){
       this.fetchData()
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
    }
  },
}

</script>

<style scoped>
.container{
 
  min-width: 100%;
  max-height: 50%;
  background-color:#432f48;
  
}
.SearchPage {
  
  align-content: center;
  margin: 0px auto;
  margin-top: 60px;
  width: 800px;
  padding-bottom: 10px;
}

ul {
  text-align: center;

}
.serviceList{
  padding: 15px;
  font-size: 25px;
  max-width: 800px;
  color:white;
  display: inline;
  border-top-style: solid;
  

}
.size{
  align-content: center;
  margin: 50px auto;
  width:50%;
}
h1{
  margin: auto;
  width: 50%;
  text-align: center;
  align-content: center;
  font-size: 100px;
  font-weight: bold;
  color:white;
  font-family: 'Domine', serif;
}


</style>