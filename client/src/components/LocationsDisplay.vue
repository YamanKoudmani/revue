<template>
    <div class="list">
      <ul class="locList">
        <li class="actualList" v-for="[location, ratVal] in ratingArr" :key="location">
        <div class = "name">{{location}} </div> <Rating class="rating" :value="ratVal"></Rating>
        </li>
      </ul>
    </div>
</template>
<script>
import store from '@/store/index'
import Rating from '@/components/Rating'

export default {
  name: 'LocationsDisplay',
  components: {Rating},
  /*
   * Initial state of the component's data.
   */
  data: function() {
    return {
      currentService: [],
      addedRatings: 0,
      ratingArr: new Map(),
    };
  },
  mounted(){
    this.currentService = store.state.selectedService;
    this.timer = setInterval(this.fetchCurrentService, 1000);
    this.timer2 = setInterval(this.avgRating2, 1000);

    console.log(this.currentService);
  },

  methods: {
    avgRating2(){
    var a,z;
    var locationsList = this.currentService.locations;
    this.ratingArr.clear();
    for (z = 0; z < locationsList.length; z++){
      var temp = locationsList[z];
      var avg = 0;
      for (a = 0; a < temp.reviewList.length; a++){
        this.addedRatings += temp.reviewList[a].rating;
      }
      if (temp.reviewList.length > 0){
          avg = this.addedRatings / temp.reviewList.length;
      }
      this.ratingArr.set(temp.name, avg);
      this.addedRatings = 0;
    }
    console.log(this.ratingArr);

    },
    avgRating(locationL){
      console.log("In method");
      var y;
      this.addedRatings = 0;
        var temp = locationL;
        for (y = 0; y < temp.reviewList.length; y++){
          this.addedRatings += temp.reviewList[y].rating;
          console.log("adding ratings...");
        }
      if (temp.reviewList.length > 0){
      return this.addedRatings / temp.reviewList.length;
      }
      else {
        return 0;
      }
    },
    fetchCurrentService(){
      this.currentService = store.state.selectedService;
      console.log(this.currentService);
    },
  },
}
</script>

<style scoped>
.list {
  justify-content: flex-end;
}

.locList {
  margin-top: 20px;
  margin-left: 20px;
}
.actualList{
  display: flex;
}
.name{
  flex: 40%;
}
.rating {
  flex: 60%;
  
}
</style>
