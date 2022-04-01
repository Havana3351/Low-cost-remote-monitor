<template>
		<div >
			<el-row>
			  <el-col :span="8" v-for="(o, index) in 1" :key="o" :offset="index > 0 ? 2 : 0">
			    <el-card :body-style="{ padding: '0px' }" id="card2">
				  <el-image :src="pictrueData" class="image" ref='img'>
					  <div slot="error" class="image">
					          <img src="../../assets/logo.png" id="text1"></img>
					  </div>
				  </el-image>
			      <div style="padding: 14px;">
			        <span ></span>
			        <div class="bottom clearfix">
			        </div>
			      </div>
			    </el-card>
			  </el-col>
			</el-row>
		</div>
	
</template>

<script>
	import store from '../../store/index.js'
	
	export default {
	  data() {
	    return {
	      currentDate: new Date()
	    };
	  },
	  computed:{
		  pictrueData: function(){
			  return store.state.video.pictureValue;
		  }
	  }
	}
</script>

<style>
	  
	  .bottom {
	    margin-top: 13px;
	    line-height: 12px;
	  }
	
	  .image {
	    width: 100%;
	  }
	
	  .clearfix:before,
	  .clearfix:after {
	      display: table;
	      content: "";
	  }
	  
	  .clearfix:after {
	      clear: both
	  }

	  #card2{
		  width: 100%;
		  height: 435px;
	  }

	  #text1{
		  width: 90%;
	  }
</style>
