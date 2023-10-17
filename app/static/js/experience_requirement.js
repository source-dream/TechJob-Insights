document.addEventListener("DOMContentLoaded", function () {
    // 使用从 HTML 中获取的数据
    var data = experience_data;

    // 将数据转换为适用于玫瑰图的格式
    var roseData = [];
    for (var key in data) {
        roseData.push({
            name: key,
            value: data[key]
        });
    }

    var roseChart = echarts.init(document.getElementById('experience-chart'));

    var option = {
        title: {
            text: '经验需求',
        },
        tooltip: {
            trigger: 'item',
            formatter: '{a} <br/>{b} : {c} ({d}%)'
        },
        series: [
            {
                name: '工作经验',
                type: 'pie',
                radius: '55%',
                center: ['50%', '60%'],
                data: roseData,
                roseType: 'angle',
                label: {
                    show: true,
                    formatter: '{b} : {c} ({d}%)'
                }
            }
        ]
    };

    roseChart.setOption(option);
});
