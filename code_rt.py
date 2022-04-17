import getpass
from time import sleep
import os


#获取系统用户名-
username = getpass.getuser()

#---------修改此处----------
fileurl="C:/Users/"+username+"/AppData/Roaming/.minecraft/logs/blclient/minecraft/latest.log" #如果你使用了第三方PVP客户端(Blclient),启用了版本隔离或修改了默认路径,您需要修改该路径;若是原版,Forge或Optfine,则无需修改
saveurl="E:/Desktop/minecraft/1.txt" #格式化完毕后文本的保存路径,可自行修改,请提前创建指定文件

#重要:要将路径中的\换为/,否侧python可能无法识别

#---------下方没有需要修改的地方---------


with open(fileurl,"r") as f:    #读取日志文件
    textlen=len(f.read().split("\n"))

i=textlen-1


aftertime=''

while True:  #通过最后修改时间判断是否需要更新

    nowtime=str(os.path.getmtime(fileurl))

    if nowtime!=aftertime: #时间不一致,需要更新

        with open(fileurl,"r") as f:    #读取日志文件
            text=f.read()[:-1]

        #分割文本
        text_list=text.split("\n")
        #获取文本行数
        lennumber=len(text_list)

        all_chat=''

    

        while i<lennumber:   

            if '[CHAT]' in text_list[i]:
        
                #print(i+1)

                time=text_list[i].split(" ",1)[0]


                nowlisttext=text_list[i].split(": ",1)[1]

                if nowlisttext=='[CHAT]':
                    print("")
                else:
                    nowchat=nowlisttext.split(" ",1)[1]

                    if ': ' in nowchat:
                
                        abclist=list(map(chr,range(ord('a'),ord('z')+1)))
                        numlist=list(map(chr,range(ord('0'),ord('9')+1)))

                        nowchat=nowlisttext.split(": ",1)[0].split(' ',1)[1]+' : '+nowchat.split(': ',1)[1]
                        

                        a=0
                        while a<36:
                            if a<26:
                                sym=abclist[a]
                            else:
                                sym=numlist[a-26]
                            a=a+1
                            nowchat= nowchat.replace('§'+sym,'')


                        
                        print('---')
                        print('当前读取行:'+str(i))

                        print(nowchat)






            i=i+1
    else:
        print('没有新日志')


    aftertime=nowtime #更新时间

    sleep(2)

    
