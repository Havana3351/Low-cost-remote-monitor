<template>
	<div id="temhui">
		<div>
			<p>温度：</p>
			<p v-for="data in info">{{data.Temp}}</p>
		</div>
		<div>
			<p>湿度：</p>
			<p v-for="data in info">{{data.Humi}}</p>
		</div>
		<van-button type="info" @click="readData" :style="{top: '100px' }">
			点击获取数据
		</van-button>
		<div>
			<van-button plain type="primary" @click="returnPage" :style="{top: '130px' }">
				点击返回主页
			</van-button>
		</div>
		
	</div>
</template>

<script>
	export default {
	  name: 'temhui',
	  data() {
		  return{
			 info : null,
		  }
	  },
	  methods:{
		readData: function(){
			this.$axios
			.get('http://47.95.11.87/api/data')
			.then(response=> (this.info = response))
			.catch(function (error) { // 请求失败处理
			        console.log(error);
			});
		},
		returnPage: function(){
			this.$router.replace('/home')
		}
	  }
	}
</script>

<style>
	#temhui {
		font-family: 'Avenir', Helvetica, Arial, sans-serif;
		-webkit-font-smoothing: antialiased;
		-moz-osx-font-smoothing: grayscale;
		text-align: center;
		color: #2c3e50;
		margin-top: 60px;
	}
</style>
