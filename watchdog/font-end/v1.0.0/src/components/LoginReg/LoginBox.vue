<template>
	<div id="login-box">
		<h1>Login</h1>
		<div class="form">
			<div class="item">
				<i class="el-icon-s-custom"></i>
				<input type="text" placeholder="Username" v-model="username">
			</div>
			<div class="item">
				<i class="el-icon-key"></i>
				<input type="password" placeholder="Password" v-model="password">
			</div>
		</div>
		<van-button type="default" @click="gotohome">Login</van-button>
		<br/>
		<el-link type="warning" @click="gotoregister">Register</el-link>
	</div>
</template>

<script>
import qs from 'qs'
import axios from 'axios'
import {setCookie} from '../../cookie.js'

export default{
	name:'LoginBox',
	data() {
		return {
			username:"",
			password:"",
			info: null
	  };
	},
	// mounted(){
	//     if(cookie.getCookie("username")){
	//     this.$router.replace('/home');
	//    }
	// },
	methods:{
		gotohome(){
			var Username = this.username;
			var Password = this.password;
			console.log(Username);
			let params = new URLSearchParams();
			params.append('username',Username );
			params.append('password',Password);
			axios.post('http://47.95.11.87/api/login', params)
			  .then((res)=>{
			    console.log(res.data)
			    console.log(typeof res.data)
			    if(res.data==-1){
					alert("用户不存在")
			    }else if(res.data == 0){
			        alert("密码输入错误")
			    }//else if(res.data == "admin"){
			    //     this.$router.replace('/home')
			    // }
				else{
			        alert("登陆成功")
					setCookie("username",Username,1000*60)
			        setTimeout(function(){
						this.$router.replace('/main')
					}.bind(this),1000)
			    }
			  })
			  .catch(function (error) {
			    console.log(error);
			  });
			// this.$router.replace('/home');
		},
		gotoregister(){
			this.$router.replace('/register');
		},
		data(){
		    return {
		        imgSrc:require('../../assets/images/login.jpg')
		    }
		}
	},
}
</script>

<style>
#login-box h1{
	color: #fff;
}
#login-box .form .item{
	margin-top: 0.9375rem;
}
#login-box .form .item i{
	font-size: 1.125rem;
	color: #FFF;
}
#login-box .form .item input{
	width: 15.625rem;
	font-size: 1.125rem;
	border: 0;
	border-bottom: 2px solid #FFF;
	padding: 5px 10px;
	background: #ffffff00;
	color:#fff;
}
#login-box button{
	margin-top: 0.9375rem;
	width: 11.9375rem;
	height: 2.1875rem;
	font-size: 0.9375rem;
}
</style>