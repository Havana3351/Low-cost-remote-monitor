import Vue from 'vue'
import App from './App.vue'
import VueRouter from 'vue-router'
import routes from './router/router'
import { Button } from 'vant'
import axios from 'axios'

Vue.prototype.$axios = axios
Vue.use(Button)
Vue.use(VueRouter)

Vue.config.productionTip = false

const router = new VueRouter({
	routes,
})

new Vue({
	router,
	render: h => h(App),
}).$mount('#app')
