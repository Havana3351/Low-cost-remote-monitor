<template>
	<el-breadcrumb separator="/">
	  <el-breadcrumb-item v-for="item in levelList" :key="item.path" :to="item.path">
		{{item.meta.title}}
	  </el-breadcrumb-item>
	</el-breadcrumb>
</template>

<script>
	export default {
	        name: 'Navbar',
	        data() {
	            return {
	                levelList: []
	            }
	        },
	        watch: {
	            $route() {
	                this.getBreadcrumb()
	            }
	        },
	        created(){
	            this.getBreadcrumb()
	        },
	        methods:{
	            getBreadcrumb() {
	                let matched = this.$route.matched.filter(item => item.name)
					const first = matched[0];
					if (first && first.name.trim().toLocaleLowerCase() !== 'main'.toLocaleLowerCase()) {
					    matched = [{ path: '/main', meta: { title: '首页' }}].concat(matched)
					}
	                this.levelList = matched
	            }
	        }
	    }
</script>

<style>
</style>
