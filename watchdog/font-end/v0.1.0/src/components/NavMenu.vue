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
			  <el-submenu index="temhui">
				<template slot="title">
				  <i class="el-icon-star-off"></i>
				  <span>温湿度查询</span>
				</template>
				<el-menu-item-group>
				  <template slot="title">温度</template>
				  <el-menu-item index="temhui">当前查看</el-menu-item>
				  <el-menu-item index="1-2">历史查看</el-menu-item>
				</el-menu-item-group>
				<el-menu-item-group title="湿度">
				  <el-menu-item index="1-3">当前查看</el-menu-item>
				  <el-menu-item index="1-4">历史查看</el-menu-item>
				</el-menu-item-group>
				<!--   <el-submenu index="1-4">
				       <template slot="title">历史查看</template> 
				       <el-menu-item index="1-4-1">选项1</el-menu-item>
				       </el-submenu>  -->
			  </el-submenu>
			  <el-menu-item index="video">
				<i class="el-icon-star-off"></i>
				<span slot="title">监控查看</span>
			  </el-menu-item>
			  <el-menu-item index="3">
				<i class="el-icon-star-off"></i>
				<span slot="title">设备管理</span>
			  </el-menu-item>
			  <el-menu-item index="4">
			  	<i class="el-icon-star-off"></i>
			  	<span slot="title">个人信息</span>
			  </el-menu-item>
			  <el-menu-item index="5">
				<i class="el-icon-setting"></i>
				<span slot="title">信息设置</span>
			  </el-menu-item>
			</el-menu>
		  </el-col>
		</el-row>
	</div>
</template>

<script>
	 export default {
	    methods: {
	      handleOpen(key, keyPath) {
	        console.log(key, keyPath);
	      },
	      handleClose(key, keyPath) {
	        console.log(key, keyPath);
	      },
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
