import Vue from 'vue'
import Vuex from 'vuex'
import video from './modules/video'
import personal from './modules/personal'
import temhui from './modules/temhui'

Vue.use(Vuex)

export default new Vuex.Store({
  modules: {
    video,
    personal,
    temhui
  }
})