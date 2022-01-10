<template>
	<div>
		<NavMenu></NavMenu>
		<Breadcrumb id="Breadcrumb"></Breadcrumb>
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
	
	export default{
		components: {
		  NavMenu,
		  Breadcrumb,
		},
		data() {
		  return {
		    activeName: 'first'
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
		  		if(type == '/video/realetime'){
					this.activeName ='first'
				}
				else{
					this.activeName =  'second'
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
		margin-top: 23px;
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
</style>
