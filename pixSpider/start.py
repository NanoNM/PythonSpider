import os,json,random
print("真敢用呗就，梯子架好了没就敢用！！")
print("输入搜索名称")

such = input()
if (os.path.exists(".\\startmat.info")):
    with open('.\\startmat.info', mode='r', encoding='utf-8') as file:
        content = file.read()
        data = json.loads(content)
        Key=data["Key"]
    print("wait")
else:
    randomK1 = random.randint(1,4)
    randomK2 = random.randint(1,5)
    randomK3 = random.choice("WDNMD")
    randomK4 = random.choice("WDNMD")
    Key=str(randomK1)+str(randomK2)+randomK3+randomK4
item={
    "input":such,
    "Key":Key
}
with open('.\\startmat.info', mode='w', encoding='utf-8') as file:
    file.write(json.dumps(item, ensure_ascii=False))
while True:
    main = "spiderServer.exe" #XXX.exe 
    r_v = os.system(main)
    print (r_v)