### 用Screen保持脚本一直跑

然后因为我的脚本非常初级和简单，我就让我的脚本用一般的傻方法的来大概五分钟执行一次。


原来我一断开ssh就不会跑的原因是进程也断了。

所以需要用到screen，还有需要安全退出，用exit，来试试。


装screen

```
sudo apt-get install screen
```


敲

```
screen
python dps.py
```


然后 ctrl + a + d 就退出了这个screen.


```
screen -ls
```


output

```
There is a screen on:
       	4486.pts-0.ip-172-31-54-207    	(08/25/2016 02:33:38 PM)       	(Detached)
```

敲

```
screen -r 4486
```


看到还在继续运行

然后用exit来close connection.

五分钟后，再看一下：

screen还在
