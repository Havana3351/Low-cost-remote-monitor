import App from '../App'

const main = r => require.ensure([], () => r(require('../page/main')), 'main')
const video = r => require.ensure([], () => r(require('../page/video/video')), 'video')
const temhui = r => require.ensure([], () => r(require('../page/temhui')), 'temhui')
const realtime = r => require.ensure([], () => r(require('../page/video/realtime')), 'video')
const historytime = r => require.ensure([], () => r(require('../page/video/historytime')), 'video')

export default [{
	path: '/',
	component: App, //顶层路由，对应index.html
	children: [ //二级路由。对应App.vue
		//地址为空时跳转页面
		{
		    path: '',
		    redirect: '/main'
		},
		{
		    path: '/main',
		    component: main,
			name: 'main',
			meta: {title: '首页'}
		},
		{
		    path: '/video',
		    component: video,
			name: 'video',
			meta: {title: '视频'},
			children: [
				{
					path: 'realtime',
					component: realtime,
					name: 'realtime',
					meta: {title: '实时视频'},
				},
				{
					path: 'historytime',
					component: historytime,
					name: 'historytime',
					meta: {title: '历史视频'},
				},
			]
		},
		{
		    path: '/temhui',
		    component: temhui,
			name: 'temhui',
			meta: {title: '温湿度'}
		},
	],
}]