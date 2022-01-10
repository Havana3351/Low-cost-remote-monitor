<template>
	<div>
		<div id="card2">
			<el-row>
			  <el-col :span="8" v-for="(o, index) in 1" :key="o" :offset="index > 0 ? 2 : 0">
			    <el-card :body-style="{ padding: '0px' }">
				  <el-image :src="pictrueData" class="image" ref='img'>
					  <div slot="error" class="image-slot">
					          <img src="../../assets/logo.png"></img>
					  </div>
				  </el-image>
			      <div style="padding: 14px;">
			        <span>历史视频</span>
			        <div class="bottom clearfix">
			        </div>
			      </div>
			    </el-card>
			  </el-col>
			</el-row>
		</div>
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
	.time {
	    font-size: 13px;
	    color: #999;
	  }
	  
	  .bottom {
	    margin-top: 13px;
	    line-height: 12px;
	  }
	
	  .button {
	    padding: 0;
	    float: right;
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
</style>
