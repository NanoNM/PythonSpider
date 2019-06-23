# -*- coding:utf-8 -*-
# created by Nanometer
# design by 傻逼群友 看你妈的P站 我又买不到会员
# first edited: 2019.1.12
# THX FOR USE MY CORD
# 版本Ver.1.0 完成时间 2019.1.14   4.12
# 版本Ver.1.1 完成时间 2019.1.14   6.00
# 免责声明
'''

请勿将本程序永远商业用途！
请勿将本程序永远商业用途！
请勿将本程序永远商业用途！

出事我不负责 一点责任都没有 国安局来找你 那是你的事 你非法卖图那是你的事 这个别找我

制作者QQ 270884295

'''
'''
新版本特性 增加设置文件 自动生成用户文件
增加代码长度 让我看起来比较NB
注释代码 我下个版本更好修复BUG
'''
'''
=============================================================================================== 
 NNNNNNN       NNN                
 NNNNNNNNN     NNN               
 NNNN  NNNN                      
 NNNN   NNN                      
 NNNN   NNN                      
 NNNN   NNN    NNN    NNNN  NNN  
 NNNN  NNN     NNN     NNNNNNN   
 NNNNNNNNN     NNN      NNNNNN   
 NNNN          NNN       NNNN    
 NNNN          NNN       NNNN    
 NNNN          NNN      NNNNN    
 NNNN          NNN     NNNNNNN   
 NNNN          NNN     NNN  NNN  
 NNNN          NNN    NNN   NNNN 
===============================================================================================                                                                                             
 NNNN  NNNN                                                                                   
 NNNN  NNNN                                                                                   
 NNNN  NNNN                                                      NNNN                         
 NNNNN NNNN                                                      NNNN                         
 NNNNN NNNN                                                      NNNN                         
 NNNNNNNNNN   NNNNNN  NNNNNNNNN   NNNNNN   NNNNNNNNNN  NNNNNN  NNNNNNNNN    NNNNNN   NNNNNNNN 
 NNNNNNNNNN  NNN  NNN NNNNN NNN  NNN NNNN  NNNNNNNNNN NNN  NNN   NNNN      NNN  NNN  NNNNNN   
 NNNNNNNNNN  N    NNN NNNN  NNNNNNNN  NNNN NNNNNNNNNNNNN   NNN   NNNN     NNN   NNN  NNNN     
 NNN NNNNNN     NNNNN NNNN  NNNNNNN    NNN NNNNNN NNNNNNNNNNNNN  NNNN     NNNNNNNNNN NNNN     
 NNN NNNNNN  NNNNNNNN NNN   NNNNNNN    NNN NNNNNN NNNNNN         NNNN     NNN        NNN      
 NNN  NNNNN NNN   NNN NNN   NNNNNNN    NNN NNNNNN NNNNNN         NNNN     NNN        NNN      
 NNN  NNNNN NNN  NNNN NNN   NNNNNNNN  NNN  NNNNNN NNNNNNN  NNN    NNN     NNNN  NNN  NNN      
 NNN   NNNN NNNNNNNNN NNN   NNNN NNNNNNNN  NNNNNN NNN NNNNNNNN    NNNNNN   NNNNNNNN  NNN      
 NNN   NNNN   NNNNNNNNNNN   NNNN   NNNN    NNNNNN NNN   NNNN       NNNNN     NNNN    NNN      

=============================================================================================== 																			                                   
'''
'''
    模块包
'''
import requests, json, os, time, re, random
from http.cookiejar import CookieJar
from bs4 import BeautifulSoup

'''
    定义全局变量和方法 文件识别定义用户名和登录密码等待模拟登陆
'''
print("真敢用呗就，梯子架好了没就敢用！！")
print("输入搜索名称")
such = input()
se = requests.session()
pagenum = 1
if (os.path.exists(".\\setting.ini")):
    with open('setting.ini', 'r', encoding='utf-8') as file:
        content = file.read()
        data = json.loads(content)
else:
    if (os.path.exists(".\\setting.ini")):
        with open('setting.ini', 'r', encoding='utf-8') as file:
            content = file.read()
        data = json.loads(content)
    else:
        item = {
            "WarningWarningWarning": "Do not use non-English characters",
            "projectName": "setting",
            "Page": "0",
            "UID": "***@***.com",
            "Passworld": "******",
            "SavePath": "*:\\*\\*",
            "PLS_REMOVE_PLS_REMOVE_PLS_REMOVE": "SCremove",
            "minilikenum": "0"
        }
        with open('.\\setting.ini', mode='w', encoding='utf-8') as file:
            file.write(json.dumps(item, ensure_ascii=False))
        with open('setting.ini', 'r', encoding='utf-8') as file:
            content = file.read()
            data = json.loads(content)
while (data["PLS_REMOVE_PLS_REMOVE_PLS_REMOVE"] == "SCremove"):
    print("您还没有输入自己的用户名和密码输入到设置中请打开软件文件夹下的setting.ini文件进行编辑")
    print("编辑完成后请将""PLS_REMOVE_PLS_REMOVE_PLS_REMOVE"''"后的"'SCremov'"删除")
    print("错误的用户名和密码会导致程序崩溃 修改用户名或密码后重启既可 注意文件目录中不允许出现非英文字符")
    print("回车键继续")
    input()
