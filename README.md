# ncov2020

本项目参考了[丁香园肺炎疫情](https://ncov.dxy.cn/ncovh5/view/pneumonia)、[阿里健康肺炎疫情](https://alihealth.taobao.com/medicalhealth/influenzamap)、[百度肺炎疫情](https://voice.baidu.com/act/newpneumonia/newpneumonia)等，最后选用百度疫情作为数据源，按自己的方式呈现疫情地图和趋势图，以了解疫情现状和趋势。使用 Python 采集、使用 JavaScript echarts 绘制 2020 年新型肺炎疫情地图和趋势图。

数据来源自“[百度-新型冠状病毒疫情实时大数据报告](https://voice.baidu.com/act/newpneumonia/newpneumonia/)”

原理：

1. 数据获取：使用 Python 采集百度疫情报告，解析疫情数据。
2. 数据展示：使用 Python Flask 作为服务端，编写 html 文件，采用百度 JavaScript 库 echarts 绘制疫情地图和趋势，渲染展示为网页。


安装依赖库：

```bash
python -m pip install requests flask
```

启动 flask 服务(默认端口 5000)：

```bash
python flask_ncov.py
```

浏览器中查看

```bash
# 主页
http://127.0.0.1:5000
# 更新
http://127.0.0.1:5000/update
```


![疫情状态](https://github.com/ausk/ncov2020/raw/master/ncov.png)
