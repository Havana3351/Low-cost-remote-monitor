<template>
	<div>
		<NavMenu></NavMenu>
		<Breadcrumb id="Breadcrumb"></Breadcrumb>
		<Avatar id="Avatar"></Avatar>
		<el-divider id="divider1"></el-divider>
			<el-tabs v-model="activeName" type="border-card" @tab-click="handleClick" id="tabs">
			    <el-tab-pane label="实时视频" name="first" id="real">
					<router-view></router-view>
				</el-tab-pane>
			    <el-tab-pane label="历史视频" name="second" id="history">
					<router-view></router-view>
				</el-tab-pane>
			</el-tabs>
	</div>
</template>

<script>
	import NavMenu from '../../components/NavMenu.vue'
	import Breadcrumb from '../../components/Breadcrumb.vue'
	import Avatar from "../../components/Avatar";
	
	export default{
		components: {
		  	NavMenu,
		  	Breadcrumb,
			Avatar
		},
		data() {
		  return {
		    activeName: "first"
		  };
		},
		mounted() {
		    //挂载时通过location.search拿到url后的部分
		    this.updateType();
		},
		methods: {
		  handleClick(tab, event) {
		    console.log(tab, event);
			if(tab.name === "first"){
				this.$router.push('/video/realtime');
			}
			else{
				this.$router.push('/video/historytime');
			}
		  },
		  updateType() {
		        let type = this.$route.path;
			  	console.log(type);
		  		if(type === '/video/realtime'){
					this.activeName = "first";
				}
				else if(type === '/video/historytime'){
					this.activeName = "second";
				}
				else{
					this.$router.push('/video/realtime');
				}
		        //通过拿到的值不同，更改activeName的值
		        console.log(type);
		  },
		}
	}
</script>

<style>
	#divider1{
		width: 86%;
		margin-top: 11px;
		margin-left: 244px;
	}
	#Breadcrumb{
		margin-top: 20px;
		margin-left: 300px;
	}
	#tabs{
		width: 86%;
		margin-top: -23px;
		margin-left: 244px;
	}
	#history{
		height: 560px;
	}
	#real{
		height: 560px;
	}
	#Avatar {
		margin-left: 93%;
		margin-top: -27px;
	}
</style>
