import Vue from 'vue'
import App from './App.vue'
import VueRouter from 'vue-router'
import routes from './router/router'
import axios from 'axios'
import ElementUI from 'element-ui'
import 'element-ui/lib/theme-chalk/index.css'
import Vuex from 'vuex'
import HighchartsVue from 'highcharts-vue'
import { Button } from 'vant'

Vue.use(Vuex)
Vue.prototype.$axios = axios
Vue.use(VueRouter)
Vue.use(ElementUI)
Vue.use(HighchartsVue)
Vue.use(Button)

Vue.config.productionTip = false

const router = new VueRouter({
	routes,
	mode: 'history',
})

new Vue({
	router,
	render: h => h(App),
}).$mount('#app')