<template>
	<div id="home">
		<h1>{{ msg }}</h1>
		<van-button type="default" @click="gotohumi" id="go-humi">去温湿度</van-button>
		<van-button type="default" @click="gotovedio" id="go-vedio">去看视频</van-button>
	</div>
</template>

<script>
	export default{
		name: 'Home',
		data () {
		    return {
		      msg: '你给我出来！！ball ball you'
		    }
		  },
		methods:{
		    gotohumi(){
		        //点击跳转至上次浏览页面
		        // this.$router.go(-1) 
		        //指定跳转地址
		        this.$router.replace('/temhui')
		    },
			gotovedio(){
				//点击跳转至上次浏览页面
			    // this.$router.go(-1) 
				//指定跳转地址
				this.$router.replace('/video')
			}
	    }
	}
</script>

<style>
	#home {
	  font-family: 'Avenir', Helvetica, Arial, sans-serif;
	  -webkit-font-smoothing: antialiased;
	  -moz-osx-font-smoothing: grayscale;
	  text-align: center;
	  color: #2c3e50;
	  margin-top: 60px;
	}
</style>
