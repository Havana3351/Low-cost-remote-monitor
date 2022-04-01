<template>
	<div id="show">
		<el-card class="box-card">
			<h2>欢迎 {{username}} 来到 WatchDog 智能宿舍管理系统~</h2>
			<el-divider></el-divider>
			<h3>共享成员：</h3>
			<p>中南大学铁道学院12楼418舍</p>
			<el-avatar :src="url" :size="50" class="bg1"></el-avatar>
			<span>handsomeman</span>
			<el-avatar :src="url" :size="50" class="bg2"></el-avatar>
			<span>handsomewoman</span>
			<el-avatar :src="url" :size="50" class="bg3"></el-avatar>
			<span>handsome</span>
			<br>
			<el-divider></el-divider>
			<h3>设备状态：</h3>
			<el-card class="card1">
			<p class="state1">树莓派：</p>
			<p class="state">恭喜你~你的树莓派状态正常！</p>
			</el-card>
			<el-card class="card2">
			<p class="state1">传感器数据：</p>
			<p class="state2">正常~</p>
			<p class="state1">摄像头：</p>
			<p class="state2">正常~</p>
			</el-card>
			<el-card class="card3">
			<p class="state1">湿度传感器：</p>
			<p class="state2">正常~</p>
			<p class="state1">温度传感器：</p>
			<p class="state2">正常~</p>
			</el-card>
		</el-card>
	</div>
</template>

<script>
import {getCookie} from "../cookie.js"
import bgurl from "../assets/images/login.jpg"

export default {
	data(){
		return{
			url: bgurl,
			username:getCookie("username")
		}
	}
}
</script>

<style>
#show .box-card {
    width: 70.25rem;
	margin-left: 17.25rem;
	margin-top: -0.8rem;
	border-color: cadetblue;
}
#show .box-card h2 {
    margin-left: 12rem;
}
#show .box-card .bg1{
	margin-left: 2.25rem;
	margin-top: 1rem;
}
#show .box-card .bg2{
	margin-left: 6.25rem;
}
#show .box-card .bg3{
	margin-left: 8.25rem;
}
#show .box-card span{
	cursor: pointer;
	font-size: 1.3125rem;
}
#show .box-card .username {
    font-size: 1.5rem;
	margin-bottom: 3.125rem;
	margin-left: 5.25rem;
}
#show .box-card .state{
	font-size: 1.9rem;
	margin-left: 0.8rem;
	margin-top: 0.5rem;
	color: #3f8cfa;
}
#show .box-card .state1{
	font-size: 1.2rem;
	margin-left: 1rem;
	margin-top: 0.5rem;
}
#show .box-card .state2{
	font-size: 1.9rem;
	margin-left: 6rem;
	color: #3f8cfa;
}
#show .box-card .card1{
	width: 20rem;
	height: 20.5rem;
	margin-left: 2rem;
}
#show .box-card .card2{
	width: 20rem;
	height: 20.5rem;
	margin-left: 23.5rem;
	margin-top: -20.5rem;
}
#show .box-card .card3{
	width: 20rem;
	height: 20.5rem;
	margin-left: 45.25rem;
	margin-top: -20.5rem;
}
</style>
