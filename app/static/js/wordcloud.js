document.addEventListener("DOMContentLoaded", function () {
    var data = wordcloud_data;

    var wordcloudData = [];
    for (var key in data) {
        wordcloudData.push({
            name: key,
            value: data[key]
        });
    }

    var wordcloudChart = echarts.init(document.getElementById('wordcloud-chart'));

    var option = {
        series: [{
            type: 'wordCloud',
            gridSize: 2,
            sizeRange: [12, 60], // 设置字体大小范围
            rotationRange: [0, 0], // 设置不旋转
            shape: 'circle',
            width: '100%',
            height: '100%',
            drawOutOfBound: false,
            textStyle: {
                normal: {
                    color: function () {
                        return 'rgb(' + [
                            Math.round(Math.random() * 160),
                            Math.round(Math.random() * 160),
                            Math.round(Math.random() * 160)
                        ].join(',') + ')';
                    },
                },
                emphasis: {
                    shadowBlur: 10,
                    shadowColor: '#333',
                },
            },
            data: wordcloudData
        }]
    };

    wordcloudChart.setOption(option);

    wordcloudChart.on('mouseover', function (params) {
        if (params.dataType === 'node') {
            // 在鼠标停留时显示数值
            alert(params.data.value);
        }
    });
});
