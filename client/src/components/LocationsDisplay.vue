<template>
    <div class="list">
      <ul class="locList">
        <li  v-for="location in currentService.locations" v-bind:key="location">
          {{location.name}} <Rating class="rating" :value="avgRating"></Rating>
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
      currentService: []
    };
  },
  mounted(){
    this.currentService = store.state.selectedService;
    console.log(this.currentService);
  },
  computed: {
    avgRating: function(){
      var rand = Math.floor((Math.random() *5) + 1);
      console.log(rand);
      return rand;
    }
  }
}
</script>

<style scoped>
.list {
  display: flex;
}

.locList {
  flex: 1;
  margin-top: 20px;
  margin-left: 20px;
}
.rating {
  flex: 3;
}
</style>
