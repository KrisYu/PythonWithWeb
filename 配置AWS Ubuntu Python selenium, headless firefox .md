### 配置AWS Ubuntu Python selenium, headless firefox 

### 安装pip 和 selenium

```
curl -O https://bootstrap.pypa.io/get-pip.py
sudo python get-pip.py
# Then use pip to install 3rd party libraries
pip install selenium
# works now
```



### 安装firefox xvfb pyvirtualdisplay


```
sudo apt-get -f update
sudo apt-get install firefox xvfb
pip install pyvirtualdisplay
```

别忘了设置

```
export DISPLAY=:99
```


### 测试

```
from pyvirtualdisplay import Display
from selenium import webdriver

display = Display(visible=0, size=(800, 600))
display.start()
driver = webdriver.Chrome()
driver.get('https://google.com')
print driver.title
```

参考：


<http://docs.aws.amazon.com/cli/latest/userguide/installing.html>


<http://www.installationpage.com/selenium/how-to-run-selenium-headless-firefox-in-ubuntu/>


<https://christopher.su/2015/selenium-chromedriver-ubuntu/>


### 本地配置

本地配置其实没什么差，但是发现 firefox 48 和 selenium 不兼容，于是更改到了chrome.

值得注意的是如果是 OS X EI Captioan想用headless chrome的话，需要先安装XQuartz. 至此，两个平台暂且配置完毕，所有的代码两个平台都可以同样跑。









