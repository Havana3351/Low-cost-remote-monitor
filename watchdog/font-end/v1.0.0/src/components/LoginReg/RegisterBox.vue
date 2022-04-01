<template>
	<div id="register-box">
		<h1>WatchDog,您的智能宿舍！</h1>
		<el-form :model="ruleForm" status-icon :rules="rules" ref="ruleForm" label-width="90px" class="demo-ruleForm">
		  <el-form-item label="用户名 :" prop="username" :error="errorMsg1">
		    <el-input type="text" v-model="ruleForm.username" @blur="checkName" autocomplete="off" class="input"></el-input>
		  </el-form-item>
			<el-form-item label="电话区号 :" prop="regionnum">
				<el-select v-model="ruleForm.regionnum" placeholder="区号" class="choice">
					<el-option label="+86" value="+86"></el-option>
					<el-option label="+101" value="+101"></el-option>
					<el-option label="+021" value="+021"></el-option>
					<el-option label="+852" value="+852"></el-option>
					<el-option label="+853" value="+853"></el-option>
				</el-select>
			</el-form-item>
		  <el-form-item label="电话号码 :" prop="phonenum">
		    <el-input type="text" v-model="ruleForm.phonenum" autocomplete="off" class="input"></el-input>
		  </el-form-item>
		  <el-form-item label="所属单位 :" prop="capus">
		  		<el-select v-model="ruleForm.capus" placeholder="请选择" class="choice">
		  			<el-option label="中南大学铁道学院" value="tiedao"></el-option>
		  			<el-option label="中南大学校本部" value="benbu"></el-option>
		  			<el-option label="中南大学南校区" value="nanxiao"></el-option>
		  		</el-select>
		  </el-form-item>
		  <el-form-item label="宿舍楼号 :" prop="dorm">
		    <el-input type="text" v-model="ruleForm.dorm" autocomplete="off" class="input"></el-input>
		  </el-form-item>
		  <el-form-item label="宿舍号 :" prop="room">
		    <el-input type="text" v-model="ruleForm.room" autocomplete="off" class="input"></el-input>
		  </el-form-item>
		  <el-form-item label="密码 :" prop="password">
		    <el-input type="password" v-model="ruleForm.password" autocomplete="off" class="input"></el-input>
		  </el-form-item>
		  <el-form-item label="确认密码 :" prop="checkPass">
		    <el-input type="password" v-model="ruleForm.checkPass" autocomplete="off" class="input"></el-input>
		  </el-form-item>
		  <el-form-item class="button">
		    <el-button type="primary" @click="submitForm('ruleForm')">立即注册</el-button>
		    <el-button @click="back">取消注册</el-button>
		  </el-form-item>
		</el-form>
	</div>
</template>

<script>
import qs from 'qs'
import axios from 'axios'
export default {
	name:'RegisterBox',
     data() {
          var validatePass = (rule, value, callback) => {
            if (value === '') {
              callback(new Error('请输入密码'));
            } else {
              if (this.ruleForm.checkPass !== '') {
                this.$refs.ruleForm.validateField('checkPass');
              }
              callback();
            }
          };
          var validatePass2 = (rule, value, callback) => {
            if (value === '') {
              callback(new Error('请再次输入密码'));
            } else if (value !== this.ruleForm.password) {
              callback(new Error('两次输入密码不一致!'));
            } else {
              callback();
            }
          };
		  var isMobileNumber= (rule, value, callback) => {
		     if (!value) {
		          return new Error("请输入电话号码");
		        } else {
		          const reg = /^1[3|4|5|7|8][0-9]\d{8}$/;
		          const isPhone = reg.test(value);
		          value = Number(value); //转换为数字
		          if (typeof value === "number" && !isNaN(value)) {//判断是否为数字
		          value = value.toString(); //转换成字符串
		            if (value.length < 0 || value.length > 12 || !isPhone) { //判断是否为11位手机号
		              callback(new Error("手机号码格式如:138xxxx8754"));
		            } else {
		              callback();
		            }
		          } else {
		            callback(new Error("请输入电话号码"));
		          }
		        }
		  };
          return {
            ruleForm: {
			  	name:'',
			  	username: '',
				regionnum: '',
			  	phonenum: '',
			  	capus:'',
			  	dorm:'',
			  	room:'',
              	password: '',
              	checkPass: '',
            },
            rules: {
			  username: [
			    { required: true, message: '请输入用户名', trigger: 'blur' },
			    // { min: 3, max: 5, message: '长度在 3 到 5 个字符', trigger: 'blur' }
			  ],
              password: [
                { validator: validatePass, trigger: 'blur' }
              ],
              checkPass: [
                { validator: validatePass2, trigger: 'blur' }
              ],
				regionnum:[
					{ required: true, message: '号码区号不能为空！', trigger: 'blur' },
				],
			  phonenum: [
			    { required: true, message: '请输入手机号码！', trigger: 'blur' },
				{ validator: isMobileNumber, trigger: "blur" }
			  ],
			  capus: [
			    { required: true, message: '请选择活动区域', trigger: 'change' }
			  ],
			  dorm: [
			    { required: true, message: '宿舍楼号不能为空！', trigger: 'blur' }
			  ],
			  room: [
			    { required: true, message: '宿舍号不能为空！', trigger: 'blur' }
			  ],
            },
			info: null,
			errorMsg1:''
          };
        },
        methods: {
		  checkName() {
		     this.errorMsg1 = ""; //校验前需清空错误信息
		     var checkUser = this.ruleForm.username;
			 console.log("用户名检测：" + checkUser);

			 let params = new URLSearchParams();
			 params.append('username',checkUser);
			 axios.post('http://47.95.11.87/api/register',params)
		  		.then((res)=>{
		  			if(res.data==-1){
		  			    this.errorMsg1 = "用户名已注册！";
		  				console.log("用户校验res", res);					
		  			}
		  		})
		  		.catch(function (error) {
		  			console.log(error);
		  		});

		  },
          submitForm(formName) {
            this.$refs[formName].validate((valid) => {
              if (valid) {
				this.$message({
				    message: '恭喜你，注册成功！',
				    type: 'success'
				});
				axios.post('http://47.95.11.87/api/register',
				 qs.stringify({
					 username: this.ruleForm.username,
					 phonenum: this.ruleForm.regionnum + this.ruleForm.phonenum,
					 capus: this.ruleForm.capus,
					 dorm: this.ruleForm.dorm,
					 room: this.ruleForm.room,
					 password: this.ruleForm.password}))
					 .then(//res => {
				  //       console.log(res);}
				      response=> (this.info = response)
				      ).catch(res => {
				        console.log(res)
				      })
				this.$router.replace('/login')	  
              } else {
                console.log('注册失败！');
                return false;
              }
			  console.log(this.ruleForm.username);
            });
          },
          // resetForm(formName) {
          //   this.$refs[formName].resetFields();
          // }
		  back(){
		  	this.$router.replace('/login')
		  }
        }
  }
</script>

<style>
#register-box{
	margin: 0 auto; /*设置元素所有外边距的宽度 有1-4个值*/
	margin-top: -16%;
	margin-left: 41%;
	text-align: center;
}
#register-box .input{
	width: 25rem;
	padding-left: 0rem;
}
#register-box .choice{
	width: 25rem;
	margin-left: 0.0625rem;
}
#register-box .button{
	width: 33.375rem;
	margin-left: -3rem;
}

#register-box h1{
	text-align: center; 
	margin-bottom: 3.75rem;
	width: 31.25rem;
}
</style>
