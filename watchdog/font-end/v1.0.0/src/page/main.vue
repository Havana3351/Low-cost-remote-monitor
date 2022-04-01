<template>
	<div id="app">
		<NavMenu></NavMenu>
		<Breadcrumb id="Breadcrumb"></Breadcrumb>
		<Avatar id="Avatar"></Avatar>
		<el-divider id="divider1"></el-divider>
		<Show id="show"></Show>
	</div>
</template>

<script>
	import NavMenu from '../components/NavMenu.vue'
	import Breadcrumb from '../components/Breadcrumb.vue'
	import Avatar from "../components/Avatar"
	import Show from '../components/Show'

	export default{
		components: {
		  	NavMenu,
		  	Breadcrumb,
			Avatar,
			Show
		},
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
	#Avatar {
		margin-left: 93%;
		margin-top: -27px;
	}
	#show {
		margin-top: 3%;
		margin-left: 2%;
	}
</style>
