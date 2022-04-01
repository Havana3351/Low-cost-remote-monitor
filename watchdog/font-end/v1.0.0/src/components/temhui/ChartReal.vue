<template>
  <div id="chartElem">
      <highcharts class="chart" :options="chartOptionsReal" :updateArgs="updateArgs"></highcharts>
  </div>
</template>

<script>
import store from "../../store";
import {getCookie} from "../../cookie";
import axios from 'axios'

export default {
  data () {
    return {
      title: '',
      points: [10, 0, 8, 2, 6, 4, 5, 5],
      chartType: 'Spline',
      seriesColor: '#00a8e1',
      colorInputIsSupported: null,
      animationDuration: 1000,
      updateArgs: [true, true, {duration: 1000}],

        chartOptionsReal: {
            chart: {
                type: 'spline',
                events: {
                    load: function () {
                        // set up the updating of the chart each second
                        var series1 = this.series[0];
                        var series2 = this.series[1];
                        setInterval(function () {
                            var username = getCookie('username');
                            axios({
                                method: 'post',
                                url: 'http://47.95.11.87/api/sensors',
                                data: {
                                    username: username
                                }
                            })
                                .then(function (response){
                                    console.log(response.data);
                                    if(response != null){
                                        store.commit('temhui/setTempReal',response.data.Temp);
                                        store.commit('temhui/setHumiReal',response.data.Humi);
                                        var x1 = (new Date()).getTime(), // current time
                                            y1 = response.data.Temp;
                                        var x2 = (new Date()).getTime(),
                                            y2 = response.data.Humi;
                                        series1.addPoint([x1, y1], true, true);
                                        series2.addPoint([x2, y2], true, true);
                                        console.log(store.state.temhui.humiReal);
                                        console.log(store.state.temhui.tempReal);
                                    }
                                })
                                .catch(function (error) { // 请求失败处理
                                    console.log(error);
                                });
                        }, 3000);
                    }
                }
            },
            title: {
                text: '实时温湿度'
            },
            time: {
                useUTC: false
            },

            accessibility: {
                announceNewData: {
                    enabled: true,
                    minAnnounceInterval: 15000,
                    announcementFormatter: function (allSeries, newSeries, newPoint) {
                        if (newPoint) {
                            return 'New point added. Value: ' + newPoint.y;
                        }
                        return false;
                    }
                }
            },
            xAxis:{
                type: 'datetime',
                tickPixelInterval: 150,
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
                {
                    yAxis: 0,
                    name: "温度",
                    data:  (function () {
                        // generate an array of random data
                        var data = [],
                            time = (new Date()).getTime(),
                            i;

                        for (i = -19; i <= 0; i += 1) {
                            data.push({
                                x: time + i * 1000,
                                y: Math.floor((Math.random()*100)+1),
                            });
                        }
                        return data;
                    }()),
                    color: '#3f8cfa',
                    tooltip: {
                        valueSuffix: ' °C'
                    }
                },
                {
                    yAxis: 1,
                    name: "湿度",
                    data: (function () {
                        // generate an array of random data
                        var data = [],
                            time = (new Date()).getTime(),
                            i;

                        for (i = -19; i <= 0; i += 1) {
                            data.push({
                                x: time + i * 1000,
                                y: Math.floor((Math.random()*100)+1),
                            });
                        }
                        return data;
                    }()),
                    color: '#fe377d',
                    tooltip: {
                        valueSuffix: ' %RH'
                    }
                }
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
        }
    }
  },
    methods:{
      loaddata(){

      }
    },
  created () {
    let i = document.createElement('input')
    i.setAttribute('type', 'color');
    (i.type === 'color') ? this.colorInputIsSupported = true : this.colorInputIsSupported = false
  },
  watch: {
    title (newValue) {
      this.chartOptions.title.text = newValue
    },
    points (newValue) {
      this.chartOptions.series[0].data = newValue
    },
    chartType (newValue) {
      this.chartOptions.chart.type = newValue.toLowerCase()
    },
    seriesColor (newValue) {
      this.chartOptions.series[0].color = newValue.toLowerCase()
    },
    animationDuration (newValue) {
      this.updateArgs[2].duration = Number(newValue)
    }
  },
    computed:{
        chartOptions: function(){
            return store.state.temhui.chartOptionsReal;
        }
    }
}
</script>

<style scoped>
input[type="color"]::-webkit-color-swatch-wrapper {
  padding: 0;
}
#colorPicker {
  border: 0;
  padding: 0;
  margin: 0;
  width: 30px;
  height: 30px;
}
.numberInput {
  width: 30px;
}
#chartElem{
	min-width:400px;
	height:400px;
}
</style>
