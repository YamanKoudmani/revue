<template>
  
 <Carousel :autoplay="6000" :wrap-around="true">
      <template #slides>
   <Slide class="slide1" v-for="image in images"  :key="image">
     <div class="carousel__item" >
     <img :src= "image" class="d-block w-100">
       </div>
     </Slide>
     </template>
    <template #addons ="{slidesCount}">
      <navigation v-if="slidesCount>1"/>
      <pagination />
    </template>
  </carousel>
  
</template>
<script>
// If you are using PurgeCSS, make sure to whitelist the carousel CSS classes
import 'vue3-carousel/dist/carousel.css';
import { Carousel, Slide, Pagination, Navigation } from 'vue3-carousel';

export default {
  name: 'slideshow',
  components: {
    Carousel,
    Slide,
    Pagination,
    Navigation,
  },
  data:()=>({
     
      
      snapAlign: 'center',
      images: [
         
           require("@/assets/Knox_oldmain.jpg"),
          require("@/assets/cfa.jpg"),
          require("@/assets/Library.jpg"),
          require("@/assets/smc.jpg"),
          require("@/assets/Art.jpg"),
          require("@/assets/gizmo.jpg"),
           require("@/assets/fraire.jpg"),
           
           
      
      ]
    
  })
};
</script>


<style>
.carousel__item {
  min-height: 200px;
  width: 100%;
  background-color: var(--carousel-color-primary);
  color:  var(--carousel-color-white);
  font-size: 20px;
  border-radius: 8px;
  display: flex;
  justify-content: center;
  align-items: center;
}

.carousel__slide {
  padding: 10px;
}

.carousel__prev,
.carousel__next {
  box-sizing: content-box;
  border: 5px solid white;
}
</style>

