<template>
	<div id="avatar">
		<el-avatar :src="url" :size="35" class="bg"></el-avatar>
		<el-dropdown @command="handleCommand">
		    <span class="el-dropdown-link">
		      {{ username }}<i class="el-icon-arrow-down el-icon--right"></i>
		    </span>
			<el-dropdown-menu slot="dropdown">
				<el-dropdown-item command="info">个人信息</el-dropdown-item>
				<el-dropdown-item command="pass">修改密码</el-dropdown-item>
				<el-dropdown-item divided command="log-out">退出登录</el-dropdown-item>
			</el-dropdown-menu>
		</el-dropdown>
		<el-dialog title="修改密码"
				   :visible.sync="dialogFormVisible"
				   width="30%"
				   :center="true"
				   :destroy-on-close="true">
			<el-form :model="form" status-icon :rules="rules" ref="form" label-width="90px">
				<el-form-item label="新密码:" :label-width="formLabelWidth" prop="password">
					<el-input v-model="form.password" autocomplete="off" class="input" type="password"></el-input>
				</el-form-item>
				<el-form-item label="确认密码:" :label-width="formLabelWidth" prop="checkPass">
					<el-input v-model="form.checkPass" autocomplete="off" class="input" type="password"></el-input>
				</el-form-item>
				<el-form-item label="验证码:" :label-width="formLabelWidth">
					<el-input v-model="form.code" placeholder="验证码" class="code"></el-input>
					<el-button type="info" plain class="code-button" @click="transmit">发送验证码</el-button>
				</el-form-item>
			</el-form>
			<div slot="footer" class="dialog-footer">
				<el-button @click="dialogFormVisible = false">取 消</el-button>
				<el-button type="primary" @click="submit">确 定</el-button>
			</div>
		</el-dialog>
	</div>
</template>

<script>
import bgurl from "../assets/images/login.jpg"
import {getCookie} from "../cookie.js"
import axios from 'axios'

export default {
	name:'Avatar',
	data(){
		var validatePass2 = (rule, value, callback) => {
			if (value === '') {
				callback(new Error('请再次输入密码'));
			} else if (value !== this.form.password) {
				callback(new Error('两次输入密码不一致!'));
			} else {
				callback();
			}
		};
		return{
			username: getCookie("username"),
			url: bgurl,
			dialogFormVisible: false,
			formLabelWidth: '100px',
			form: {
				password: '',
				checkPass: '',
				code: '',
			},
			rules: {
				checkPass: [
					{ validator: validatePass2, trigger: 'blur' }
				],
			}
		};
	},
    methods: {
		handleCommand(command) {
			if(command == "info"){
				this.$router.replace('/personal')
				console.log("个人信息")
			}else if(command == "pass"){
				this.dialogFormVisible = true
			}else{
				this.$router.replace('/login')
			}
		},
		transmit(){
			console.log("验证码请求：" + getCookie("username"))
			let params = new URLSearchParams();
			params.append('username',getCookie("username"));
			axios.post('http://47.95.11.87/api/reset_pw',params)
					.then((res)=>{
						console.log(res.data)
						console.log(typeof res.data)
						if(res.data == 0){
							alert("验证码发送失败，请重新请求！")
						}else{
							alert("验证码发送成功！")
						}
					})
					.catch(function (error) {
						console.log(error);
					});
		},
		submit(){
			console.log(this.form.checkPass)
			if(this.form.code == ""){
				alert("请获取验证码输入验证之后再修改密码！")
			}
			let params = new URLSearchParams();
			params.append('vertify_code',this.form.code);
			params.append('username',getCookie("username"));
			params.append('password',this.form.checkPass);
			axios.post('http://47.95.11.87/api/reset_pw',params)
					.then((res)=>{
						console.log(res.data)
						console.log(typeof res.data)
						if(res.data == 1){
							alert("修改成功!");
							this.dialogFormVisible = false;
						}else if(res.data == 0){
							alert("验证码错误！")
						}else{
							alert("验证码超时！")
						}
					})
					.catch(function (error) {
						console.log(error);
					});
		}
    }
  }
</script>

<style>
	#avatar .el-dropdown-link {
		cursor: pointer;
		color: #409EFF;
		font-size: 0.9375rem;
	}
	#avatar .el-icon-arrow-down {
		font-size: 12px;
	}
	#avatar .bg{
		margin: 0px 10px -10px;
	}
	#avatar .code{
		width: 45%;
		margin-left: 0rem;
	}
	#avatar .code-button{
		width: 30%;
		font-size: 0.625rem;
		margin-left: 1rem;
	}
	#avatar .input{
		width: 80%;
	}
</style>
