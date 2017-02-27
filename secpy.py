#!/usr/bin/python  
# -*- conding:utf-8 -*-  

from bottle import *  # 导入bottle相关的包
var1='{"code":"0","error":"","body":{"datalist":[{"title":"美食城","lon":"30.679879","lat":"104.064855","world":"中国第一火锅"},{"title":"绝味火火","lon":"31.238068","lat":"121.501654","world":"宇宙第一川味"},{"title":"老友粉","lon":"34.341568","lat":"108.940174","world":"微辣最为合适"},{"title":"游乐场","lon":"34.7466","lat":"113.625367","world":"绝不出意外儿童娱乐场所"}]}}'

@route('/getgd/:yourwords', methods=['GET', 'POST'])  # url接口，注意参数书写格式，前面有个冒号表示是参数
def hello(yourwords):
    if yourwords == 'getjson':
        return var1
    else:
        return 'nothing '
    #return 'hello world. ' + yourwords  # 返回前台数据，此处返回一个字符串


run(host='0.0.0.0', port=8080)  # 表示本机，接口是8080


{
	"code": 0,
	"error": "",
	"body": {
		"datalist": [
			{
				"title": "美味",
				"lon": "222",
				"lat": "111",
				"world": "要不要来个鸳鸯戏水呢",
			},
		],
	}
}

