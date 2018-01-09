# spiderStudy
## 记录自己学习python的文件夹
#### 第一个问题
    import requests
    url = 'https://www.toutiao.com/search_content/?offset=0&format=json&keyword=%E8%A1%97%E6%8B%8D&autoload=true&count=20&cur_tab=3&from=gallery'
    response = requests.get(url)
    response.text
    这个网址在chrome里面得到的信息要比程序跑代码多。用word粘贴下来，直接用chrome打开是30页，用jupyter或者vscode都是27页。少了部分内容，完全不知道是什么原因
