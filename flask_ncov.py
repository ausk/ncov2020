# 2020/02/15 by ausk
# 从百度疫情获取数据，并使用 flask 搭建后台。

"""
# 使用 Flask + ECharts 实现疫情展示。
1)从疫情网站抓取疫情数据，保存为离线数据；
2) 启动 flask 后台，可实时更新数据祸加载离线数据，然后以 json 格式返回查询数据；同时返回渲染的网页。
3) 编写 html 页面，前台(浏览器)通过 ajax 请求指定路由异步加载数据，绘制疫情地图和疫情趋势图。
"""
from flask import Flask, render_template, jsonify
from baidu_ncov import update, query

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False

## 注册 flask 路由
@app.route('/<fname>.html')
def hello(fname):
    return render_template(fname+".html")

## 主页
@app.route('/')
def index():
    return render_template('flask_ncov.html')

# 更新
@app.route("/update", methods=["GET"])
def update_data():
    data = update()
    return jsonify(data)

# 查询确诊
@app.route("/query_confirm", methods=["GET"])
def query_confirm():
    data = query("confirm")
    return jsonify(data)

# 查询趋势
@app.route("/query_trend", methods=["GET"])
def query_trend():
    data = query("trend")
    return jsonify(data)

if __name__ == '__main__':
    update()
    app.run(debug=False)
