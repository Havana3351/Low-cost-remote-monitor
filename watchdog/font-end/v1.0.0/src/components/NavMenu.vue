<template>
	<div id="slide-bar">
		<el-row class="tac">
		  <el-col :span="12">
			<h3 class="el-icon-menu"> WatchDog</h3>
			<el-menu
			  :router=true 
			  :default-active="$route.name"
			  class="el-menu-vertical-demo"
			  @open="handleOpen"
			  @close="handleClose"
			   background-color="#545c64"
			   text-color="#fff"
			   active-text-color="#ffd04b">
			  <el-submenu index="temhuireal">
				<template slot="title">
				  <i class="el-icon-star-off"></i>
				  <span>温湿度查询</span>
				</template>
				<el-menu-item-group>
				  <template slot="title">温湿度</template>
				  <el-menu-item index="temhuireal">当前查看</el-menu-item>
				  <el-menu-item index="temhuiHis" @click="getData">历史查看</el-menu-item>
				</el-menu-item-group>
			  </el-submenu>
			  <el-menu-item index="video">
				<i class="el-icon-star-off"></i>
				<span slot="title">监控查看</span>
			  </el-menu-item>
			  <el-menu-item index="personal">
			  	<i class="el-icon-star-off"></i>
			  	<span slot="title">个人信息</span>
			  </el-menu-item>
			</el-menu>
		  </el-col>
		</el-row>
	</div>
</template>

<script>
	 import {getCookie} from "../cookie";
	 import store from "../store";

	 export default {
	    methods: {
	      handleOpen(key, keyPath) {
	        console.log(key, keyPath);
	      },
	      handleClose(key, keyPath) {
	        console.log(key, keyPath);
	      },
		  getData(){
			  var username = getCookie('username');
			  this.$axios.get('http://47.95.11.87/api/sensors',{
				  params: {
					  username: username
				  }
			  })
					  .then(function (response){
						  console.log(response.data);
						  console.log(response.data.tem);
						  console.log(response.data.hui);
						  if(response!= null){
							  console.log(store.state.temhui.chartOptionsHIS);
							  store.commit('temhui/setTemHuiHis',[response.data.tem,response.data.hui]);
							  console.log(store.state.temhui.chartOptionsHIS);
							  console.log(store.state.temhui.chartOptionsHIS.series);
						  }
					  })
					  .catch(function (error) { // 请求失败处理
						  console.log(error);
					  });
		  }
	    }
	  }
</script>

<style>
	#slide-bar .tac .el-menu-vertical-demo{
		width: 15.625rem;
		height: 46.875rem;
	}
	#slide-bar .tac{
		position: fixed;
		top: 0%; 
		left: 0rem;
	}
</style>
