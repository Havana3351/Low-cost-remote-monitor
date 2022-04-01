import App from '../App'

const login = r => require.ensure([], () => r(require('../page/LoginReg/Login')), 'login')
const register = r => require.ensure([], () => r(require('../page/LoginReg/Register')), 'login')
const main = r => require.ensure([], () => r(require('../page/main')), 'login')
const video = r => require.ensure([], () => r(require('../page/video/video')), 'video')
const temhuireal = r => require.ensure([], () => r(require('../page/temhui/temhuireal')), 'temhui')
const temhuiHis = r => require.ensure([], () => r(require('../page/temhui/temhuiHis')), 'temhui')
const realtime = r => require.ensure([], () => r(require('../page/video/realtime')), 'video')
const historytime = r => require.ensure([], () => r(require('../page/video/historytime')), 'video')
const personal = r => require.ensure([], () => r(require('../page/Personal/personalInfo')), 'personal')

export default [{
	path: '/',
	component: App, //顶层路由，对应index.html
	children: [ //二级路由。对应App.vue
		//地址为空时跳转页面
		{
		    path: '',
		    redirect: '/login'
		},
		//登陆页面
		{
			path: '/login',
			component: login
		},
		//注册界面
		{
			path:'/register',
			component: register
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
		    path: '/temhuireal',
		    component: temhuireal,
			name: 'temhuireal',
			meta: {title: '当前温湿度'}
		},
		{
			path: '/temhuiHis',
			component: temhuiHis,
			name: 'temhuiHis',
			meta: {title: '历史温湿度'}
		},
		{
			path: '/personal',
			component: personal,
			name: 'personal',
			meta: {title: '个人信息'}
		},
	],
}]