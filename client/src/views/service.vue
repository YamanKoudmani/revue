<template>
    <div>
    <div class="float">
    <div class="knox"><img src ="/assets/Knox.jpg"
    width=250px;
    height=250px;
    align=right;
    />
    </div>

    <div class="container">
   <div class="photo"><img src ="/assets/Knox_oldmain.jpg"
    width=400px;
    height=300px;
    align=left; />
    </div>
    
    </div>


  <div class="container">
      <div class="SearchPage">
        <h1>Services</h1>
        
    </div>
    
    </div>

    </div>
<div class="search">
<SearchBox :items="services" filterby="name" />
    </div>

    <div class="bod">
      
    <h2> Service Name: </h2>
    
    </div>


    <div class="locate">
    <h3>Location Ratings:</h3>
    <Rating value="3"></Rating>
    </div>

    <div class="student">
    <h4>Student Reviews</h4>
    <input type="button" value="Add Reviews" style="float: right; font-size:30px; ,margin:0 0 0;">
    </div>
  
  
    </div>
</template>



<script>
import Rating from '@/components/Rating'
import SearchBox from '@/components/SearchBox'
import services from '@/assets/services.js'


export default {
  name: 'Service',
    mounted(){
        this.services = services;
        console.log(this.services);
    },
    data(){
        return {
            services: []
        };
    },
    components: { 
        SearchBox,Rating
    }
}

</script>




<style scoped>
.float{

padding:10px;

}
 .container{
   margin:0px,50px,0;
   width: 40%;
    float: left;
    padding: 20px;  
}

.knox{
   margin:0px,0px,0;
   width: 250px;
   height: 0%;
  float: right;
      
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