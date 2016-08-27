### SSH -v 显示nodename nor servname provided, or not known



中午准备连接的时候，发现SSH报错

```
aws ssh_exchange_identification: read: Connection reset by peer
```


然后查询了一下，发现蛮多人有这个问题

所以用

```
ssh -v ~/.ssh/AWSKey.pem ubuntu@54.226.105.14



Verbose mode.  Causes ssh to print debugging messages about its
             progress.  This is helpful in debugging connection, authentica-
             tion, and configuration problems.  Multiple -v options increase
             the verbosity.  The maximum is 3.


```



看了一下具体的，报错


```
nodename nor servname provided, or not known
```

用别人的方法，换了一个port进去

```
ssh -i ~/.ssh/AWSKey.pem ubuntu@54.226.105.14 -p 22
```

原因有待更仔细的研究，记录以防止下一次继续的产生
