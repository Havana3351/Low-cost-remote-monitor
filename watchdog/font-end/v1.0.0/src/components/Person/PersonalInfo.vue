<template>
	<div id="personal-info">
		<div class="table">
		  <h1>个人信息</h1>
		  <el-table
			:data="tableData1"
			stripe
			style="width : 30.375rem;">
			<el-table-column
			  label="Information"
			  prop="information">
			</el-table-column>
			<el-table-column
			  label="Content"
			  prop="content">
			</el-table-column>
			<el-table-column
				align="right">
				  <template slot-scope="scope">
					<div class="edit" @click="handleEdit(scope.$index, scope.row)">
					  <i class="el-icon-edit" ></i>
					</div>
				  </template>
			</el-table-column>
		  </el-table>
			<el-popover
					placement="top"
					width="160"
					v-model="visible">
				<p>确定更新您的信息嘛？</p>
				<div style="text-align: right; margin: 0">
					<el-button size="mini" type="text" >取消</el-button>
					<el-button type="primary" size="mini" @click="updatePersonal">确定</el-button>
				</div>
				<el-button class="save" slot="reference" type="warning">保 存</el-button>
			</el-popover>
		  <el-button
		    class="exit"
		    type="primary"
		    plain
		    @click="handleExit">返 回</el-button>
		</div>
	  <div :style="bgImg" class="background"></div>
	</div>
</template>

<script>
	import store from '../../store/index.js'

export default {
	name:'PersonalInfo',
    data() {
      return {
        search: '',
		bgImg: {
		    //backgroundImage: "url(" + require("../assets/images/bb.jpg") + ")",
		    //backgroundRepeat: "no-repeat",
		    //backgroundSize: "1450px 850px",
		},

      }
    },
	computed:{
		tableData1: function(){
			return store.getters["personal/getPersonalTab"];
		}
	},
    methods: {
      handleEdit(index, row) {
        console.log(index, row);
		if(index == 0){
			this.$alert('用户名不可修改！', '警告', {
			          confirmButtonText: '确定',
			          callback: action => {
			            this.$message({
			              type: 'info',
			              message: `action: ${ action }`
			            });
			          }
			      });
		}else if(index == 1){
			this.$prompt('请输入新的电话号码：', '提示', {
			          confirmButtonText: '确定',
			          cancelButtonText: '取消',
			          inputPattern: /^1[3|4|5|7|8][0-9]\d{8}$/,
			          inputErrorMessage: '电话号码格式不正确'
			    }).then(({ value }) => {
			    	  store.commit('personal/setPersonalPhone1',value);
			          this.$message({
			          type: 'success',
			          message: ' 修改成功，记得保存哟~ '
			        });
			    }).catch(() => {
			          this.$message({
			            type: 'info',
			            message: '取消输入'
			    });
			});
		}else if(index == 2){
			this.$prompt('请输入新的所属校区：', '提示', {
			          confirmButtonText: '确定',
			          cancelButtonText: '取消',
			    }).then(({ value }) => {
					  store.commit('personal/setPersonalCom1',value);
			          this.$message({
			          type: 'success',
			          message: ' 修改成功，记得保存哟~ '
			        });
			    }).catch(() => {
			          this.$message({
			            type: 'info',
			            message: '取消输入'
					  });
				});
		}else if(index == 3){
			this.$prompt('请输入新的宿舍楼号：', '提示', {
			          confirmButtonText: '确定',
			          cancelButtonText: '取消',
			    }).then(({ value }) => {
					  store.commit('personal/setPersonalSsl1',value);
			          this.$message({
			          type: 'success',
			          message: ' 修改成功，记得保存哟~ '
			        });
			    }).catch(() => {
			          this.$message({
			            type: 'info',
			            message: '取消输入'
			    });
			});
		}else if(index == 4){
			this.$prompt('请输入新的寝室号：', '提示', {
			          confirmButtonText: '确定',
			          cancelButtonText: '取消',
			    }).then(({ value }) => {
					  store.commit('personal/setPersonalSsh1',value);
			          this.$message({
			          type: 'success',
			          message: ' 修改成功，记得保存哟~ '
			        });
			    }).catch(() => {
			          this.$message({
			            type: 'info',
			            message: '取消输入'
			    });
			});
		}else if(index == 5){
			this.$prompt('请输入新的视频源号：', '提示', {
				confirmButtonText: '确定',
				cancelButtonText: '取消',
			}).then(({ value }) => {
				store.commit('personal/setPersonalVideo1',value);
				this.$message({
					type: 'success',
					message: ' 修改成功，记得保存哟~ '
				});
			}).catch(() => {
				this.$message({
					type: 'info',
					message: '取消输入'
				});
			});
		}else if(index == 6){
			this.$prompt('请输入新的温度源号：', '提示', {
				confirmButtonText: '确定',
				cancelButtonText: '取消',
			}).then(({ value }) => {
				store.commit('personal/setPersonalTemp1',value);
				this.$message({
					type: 'success',
					message: ' 修改成功，记得保存哟~ '
				});
			}).catch(() => {
				this.$message({
					type: 'info',
					message: '取消输入'
				});
			});
		}else if(index == 7){
			this.$prompt('请输入新的温度源号：', '提示', {
				confirmButtonText: '确定',
				cancelButtonText: '取消',
			}).then(({ value }) => {
				store.commit('personal/setPersonalHumi1',value);
				this.$message({
					type: 'success',
					message: ' 修改成功，记得保存哟~ '
				});
			}).catch(() => {
				this.$message({
					type: 'info',
					message: '取消输入'
				});
			});
		}

      },
      handleSave(index, row) {
        console.log(index, row);
      },
	  handleExit(){
		this.$router.replace('/main')
	  },
		updatePersonal(){
      		var username = store.state.personal.personalName.content;
      		var phonenum = store.state.personal.personalPhone.content;
      		var campus = store.state.personal.personalCom.content;
      		var dorm = store.state.personal.personalSsl.content;
      		var room = store.state.personal.personalSsh.content;
      		var temp = store.state.personal.personalTemp.content;
      		var humi = store.state.personal.personalHumi.content;
      		var video = store.state.personal.personalVideo.content;
			this.$axios({
				method: 'post',
				url: 'http://47.95.11.87/api/profile',
				data: {
					username: username,
					phonenum: phonenum,
					campus: campus,
					dorm: dorm,
					room: room,
					temp: temp,
					humi: humi,
					video: video
				}
			})
					.then(response=> (this.info = response))
					.catch(function (error) { // 请求失败处理
						console.log(error);});
		}
    },
  }
</script>

<style>
#personal-info .table{
	margin: 0 auto; /*设置元素所有外边距的宽度 有1-4个值*/
	margin-top: 0%;
	margin-left: 40%;
	text-align: center;
	z-index:1;
	position: absolute;
}
#personal-info .background{
    height: 85%;
	width: 100%;
	z-index:-1;
    position: absolute;	
	opacity: 0.8;
}
#personal-info .table .save{
	padding: 0.625rem 2.1875rem;
	margin: 3.25rem 5.125rem 3.125rem 6.25rem;
}
#personal-info .table .exit{
	padding: 0.625rem 2.1875rem;
	margin: 3.25rem 5.125rem 3.125rem 0rem;
}
</style>
