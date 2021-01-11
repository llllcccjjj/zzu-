# zzu-签到打卡简易版本（目前支持多账号进行签到，多个账号，多个密码之间利用&分割）
```两个账号例子 S_NAME里面的内容  20177720866&20177720877```
 ```           S_PWD里面的内容   12324567&23434545 ```

## 步骤1：登录pushpius网站拿到token
（1）打开网址 http://pushplus.hxtrip.com/
![image](https://github.com/llllcccjjj/zzu-/blob/main/images/1.png)

（2）点击一对一推送，之后出现微信扫二维码扫描，之后到下面的界面
![image](https://github.com/llllcccjjj/zzu-/blob/main/images/2.png)
拿到自己的Token号复制下来，下面需要用。
## 步骤2：fork项目到自己的账号下，进行修改
（1）点击右上角的fork
![image](https://github.com/llllcccjjj/zzu-/blob/main/images/3.png)
(2)第一栏 选择settings ,左边点击 secret  
![image](https://github.com/llllcccjjj/zzu-/blob/main/images/4.png)
（3）新出现界面右上角点击 New secret 添加PULS_KEY、S_NAME、S_PWD字段，添加结束之后保存。
![image](https://github.com/llllcccjjj/zzu-/blob/main/images/5.png)
将第一步得到的token复制到 PULS_KEY的value里面，点击Add secret
![image](https://github.com/llllcccjjj/zzu-/blob/main/images/6.png)
同理，添加S_NAME、S_PWD字段 value的值分别为你的学号和密码
![image](https://github.com/llllcccjjj/zzu-/blob/main/images/7.png)
## 步骤3：启动action 激活程序
点击上面一栏的action
![image](https://github.com/llllcccjjj/zzu-/blob/main/images/8.png)
此时action可能还未运行，目前的 GitHub Actions 配置的执行触发有 2 个：
1.定时执行
2.推送更新代码执行
这里根据第二点的特性来进行测试。例如编辑 README.md 文档，增加个回车，然后提交，来进行触发。
![image](https://github.com/llllcccjjj/zzu-/blob/main/images/9.png)
![image](https://github.com/llllcccjjj/zzu-/blob/main/images/10.png)
再次返回action，便可以看到程序已经正常启动。结束之后，手机微信绑定的微信公众号将会通知相应的结果。
由于写的比较简单，偶尔会出现BUG，出现问题后只能手动打卡了。
设置定时启动的代码在 ./gitflow里面的.yml文件，使用的是corntab 时间+8:00等于上海时间
想了解更多，可以百度 corntab
![image](https://github.com/llllcccjjj/zzu-/blob/main/images/11.png)


                      
                       
                       
