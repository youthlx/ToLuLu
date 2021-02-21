# -*- coding:utf-8 -*-
# author xin.luo
import requests


# get请求
def get():
    # get请求的url，header和参数
    r = requests.get('https://www.douban.com/search',
                     headers={'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit'},
                     params={'q':'python', 'cat': '1001'})
    # response对象属性
    # 请求的url
    print(r.url)
    # HTTP请求的返回状态
    print(r.status_code)
    # 从HTTP header中猜测的响应内容编码方式
    print(r.encoding)
    # HTTP响应内容的字符串形式，即url对应的页面内容
    print(r.text)
    # HTTP响应内容的二进制形式
    print(r.content)


# post form请求
def post_form():
    # 使用data参数指定form入参
    r = requests.post('https://accounts.douban.com/login',
                      data={'form_email': 'abc@example.com', 'form_password': '123456'})
    print(r.status_code)


# post json请求
def post_json():
    # 使用json参数指定json入参
    r = requests.post('https://accounts.douban.com/login',
                      json={'form_email': 'abc@example.com', 'form_password': '123456'})
    # response的json响应格式
    print(r.json())


# post上传文件请求
def post_file():
    url = ''
    upload_files = {'file': open('report.xls', 'rb')}
    # 使用files参数指定文件流
    r = requests.post(url, files=upload_files)
    print(r.status_code)


# session
def use_session():
    url = ''
    data = {}
    session = requests.Session()
    r = session.post(url, data=data)
    print(r.status_code)


# cookie
def use_cookie():
    url = ''
    data = {}
    r = requests.post(url, data=data)
    # 使用上一次请求获取的cookies传入
    r1 = requests.post(url, data=data, cookies=r.cookies)
    print(r1.status_code)


# 小贴士

# requests库里的常见异常
# requests.ConnectionError	网络连接错误异常，如DNS查询失败、拒绝连接等
# requests.HTTPError	    HTTP错误异常
# requests.URLRequired	    URL缺失异常
# requests.TooMangRedirects	超过最大重定向次数，产生重定向异常
# requests.ConnectTimeout	连接远程服务器超时异常
# requests.Timeout	        请求URL超时，产生超时异常

# request库的异常捕获
# r.raise_for_status()	    如果不是200，产生异常requests.HTTPError
