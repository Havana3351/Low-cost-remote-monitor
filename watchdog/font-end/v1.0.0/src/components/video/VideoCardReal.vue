<template>
	<div id="card1">
		<el-row>
		  <el-col :span="8" v-for="(o, index) in 1" :key="o" :offset="index > 0 ? 2 : 0">
		    <el-card :body-style="{ padding: '0px' }">
				<el-image src="http://47.95.11.87/api/video" class="image" id="randimg">
					<div slot="error" class="image-slot">
						<img src="../../assets/logo.png"></img>
					</div>
				</el-image>
		      <div style="padding: 14px;">
		        <span>实时视频</span>
		        <div class="bottom clearfix">
		          <time class="time">{{ currentDate }}</time>
		        </div>
		      </div>
		    </el-card>
		  </el-col>
		</el-row>
	</div>
</template>

<script>
	export default {
	  data() {
	    return {
	      currentDate: new Date(),
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
	    window.clearInterval(this.timer);
	  	this.timer = null;
	  },
	}
</script>

<style>
	.image {
		width: 120%;
	}
</style>
