document.addEventListener("DOMContentLoaded", function () {
    // 使用从 HTML 中获取的数据
    var data = job_data;

    // 将数据转换为适用于条形统计图的格式
    var labels = Object.keys(data);
    var counts = Object.values(data);

    var barChart = echarts.init(document.getElementById('job-chart'));

    var option = {
        title: {
            text: '职位统计',
        },
        tooltip: {
            trigger: 'axis',
            axisPointer: {
                type: 'shadow'
            }
        },
        xAxis: {
            type: 'category',
            data: labels
        },
        yAxis: {
            type: 'value'
        },
        dataZoom: [ // 添加数据视图滑动条
            {
                type: 'slider',
                show: true,
                xAxisIndex: [0],
                start: 0,
                end: 100
            }
        ],
        series: [
            {
                name: '数量',
                type: 'bar',
                data: counts
            }
        ]
    };

    barChart.setOption(option);
});
