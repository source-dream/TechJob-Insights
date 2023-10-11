// 提取数据中的标签和计数
var labels = Object.keys(education_data);
var counts = Object.values(education_data);

// 为每个条形分配不同颜色
var colors = ['#c70e63', '#FF6347', '#32CD32', '#3e138c', '#FFA07A', '#87CEEB', '#F08080','#3398DB'];

// 创建ECharts实例
var myChart = echarts.init(document.getElementById('education-chart'));

// 配置项
var option = {
    title: {
        text: '学历需求'
    },
    color: colors, // 分配的颜色数组
    tooltip: {},
    xAxis: {
        data: labels,
        axisLabel: {
            interval: 0, // 使标签全部显示
            rotate: 45, // 旋转标签，适应较长的标签
        }
    },
    yAxis: {},
    series: [{
        name: '人数',
        type: 'bar',
        data: counts
    }]
};

// 使用刚指定的配置项和数据显示图表。
myChart.setOption(option);

// 添加缩放功能
myChart.on('dblclick', function (params) {
    // 实现缩放
    var option = myChart.getOption();
    var yAxisMax = option.yAxis[0].max;
    if (yAxisMax === null) {
        option.yAxis[0].max = 2 * Math.max(...counts); // 双击时放大
    } else {
        option.yAxis[0].max = null; // 再次双击时还原
    }
    myChart.setOption(option);
});
