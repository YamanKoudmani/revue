
import { createApp } from 'vue';
import App from './App.vue'
import router from './router'
import store from './store'
import 'bootstrap'
import 'bootstrap/dist/css/bootstrap.min.css'

require('@/assets/style.css')
require('vue-dynamic-star-rating');

createApp(App).use(router).use(store).mount('#app')
