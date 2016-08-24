###.bash_profile


这个文件主要是放配置用的东西，当我在自己的

```
open .bash_profile
```

天，内容

是这些

```

# added by Anaconda3 2.4.1 installer
export PATH="//anaconda/bin:$PATH"

# added by Anaconda3 2.4.1 installer
export PATH="//anaconda/bin:$PATH"
-e 
export PATH=//anaconda/bin://anaconda/bin:/usr/local/bin:/usr/bin:/bin:/usr/sbin:/sbin:/usr/local/mysql/bin

# added by Anaconda2 4.0.0 installer
export PATH="//anaconda/bin:$PATH"

# added by Anaconda3 4.0.0 installer
export PATH="//anaconda/bin:$PATH"


# added by Xue Yu for sox
export PATH=$PATH:/Applications/sox-14.4.2
```

终于，anaconda删干净也要删这里

问题出在使用sublime text3 跑python 报两个错

加了这个之后第一个错解决


```
PATH=$PATH:~/bin
export PATH
```


第二个跑出来的东西


```
/bin/bash: shell_session_update: command not found

```

依旧在，根据网上的解决方案没有解决

