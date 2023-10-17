document.addEventListener("DOMContentLoaded", function () {
    // 使用从 HTML 中获取的数据
    var data = city_data;

    // 将数据转换为适用于气泡图的格式
    var bubbleData = [];
    for (var city in data) {
        var randomX = Math.random() * 100; // 随机X坐标
        var randomY = Math.random() * 100; // 随机Y坐标
        var randomSize = data[city] * 0.2; // 数值越大气泡越大

        bubbleData.push([randomX, randomY, randomSize, city]);
    }

    var bubbleChart = echarts.init(document.getElementById('city-chart'));

    var option = {
    title: {
        text: '城市分布',
        subtext: '气泡图示例'
    },
    xAxis: {
        show: false // 取消横坐标显示
    },
    yAxis: {
        show: false // 取消纵坐标显示
    },
    series: [
        {
            type: 'scatter',
            data: bubbleData,
            symbolSize: function (data) {
                return data[2]; // 设置气泡大小
            },
            label: {
                show: true,
                formatter: function (data) {
                    return data.value[3]; // 显示城市名
                },
                position: 'right', // 标签位置
                emphasis: {
                    show: true
                }
            },
            labelLayout: {
                moveOverlap: 'shiftY'
            },
            avoidLabelOverlap: true // 避免标签重叠
        }
    ]
};


    bubbleChart.setOption(option);
});
