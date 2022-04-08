import getpass

#获取系统用户名-
username = getpass.getuser()

#---------修改此处----------
fileurl="C:/Users/"+username+"/AppData/Roaming/.minecraft/logs/latest.log" #如果你使用了第三方PVP客户端(Blclient),启用了版本隔离或修改了默认路径,您需要修改该路径;若是原版,Forge或Optfine,则无需修改
saveurl="D:/1.txt" #格式化完毕后文本的保存路径,可自行修改,请提前创建指定文件

#重要:要将路径中的\换为/,否侧python可能无法识别

#---------下方没有需要修改的地方---------

with open(fileurl,"r") as f:    #设置文件对象
    text=f.read()

#分割文本
text_list=text.split("\n")
#获取文本行数
lennumber=len(text_list)

all_chat=''

i=0

while i<lennumber:   

    if '[CHAT]' in text_list[i]:
        
        print(i+1)

        time=text_list[i].split(" ",1)[0]


        nowlisttext=text_list[i].split(": ",1)[1]

        if nowlisttext=='[CHAT]':
            print("")
        else:
            nowchat=nowlisttext.split(" ",1)[1]
            all_chat=all_chat+time+' '+nowchat+"\n"

        i=i+1
    else:
        nowlen=text_list[i]
        if "java.util.concurrent.ExecutionException:" not in nowlen and "Caused by: java.lang" not in nowlen and "	... 9 more" not in nowlen:
            if "[" not in nowlen:
                all_chat=all_chat+nowlen+"\n"
        i=i+1


    



#删除all_chat的最后一行
all_chat=all_chat[:-1]

#获取文本行数

#使用回车分割
all_chat_list=all_chat.split("\n")

all_chat_len=len(all_chat_list)


print("-----Successful----")
print('--Info--')
print("All rows:"+str(lennumber))
print("chat rows:"+str(all_chat_len))
print('--Chat--')
print(all_chat)

abclist=list(map(chr,range(ord('a'),ord('z')+1)))
numlist=list(map(chr,range(ord('0'),ord('9')+1)))

i=0
while i<36:
    if i<26:
        sym=abclist[i]
    else:
        sym=numlist[i-26]
    i=i+1
    all_chat= all_chat.replace('§'+sym,'')


with open(saveurl,"w") as f:
    f.write(all_chat)


