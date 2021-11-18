# python3.6.5
# 需要引入requests包 ：运行终端->进入python/Scripts ->输入：pip install requests
from 农业数据.ShowapiRequest import ShowapiRequest

r = ShowapiRequest("http://route.showapi.com/2261-3","662836","7ea7286028714960af10da5bfef4294e" )
r.addBodyPara("pro", "广东")
r.addBodyPara("city", "广州")
r.addBodyPara("code", "5bai_hua_cai")
res = r.post()
print(res.text) # 返回信息