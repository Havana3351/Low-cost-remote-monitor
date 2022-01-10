<template>
	<div id="app">
		<NavMenu></NavMenu>
		<Breadcrumb id="Breadcrumb"></Breadcrumb>
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
	#Breadcrumb{
		margin-left: 500px;
	}
</style>
