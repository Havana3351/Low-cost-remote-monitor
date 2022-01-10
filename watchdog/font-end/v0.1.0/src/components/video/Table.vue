<template>
		<el-table
		    :data="tableData1"
		    style="width: 55%"
			stripe
		    max-height="470"
			@row-dblclick="getPicture">
		    <el-table-column
		      fixed
		      prop="date"
		      label="日期"
		      width="150">
		    </el-table-column>
			<el-table-column
			  fixed
			  prop="time"
			  label="时间"
			  width="150">
			</el-table-column>
		    <el-table-column
		      prop="name"
		      label="用户名"
		      width="120">
		    </el-table-column>
		    <el-table-column
		      prop="address"
		      label="地址"
		      width="300">
		    </el-table-column>
		</el-table>
</template>

<script>
	import store from '../../store/index.js'
	
	 export default {
	    methods: {
	      deleteRow(index, rows) {
	        rows.splice(index, 1);
	      },
		  getPicture(val){
			  console.log(val.date);
			  var date = val.date;
			  var time = val.time;
			  console.log(time);
			  this.$axios({
				  method: 'post',
				  url: 'http://47.95.11.87/api/videorecord',
				  data: {
					  picturedate: date,
					  time: time
				  },
				  responseType: 'blob'
			  })
			  .then(response=> (this.info = response))
			  .catch(function (error) { // 请求失败处理
			          console.log(error);
			  });
			  if(this.info != false){
				  console.log(typeof this.info);
				  console.log(this.info);
				  let picture = this.info.data;
				  let src = window.URL.createObjectURL(picture);
				  store.commit('video/setPictureValue', src);
				  console.log(store.state.video.pictureValue);
			  }
		  }
	    },
	    data() {
	      return {
	        info: null
	      }
	    },
		computed:{
			tableData1: function(){
				return store.state.video.tableValue.tables;
			}
		}
	  }
</script>

<style>
</style>
