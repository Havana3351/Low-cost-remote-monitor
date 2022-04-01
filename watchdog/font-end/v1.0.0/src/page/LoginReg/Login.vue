<template>
	<div id="login">
		<div class="box">
			<LoginBox></LoginBox>
		</div>
		<div :style="bgImg" class="background">
		</div>
	</div>
</template>

<script>
import LoginBox from '../../components/LoginReg/LoginBox.vue'
export default{
	name:'Login',
	components:{
		LoginBox
	},
    data() {
	    return {
	        bgImg: {
	            backgroundImage: "url(" + require("../../assets/images/login1.jpg") + ")",
	            backgroundRepeat: "no-repeat",
	            backgroundSize: "1500px auto"
	        }
	     }
	}
}
</script>

<style>
#login .background{
    height: 100%;
	width: 100%;
	z-index:-1;
    position: absolute;	
}
#login .box{
	width: 30%;
	height:auto;
	margin: 0 auto; /*设置元素所有外边距的宽度 有1-4个值*/
	margin-top: 15%;
	margin-left: 30%;
	text-align: center;
	background: #00000090; /*后两位是半透明的百分比*/
	padding: 1.25rem 3.125rem; /*padding设置login模块的四个内边距（上右下左） 只有三个值：上、左右、下 两个值： 上下、左右*/
	z-index:1;
	position: absolute;
}
#login .box h1{
	margin: 0 auto; /*设置元素所有外边距的宽度 有1-4个值*/
	margin-top: 5%;
	margin-left: 2%;
	text-align: center;
}
</style>