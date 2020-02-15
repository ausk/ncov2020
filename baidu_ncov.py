# 2020/02/15 by ausk
# 从百度疫情获取数据。

import re, json
import requests
import time

DATA_PATH = "static/data/flask_ncov.json"
DATA_PATH_NEW = "static/data/flask_ncov_new.json"

# (1) 更新数据
def update():
    url = "https://voice.baidu.com/act/newpneumonia/newpneumonia/"
    headers = {
        "User-Agent":"User-Agent Mozilla/5.0 (Win64; x64; rv:69.0) Firefox/69.0",
        "host": "voice.baidu.com",
        "origin":"https://voice.baidu.com",
        "referer":"https://voice.baidu.com"
    }

    qdata = {}
    qdata["status"]  = 400

    sess = requests.Session()

    try:
        resp = sess.get(url, headers=headers)
        if resp.status_code !=200:
            return jsonify({"status": 404})
        data = resp.text
        pat = re.compile("V.conf = (.*?);")
        lst = pat.findall(data)
        res = json.loads(lst[0])
        component = res["component"][0]

        # 每个省市确诊人数
        caseList = component["caseList"]
        confirm = [{"name": x["area"], "value": int(x["confirmed"])} for x in caseList]

        # 趋势
        trend = component["trend"]

        # 保存信息
        qdata["confirm"] = confirm
        qdata["trend"]   = trend
        qdata["status"]  = 200
        qdata["time"] = time.strftime("%Y/%m/%d %H:%M:%S", time.localtime())

        with open(DATA_PATH_NEW, "w", encoding="utf-8") as fout:
            fout.write(json.dumps(qdata))
    except Exception as exc:
        print("Exception: {}".format( exc ))

    return qdata

# (2) 查询数据
def query(key="confirm"):
    qdata = {}
    qdata["status"] = 400
    if key not in ("confirm", "trend"):
        qdata["msg"] = "Unknown query key: {}".format(key)
    else:
        try:
            qdata["status"] = 200
            try:
                with open(DATA_PATH_NEW, "r", encoding = "utf-8") as fin:
                    data = json.loads(fin.read())
            except:
                with open(DATA_PATH, "r", encoding = "utf-8") as fin:
                    data = json.loads(fin.read())

            qdata[key] = data.get(key, None)
            qdata["msg"] = "Successful"
        except Exception as exc:
            print("Exception: {}".format(exc))
            qdata["msg"] = "Internal error!"
    return qdata

if __name__ == "__main__":
    update()
    confirm = query("confirm")
    trend = query("trend")