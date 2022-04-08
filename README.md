# Minecraft 日志解析聊天脚本
### 是使用Minecraft登录游玩服务器或单人游戏时,游戏会向 C:\Users\您的系统用户名\AppData\Roaming\.minecraft\logs 文件夹中实时写入最新的游戏日志(latest.log),此日志文件通常包含: 系统配置,游戏运行情况,聊天内容,服务器系统通知 等内容.
#### 因为写入的内容非常杂乱,且服务器聊天内容一般带有颜色代码(类似于:§a),会使得日志可读性下降
#### 本脚本可以帮助用户删除聊天内容中的颜色代码,并输出经格式化的,删除了多余内容的日志
### ❗本脚本需手动修改日志文件路径及格式化后日志文件保存路径

## 对比图:
![解析前](https://cdn.jsdelivr.net/gh/linglaoda/imgs@master/imgs/202204081542286.png)
> 解析前:可读性低,内容混杂

![解析后](https://cdn.jsdelivr.net/gh/linglaoda/imgs@master/imgs/202204081548848.png)
> 解析后:可读性高,清晰明了
