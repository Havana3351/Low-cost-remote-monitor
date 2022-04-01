<template>
	<div>
		<div>
			<NavMenu></NavMenu>
			<Breadcrumb id="Breadcrumb"></Breadcrumb>
			<Avatar id="Avatar"></Avatar>
			<el-divider id="divider1"></el-divider>
		</div>
		<div id="backgroudDiv">
			<div id="temhmiDiv">
				<el-card id="temCard">
					<p style="text-align: left; font-size: large" >实时温度：</p>
					<p style="text-align: center; font-size: xx-large; color: #fe377d" >{{tempReal + '°C'}}</p>
				</el-card>
				<el-card id="hmiCard">
					<p style="text-align: left; font-size: large" >实时湿度：</p>
					<p style="text-align: center; font-size: xx-large; color: #3f8cfa" >{{humiReal + '%RH'}}</p>
				</el-card>
			</div>
			<div id="ChartRealDiv">
				<el-card id="Chart">
					<ChartReal></ChartReal>
				</el-card>
			</div>
		</div>
	</div>
</template>

<script>
	import NavMenu from '../../components/NavMenu.vue'
	import Breadcrumb from '../../components/Breadcrumb.vue'
	import Avatar from "../../components/Avatar";
	import ChartReal from "../../components/temhui/ChartReal";
	import store from '../../store/index.js'
	import {getCookie} from '../../cookie.js'
	
	export default{
		components: {
		  	NavMenu,
		  	Breadcrumb,
			Avatar,
			ChartReal,
			store
		},
		computed: {
			tempReal: function () {
				return store.state.temhui.tempReal;
			},
			humiReal: function () {
				return store.state.temhui.humiReal;
			}
		}
	}
</script>

<style>
	#Breadcrumb{
		margin-top: 20px;
		margin-left: 300px;
	}
	#divider1{
		width: 86%;
		margin-top: 11px;
		margin-left: 244px;
	}
	#Avatar {
		margin-left: 93%;
		margin-top: -27px;
	}
	#backgroudDiv{
		background-color: #eceef1;
		height: 710px;
		margin-top: -1.7%;
	}
	#ChartRealDiv{
		width: 70%;
		margin-left: 23%;
		margin-top: 17%;
		position: absolute;
	}
	#Chart{
		width: 100%;
	}
	#temCard{
		width: 30%;
		margin-left: 23%;
		margin-top: 1.9%;
		float: left;
		background-color: #ffffff;
	}
	#hmiCard{
		width: 30%;
		margin-left: 63.8%;
		margin-top: -12.5%;
		float: left;
	}
</style>
