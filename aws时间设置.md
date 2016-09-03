### AWS Ubuntu时间设置

##### 1看看美国有哪些城市可用



```
ls /usr/share/zoneinfo/America
```

再谷歌了一下，Dallas和Chicago时区一样



##### 2 更改

```
sudo timedatectl set-timezone America/New_York
```


这个时间

```
date 
```
发现已经成功更改

保险起见，还是reboot了一下


参考：
 <http://askubuntu.com/questions/323131/setting-timezone-from-terminal>