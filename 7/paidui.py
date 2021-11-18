import requests
key={'Authorization': 'MTYwODYwMjAwODpkZjAyZDliZDcwMDQyZjczY2M4NTIzZjU4NDIyNzMzODpjYjU2ZTU1YzcyNmM0YTg1YThlMTY2Y2VmZTAxYmE3OA=='}
header={'Accept': 'application/json, text/plain, */*',
'Accept-Encoding': 'gzip, deflate',
'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.6,en;q=0.5;q=0.4',
 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.116 Safari/537.36 QBCore/4.0.1278.400 QQBrowser/9.0.2524.400 Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2875.116 Safari/537.36 NetType/WIFI MicroMessenger/7.0.5 WindowsWechat'
       }
url = 'http://2ndclass.eqclub.cn/wechat/activity/sign_up/activity/bba137d3185440f0871a8cf4440b4c5b/role/1/user/af900b7d198b11e98bbe00163e085cb1 HTTP/1.1'
post = requests.post(url,data=key,headers=header)
print(post)