<template>
	<div id="register">
		<div class="box">
			<RegisterBox></RegisterBox>
		</div>
		<div :style="bgImg" class="background">
		</div>
	</div>
</template>

<script>
import RegisterBox from '../../components/LoginReg/RegisterBox.vue'
export default{
	name:'Register',
	components:{
		RegisterBox
	},
	data() {
	    return {
	        bgImg: {
	            //backgroundImage: "url(" + require("../../assets/images/login1.jpg") + ")",
	            backgroundRepeat: "no-repeat",
	            backgroundSize: "1500px auto"
	        }
	     }
	}
}
</script>

<style>
#register .background{
    height: 100%;
	width: 100%;
	z-index:-1;
    position: absolute;	
}
#register .box{
	z-index:1;
	position: absolute;
	margin-top: 6%;
	margin-left: 20%;
}
</style>
