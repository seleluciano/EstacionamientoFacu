/* eslint-disable */ 
import Vue from 'vue'
import VueRouter from 'vue-router'
import App from './App.vue'
import routes from './routes'  // Asegúrate de tener un archivo con tus rutas
Vue.use(VueRouter)
const router = new VueRouter({
  routes
})
new Vue({
 router,
 render: h => h(App),
}).$mount('#app')
