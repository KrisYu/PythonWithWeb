###试用Shell

前几天看了两个shell相关的脚本，感觉还是很方便的。

写一个傻shell，定期删文件：

```
deleteLog.sh

#!/bin/bash  

cd /home/ubuntu
rm log

```

然后每天crontab里面定时删
 
crontab -e

```
50 12 * * * /home/pythonicScripts/deleteLog
```