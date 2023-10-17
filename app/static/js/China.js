        var map = L.map('map', {
            center: [35.8617, 104.1954], // 设置地图初始中心点
            zoom: 4, // 设置初始缩放级别
            zoomControl: false, // 隐藏缩放控制按钮
            dragging: false, // 禁用地图拖动
            tap: false // 禁用地图上的点击事件
        });
        map.scrollWheelZoom.disable();
        map.touchZoom.disable();
        map.doubleClickZoom.disable();
        // 禁用所有点击事件
        map.boxZoom.disable(); // 禁用拖拽框缩放
        map.doubleClickZoom.disable(); // 禁用双击缩放
        map.keyboard.disable(); // 禁用键盘控制
        map.scrollWheelZoom.disable(); // 禁用滚轮缩放
        map.tap && map.tap.disable(); // 禁用触摸设备的点击

        // 禁用地图点击事件（单击和双击）
        map.off('click');
        map.off('dblclick');

        fetch('https://geo.datav.aliyun.com/areas_v3/bound/geojson?code=100000_full')
            .then(function(response) {
                return response.json();
            })
            .then(function(data) {
                var geojsonLayer = L.geoJSON(data, {
            onEachFeature: function(feature, layer) {
                // 添加点击事件处理程序
                // layer.on('click', function() {
                //     // 在点击时，放大到选中城市的边界
                //     map.fitBounds(layer.getBounds());
                // });

                // 添加悬浮效果
                layer.on('mouseover', function() {
                    // 在鼠标悬停时添加效果，例如改变颜色、边界等
                    layer.setStyle({
                        fillColor: 'yellow',
                        weight: 2,
                        opacity: 1
                    });
                });

                // 移除悬浮效果
                layer.on('mouseout', function() {
                    // 在鼠标移出时恢复默认样式
                    geojsonLayer.resetStyle(layer);
                });

                // 将城市名称添加为标签
                if (feature.properties && feature.properties.name) {
                    layer.bindTooltip(feature.properties.name, { permanent: false, direction: 'top' });
                }
            }
        }).addTo(map);
            });