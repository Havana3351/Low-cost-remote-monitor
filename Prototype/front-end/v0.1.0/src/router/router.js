import App from '../App'

const temhui = r => require.ensure([], () => r(require('../page/temhui')), 'temhui')
const video = r => require.ensure([], () => r(require('../page/video')), 'video')
const home = r => require.ensure([], () => r(require('../page/home')), 'home')


export default [{
	path: '/',
	component: App, //顶层路由，对应index.html
	children: [ //二级路由。对应App.vue
		//地址为空时跳转temhui页面
		{
		    path: '',
		    redirect: '/home'
		},
		//温湿度页面
		{
		    path: '/temhui',
		    component: temhui
		},
		//视频流页面
		{
			path: '/video',
			component: video
		},
		//视频流页面
		{
			path: '/home',
			component: home
		}
	],
}]