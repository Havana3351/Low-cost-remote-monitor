<template>
	<div>
		<el-time-picker
			@change="getTime"
		    is-range
		    v-model="value1"
		    range-separator="至"
		    start-placeholder="开始时间"
		    end-placeholder="结束时间"
		    placeholder="选择时间范围"
			format='HH:mm'
			value-format='HH:mm'>
		</el-time-picker>
	</div>
</template>

<script>
	import store from '../../store/index.js'
	import {getCookie} from '../../cookie.js'
	
	export default {
	    data() {
	      return {
	        value1: [new Date(2016, 9, 10, 8, 40), new Date(2016, 9, 10, 9, 40)],
			info: null
	      };
	    },
		methods:{
			getTime: function(){
				console.log(String(this.value1));
				store.commit('video/setTimeValue',String(this.value1));
				
				
				/*var test = '{"sites":[{"date": "2018-05-24", "time": "2052", "name": "王小虎", "address": "上海市普陀区金沙江路 1518 弄"}]}';
				var test1 = JSON.parse(test);
				console.log(test1);
				store.commit('video/setTableValue',test1);
				console.log(store.state.video.tableValue);*/
				
				var recorddate = store.state.video.dataValue;
				var recordminute = store.state.video.timeValue;
				var username = getCookie('username');
				console.log(username);
				console.log(recorddate);
				console.log(recordminute);
				if(recorddate != null){
					this.$axios
					.post('http://47.95.11.87/api/videosavedata',{
							recorddate: recorddate,
							recordminute: recordminute,
							username: username
					})
					.then(response=> (this.info = response))
					.catch(function (error) { // 请求失败处理
					        console.log(error);
					});
					if(this.info != null){
						console.log(typeof this.info);
						console.log(this.info);
						
						var tableArr = this.info.data;
						
						console.log(typeof tableArr);
						console.log(tableArr);
						
						var mid = JSON.parse(tableArr);
						console.log(typeof mid);
						console.log(mid);
						store.commit('video/setTableValue',mid);
						console.log(store.state.video.tableValue);
						store.commit('video/setDataValue',null);
						store.commit('video/setTimeValue',null);
					}
				}
			}
		}
	  }
</script>

<style>
</style>
