
const state = {
    chartOptionsHIS: {
        chart: {
            type: 'spline',
            animation: {
                duration: 1000
            }
        },
        title: {
            text: '历史温湿度'
        },
        xAxis:{
            title:{
                text:'时间'
            }
        },
        yAxis: [{ // Primary yAxis
            labels: {
                format: '{value}°C',
            },
            title: {
                text: '温度',
            },
            plotLines:[{
                color:'red',           //线的颜色，定义为红色
                dashStyle:'solid',     //默认值，这里定义为实线
                value:40,               //定义在那个值上显示标示线，这里是在x轴上刻度为3的值处垂直化一条线
                width:2                //标示线的宽度，2px
            }]
        }, { // Secondary yAxis
            title: {
                text: '降雨量',
            },
            labels: {
                format: '{value} %RH',
            },
            opposite: true
        }],
        legend: {
            layout: 'vertical',
            align: 'left',
            x: 120,
            verticalAlign: 'top',
            y: 100,
            floating: true,
        },
        series: [

        ],
        tooltip: {
            xDateFormat: '%Y-%m-%d',
            shared: true,
            crosshairs: true,
            animation: true,               // 是否启用动画效果
            style: {                      // 文字内容相关样式
                fontSize: "12px",
                fontWeight: "blod",
                fontFamily: "Courir new"
            }
        },
    },
    tempReal: 50,
    humiReal: 50
}

const mutations = {
    setTemHuiHis(state, TemHuiHis){
        state.chartOptionsHIS.series = TemHuiHis;
    },
    setTempReal(state, TempReal){
        state.tempReal =TempReal;
    },
    setHumiReal(state,HumiReal){
        state.humiReal = HumiReal;
    }
}

const getters = {

}


export default {
    namespaced: true,
    state,
    getters,
    mutations
}