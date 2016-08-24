### AWS 我的常见操作


连接 

```
ssh -i ~/.ssh/AWSKey.pem ubuntu@54.226.105.14
```


scp上传文件

```
scp -i ~/.ssh/AWSKey.pem ~/Pythonic/dps.py ubuntu@54.226.105.14:/home/ubuntu/pythonScripts
```

断开SSH连接

速度稍慢
```
~.
```

后台跑脚本

```
run your files in the background (with '&' at the end or use nohup)
python xx.py &
```

这个时候，它会给你一个号


```
ubuntu    1304  0.0  1.2  44396 12976 pts/0    S    00:17   0:00 python dps.py
```

but 奇怪的是今天去看pib 的那个没了，是我代码的原因还是进程的原因to be more 研究

tobe - fix 貌似我代码的原因，用的第三方的库我可能没搞明白


看所有正在跑的进程

```
ps aux | less
```





