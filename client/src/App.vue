<template>
    <div id="app">
   
        <NavBar />
         
        <main>
            <router-view />
        </main>
       
        
             
        
       
    </div>
</template>

<script>
import NavBar from '@/components/NavBar'

export default {
    name: 'app',
    components: { NavBar },

    created() {
        this.$store.dispatch('updateSubscribedSubvues')
    }
}
</script>

#service{
    
  margin:200px 50px 0;
  font-size: 75px;
  font-weight: bold;
  text-align: center;
  color:darkslategrey;

}
<style>
#app {
    font-family: "Avenir", Helvetica, Arial, sans-serif;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
}
</style>
