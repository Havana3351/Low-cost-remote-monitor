<template>
	<div id="app">
		<NavMenu></NavMenu>
		<Breadcrumb id="Breadcrumb"></Breadcrumb>
		<el-divider id="divider1"></el-divider>
	</div>
</template>

<script>
	import NavMenu from '../components/NavMenu.vue'
	import Breadcrumb from '../components/Breadcrumb.vue'

	export default{
		components: {
		  NavMenu, 
		  Breadcrumb,
		},
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
</style>
