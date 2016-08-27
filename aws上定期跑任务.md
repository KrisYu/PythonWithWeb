### AWS上用Cron定期跑Python脚本

#### *nix上默认装有cron，可以定期跑脚本

不过先需要给python设置环境变量,弄个最简单的脚本来测试

注意第一行

```
#!/usr/local/bin/python


def hello():
	file = open("test.txt","a")
	file.write("hello world\n")
	file.close()



if __name__ == '__main__':
	hello()
```

然后让文件可执行

```
chmod +x cronTest.py
```


#### 写crontab文件


```
crontab -e 
```

每分钟执行一次

```
*/1 * * * * /usr/bin/python /home/ubuntu/pythonScripts/cronTest.py

*/5 * * * * /usr/bin/python /home/ubuntu/pythonScripts/dps.py

```

开始静候

注意这个可能直接吧test.txt放到根目录下了 -> 煞笔的我迷茫了半天


所以开始定期自己的App了

偷个图

```
* * * * * command to be executed
- - - - -
| | | | |
| | | | ----- Day of week (0 - 7) (Sunday=0 or 7)
| | | ------- Month (1 - 12)
| | --------- Day of month (1 - 31)
| ----------- Hour (0 - 23)
------------- Minute (0 - 59)
```


静候两分钟， done √
👍


参考

<https://segmentfault.com/q/1010000000654014>

