# -*- coding:utf-8 -*-
# created by Nanometer
# design by 傻逼群友 看你妈的P站 我又买不到会员
# first edited: 2019.1.12
# THX FOR USE MY CORD
# 版本Ver.1.0 完成时间 2019.1.14   4.12
# 版本Ver.1.1 完成时间 2019.1.14   6.00
# 版本Ver.1.2 完成时间 2019.1.15
# 版本Ver.1.3 完成时间 2019.1.15   5.32
# 版本Ver.2.0 完成时间 2019.1.15   7.10
# 版本Ver.2.1 完成时间 2019.1.15   8.55
# 版本Ver.2.2 完成时间 2019.1.15   9.50
# 版本Ver.2.2.1 完成时间 2019.1.18   10.43
# 免责声明

import requests, json, os, re, time
from http.cookiejar import CookieJar
from bs4 import BeautifulSoup

'''
    定义全局变量和方法 文件识别定义用户名和登录密码等待模拟登陆
'''
with open('.\\startmat.info', 'r', encoding='utf-8') as file:
    content = file.read()
    inputname = json.loads(content)
inputname=inputname["input"]
such = inputname
data={"input":""}
if (os.path.exists(".\\断点续传日志\\%s.info" % such)):
    with open('.\\断点续传日志\\%s.info' % such, 'r', encoding='utf-8') as file:
        content = file.read()
        data = json.loads(content)
if such==data["input"]:
    print("检测到来自%s的断点续传文件我们将从第%s" % (data["input"],data["page"]), "为您继续下载关于%s的图片" % data["input"])
    such = data["input"]
    se = requests.session()
    pagenum = data["page"]
else:
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
        ImageID=ImageID

    def GotImageUrl(self, ImageID):
        ImageUrl = "https://www.pixiv.net/member_illust.php?mode=medium&illust_id=" + ImageID
        print(ImageUrl)
        self.AnalysisImage(ImageUrl, ImageID)

    def AnalysisImage(self, ImageUrl, ImageID):
        self.headers['Referer'] = ImageUrl
        try:
            html = se.get(ImageUrl, headers=self.headers).text
            likenum = re.findall(r'"bookmarkCount":(.*?),"likeCount"', html, re.S)[0]
            # print(likenum)
            if int(likenum) > int(minilikenum):
                print("检测到合适文件进行跳转")
                self.Shibie(ImageUrl, ImageID)
            else:
                print("未满足点赞人数，识别下一张")
            print(likenum)
        except requests.exceptions.ConnectionError as e:
            print(e)

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
            if temp.find("ugoira") == -1:
                Pagedataall = \
                re.findall(r'"small":"https://i.pximg.net/c/540x540_70/img-master/img(.*?)_p0_(.*?)","regular"', temp,re.S)[0]
                Pagedata = Pagedataall[0]
                PagedataGeshi = Pagedataall[1]
                print(Pagedata)
                print(PagedataGeshi)
                Title = re.findall(r'"illustTitle":"(.*?)"', html, re.S)[0]
                UserID = re.findall(r'"authorId":"(.*?)"', html, re.S)[0]
                TitleASCLL = Title.replace('u', '\\u')
                self.Xiazai(Pagedata, TitleASCLL, UserID, ImageID, PagedataGeshi)
                print(Pagedata)
                print("动图暂时无法下载")
            else:
                print("动图暂时无法下载")
                time.sleep
        print("理论成功")

    def Xiazai(self, Pagedata, TitleASCLL, UserID, ImageID, PagedataGeshi):
        number=0
        PIC=""
        while str(PIC) != "<Response [404]>":
            page = "https://i.pximg.net/img-master/img" + Pagedata + "_p"+str(number)+"_" + PagedataGeshi
            print(page)
            print(PIC)
            self.headers['Referer'] = page
            PIC = requests.get(page, headers=self.headers)
            print("已保存%s" % str(int(number) + 1),"张图片")
            if os.path.exists(such):
                print("OKK")
            else:
                os.makedirs(such)
            with open('.\\%s\\%s %s %s.jpg' % (such, ImageID, UserID, 'P'+str(number)), mode='wb') as pic:
                pic.write(PIC.content)
            number = number+1
            page = "https://i.pximg.net/img-master/img" + Pagedata + "_p" + str(number) + "_" + PagedataGeshi
            PIC = requests.get(page, headers=self.headers)
    def work(self):
        self.login()


'''
    调用函数 启动程序
'''
while True:
    pixiv = Pixiv()
    pixiv.work()
    pagenum = pagenum + 1
    Page= {"page":pagenum,
           "input":such}
    zifu=os.path.exists('断点续传日志')
    print(zifu)
    if(zifu==False):
        os.makedirs("断点续传日志")
    with open('.\\断点续传日志\\%s.info' % such, 'w', encoding='utf-8') as file:
        file.write(json.dumps(Page, ensure_ascii=False))
    if pagenum == (int(allpage) + 1):
        break