<template>
	<div class="block">
	    <span class="demonstration">请选择视频所在的日期与时间：</span>
	    <el-date-picker
		  @change="getdate"
	      v-model="value2"
	      type="daterange"
	      align="right"
	      unlink-panels
	      range-separator="至"
	      start-placeholder="开始日期"
	      end-placeholder="结束日期"
		  :default-time="['00:00:00', '23:59:59']"
		  value-format="yyyy-MM-dd"
	      :picker-options="pickerOptions">
		</el-date-picker>
	</div>
</template>

<script>
	import store from '../../store/index.js'
	import {getCookie} from '../../cookie.js'
	
	export default {
	    data() {
	      return {
	        pickerOptions: {
	          shortcuts: [{
	            text: '最近一周',
	            onClick(picker) {
	              const end = new Date();
	              const start = new Date();
	              start.setTime(start.getTime() - 3600 * 1000 * 24 * 7);
	              picker.$emit('pick', [start, end]);
	            }
	          }, {
	            text: '最近一个月',
	            onClick(picker) {
	              const end = new Date();
	              const start = new Date();
	              start.setTime(start.getTime() - 3600 * 1000 * 24 * 30);
	              picker.$emit('pick', [start, end]);
	            }
	          }, {
	            text: '最近三个月',
	            onClick(picker) {
	              const end = new Date();
	              const start = new Date();
	              start.setTime(start.getTime() - 3600 * 1000 * 24 * 90);
	              picker.$emit('pick', [start, end]);
	            }
	          }]
	        },
	        value2: '',
			info: null
	      };
	    },
		methods: {
			getdate: function() {
				console.log(String(this.value2));
				store.commit('video/setDataValue',String(this.value2));
				console.log(store.state.video.dataValue);
				
				var recorddate = store.state.video.dataValue;
				var recordminute = store.state.video.timeValue;
				var username = getCookie('username');
				console.log(username);
				console.log(recorddate);
				console.log(recordminute);
				if(recordminute != null){
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
		},
	};
</script>

<style>
</style>
