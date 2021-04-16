<template>
    <div class="SearchPage">
        <h1>Knox Rate-A-Service</h1>
        <SearchBox :items="services" filterby="name" />
    </div>
</template>

<script>
import SearchBox from '@/components/SearchBox'
import services from '@/assets/services.js'
export default {
    name: 'Search-Page',
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
        SearchBox
    }
}
</script>
<style scoped>
.SearchPage {
  margin: 0px auto;
  margin-top: 60px;
  width: 800px;
}
</style>