<template>
	<div id="video">
		<h1>Pi Video Surveillance</h1>
		<img id="randimg" src="http://47.95.11.87/api/video"></img>
		<div>
			<van-button plain type="primary" @click="returnPage" :style="{top: '130px' }">
				点击返回主页
			</van-button>
		</div>
	</div>
</template>

<script>
	//http://47.95.11.87/api/video
	export default {
	  name: 'Video',
	  data() {
	        return {
	          value: 0,
			  timer: null
	        };
	  },
	  mounted: function(){
	  	this.$nextTick(function (){
	  		if(this.timer == null){
	  			this.value ++;
	  			console.log(this.value);
	  			this.timer = setInterval(function(){
					document.querySelector('#randimg').src="http://47.95.11.87/api/video?"+Math.random();
				}, 500);
	  		}
	  	})
	  },
	  beforeDestroy: function(){
	    clearInterval(this.timer);
	  	this.timer = null;
	  },
	  methods:{
	  		returnPage: function(){
	  			this.$router.replace('/home')
	  		}
	  }
	}
	
</script>

<style>
</style>
