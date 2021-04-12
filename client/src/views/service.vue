<template lang="service">
<div class="float">
<div class="knox"><img src ="/assets/Knox.jpg"
    width=200px;
    height=200px;
    align=right;
    />
    </div>
<div class="container">

<div class="photo"><img src ="/assets/Knox_oldmain.jpg"
    width=400px;
    height=300px;
    align=left;
    />
    </div>

    

</div>
  <div class="container">
      <div class="serve">
       <h1 id= "name" name="ser">
      
    Services
    </h1>

 
 </div>
 
    </div>
    </div>

    <div class="bod">
    
    <h2>
    Service Name:
    </h2>
    <div id="app">
      <star-rating></star-rating>
  <p>Rating component (with set value that <strong>can't</strong> be changed)</p>
  <star-rating value="3" :disabled="true"></star-rating>
</div>
    </div>
    <div class="locate">
    <h3>
    Location Ratings:
    </h3>
    </div>
    <div class="student">
    <h4>
    Student Reviews
    </h4>
     <input type="button" value="Add Reviews" style="float: right; font-size:30px; ,margin:0 0 0;">
  </div>
  <div class="UI"> 

  </div>
</template>



<style scoped lang="css">

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
   width: 200px;
   height: 0%;
    float: right;
      
}
.serve{
  text-align:left;
font-size: 50px;
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