allpage = data["Page"]
PIXIV_ID = data["UID"]
Passworld = data["Passworld"]
load_path = data["SavePath"]
minilikenum = data["minilikenum"]


class Pixiv():
    '''
    内部变量 定义登录网址 爬取网址 头文件 并定义用户ID和密码以及图片保存位置
    '''

    def __init__(self):
        self.base_url = 'https://accounts.pixiv.net/login?lang=zh&source=pc&view_type=page&ref=wwwtop_accounts_index'
        self.login_url = 'https://accounts.pixiv.net/api/login?lang=zh'
        self.target_url = 'https://www.pixiv.net/search.php?word=%s&order=date_d&p=' % such
        self.main_url = 'http://www.pixiv.net'
        self.headers = {
            'Referer': 'https://accounts.pixiv.net/login?lang=zh&source=pc&view_type=page&ref=wwwtop_accounts_index',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) '
                          'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'}
        self.pixiv_id = PIXIV_ID
        self.password = Passworld
        self.post_key = []
        self.return_to = 'http://www.pixiv.net/'
        self.load_path = load_path
        self.ip_list = []

    '''
        登录模块 登录获取并分析出图片的ID
    '''

    def login(self):
        se.cookies = CookieJar()
        post_key_html = se.get(self.base_url, headers=self.headers).text
        post_key_soup = BeautifulSoup(post_key_html, 'lxml')
        self.post_key = post_key_soup.find('input')['value']
        # 上面是去捕获postkey
        data = {
            'pixiv_id': self.pixiv_id,
            'password': self.password,
            'return_to': self.return_to,
            'post_key': self.post_key
        }
        se.post(self.login_url, data=data, headers=self.headers)
        self.target_url = self.target_url + str(pagenum)
        print(self.target_url)
        html = se.get(self.target_url).text
        '''
            清理字符
        '''
        ImageIDALL = re.findall(
            r'<section id="js-react-search-mid"></section><input type="hidden"id="js-mount-point-search-result-list"data-items="\[(.*?)\]"data-related-tags=',
            html, re.S)[0]
        ImageIDALL2 = ImageIDALL.replace('&quot;', '"')
        ImageIDALL3 = ImageIDALL2.replace('/', '')
        ImageIDALL4 = ImageIDALL3.replace('[', '')
        ImageIDALL5 = ImageIDALL4.replace(']', '')
        ImageIDlist = re.findall(r'"illustId":"(.*?)","illustTitle"', ImageIDALL5, re.S)
        LIMLIST = len(ImageIDlist)
        char = (-1)
        '''
            拼合图片地址
        '''
        for ImageID in ImageIDlist:
            ImageID = ImageIDlist[char]
            print(ImageID)
            self.GotImageUrl(ImageID)
            if char < LIMLIST:
                char = char + 1
            else:
                self.login()
        print(ImageIDlist)

    def GotImageUrl(self, ImageID):
        ImageUrl = "https://www.pixiv.net/member_illust.php?mode=medium&illust_id=" + ImageID
        print(ImageUrl)
        self.AnalysisImage(ImageUrl, ImageID)

    def AnalysisImage(self, ImageUrl, ImageID):
        self.headers['Referer'] = ImageUrl
        html = se.get(ImageUrl, headers=self.headers).text
        likenum = re.findall(r'"bookmarkCount":(.*?),"likeCount"', html, re.S)[0]
        # print(likenum)
        if int(likenum) > int(minilikenum):
            print("检测到合适文件进行跳转")
            self.Shibie(ImageUrl, ImageID)
        else:
            print("未满足点赞人数，识别下一张")
        print(likenum)

    def Shibie(self, ImageUrl, ImageID):

        print("为您下载")
        ImageUrl = ImageUrl
        html = se.get(ImageUrl, headers=self.headers).text
        html = html.replace('\\', '')
        info = re.findall(r'}\)\((.*?)\);</script>', html, re.S)[0]
        with open('log.wjmbhjb', mode='w') as pic:
            pic.write(info)
        with open("log.wjmbhjb", 'r') as f:
            temp = f.readlines()[0]
            likenum = re.findall(r'"pageCount":(.*?),"', temp, re.S)[0]
            Pagedata = \
                re.findall(r'"small":"https://i.pximg.net/c/540x540_70/img-master/img(.*?)","regular"', temp, re.S)[0]
            Title = re.findall(r'"illustTitle":"(.*?)"', html, re.S)[0]
            UserID = re.findall(r'"authorId":"(.*?)"', html, re.S)[0]
            TitleASCLL = Title.replace('u', '\\u')
            page = "https://i.pximg.net/img-master/img" + Pagedata
            self.Xiazai(page, TitleASCLL, UserID, ImageID)
            print(Pagedata)
        print("理论成功")

    def Xiazai(self, page, TitleASCLL, UserID, ImageID):
        print(page)
        self.headers['Referer'] = page
        PIC = requests.get(page, headers=self.headers)
        if os.path.exists(such):
            print("OKK")
        else:
            os.makedirs(such)
        with open('.\\%s\\%s %s.jpg' % (such, ImageID, UserID), mode='wb') as pic:
            pic.write(PIC.content)

    def work(self):
        self.login()


'''
    调用函数 启动程序
'''
while True:
    pixiv = Pixiv()
    pixiv.work()
    time.sleep(3)
    pagenum = pagenum + 1
    if pagenum == (int(allpage) + 1):
        break