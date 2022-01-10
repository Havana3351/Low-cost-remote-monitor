<template>
	<div>
		<div id="Picker">
			<DatePicker id="DatePicker"></DatePicker>
			<TimePicker id="TimePicker"></TimePicker>
		</div>
		<hr style="background-color: snow; border:none;">
		<div id="TableDiv">
			<Table id="Table"></Table>
			<VideoCard id="VideoCard"></VideoCard>
		</div>
	</div>
</template>

<script>
	import NavMenu from '../../components/NavMenu.vue'
	import DatePicker from '../../components/video/DatePicker.vue'
	import Table from '../../components/video/Table.vue'
	import TimePicker from '../../components/video/TimePicker.vue'
	import VideoCard from '../../components/video/VideoCardHistory.vue'
	import Breadcrumb from '../../components/Breadcrumb.vue'
	
	export default{
		components: {
		  NavMenu,
		  DatePicker,
		  Table,
		  TimePicker,
		  VideoCard,
		  Breadcrumb
		},
	}
</script>

<style>
	#DatePicker{
		margin-top: 5px;
		margin-left: 80px;
		float: left;
	}
	#TimePicker{
		float: left;
		margin-top: -40px;
		margin-left: 700px;
	}
	#Table{
		margin-top: 100px;
		margin-left: 80px;
		box-shadow: 0 2px 4px rgba(0, 0, 0, .12), 0 0 6px rgba(0, 0, 0, .04)
	}
	#VideoCard{
		width: 105%;
		margin-top: -109px;
		margin-left: 820px;
	}
	#TableDiv{
		margin-top: -20px;
		margin-left: -40px;
	}
</style>
