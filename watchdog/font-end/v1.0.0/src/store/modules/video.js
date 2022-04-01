
const state = {
    dataValue: null,
  	timeValue: null,
  	tableValue: [],
  	pictureValue: null,
	realVideoTimer: null
}

const mutations = {
	setDataValue(state, DataValue){
		state.dataValue = DataValue;
	},
	setTimeValue(state, TimeValue){
		state.timeValue = TimeValue;
	},
	setTableValue(state, TableValue){
		state.tableValue = TableValue;
	},
	setPictureValue(state, PictureValue){
		state.pictureValue = PictureValue;
	},
	setRealVideoTimer(state, RealVideoTimer){
		state.realVideoTimer = RealVideoTimer;
	},
}

const getters = {
	getDataValue: state => {
		return state.dataValue;
	}
}


export default {
  namespaced: true,
  state,
  getters,
  mutations
}