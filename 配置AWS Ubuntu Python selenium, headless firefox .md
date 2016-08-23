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

### 测试

```
from pyvirtualdisplay import Display
from selenium import webdriver

display = Display(visible=0, size=(800, 600))
display.start()
driver = webdriver.Firefox()
driver.get('https://google.com')
print driver.title
```

参考：


<http://docs.aws.amazon.com/cli/latest/userguide/installing.html>


<http://www.installationpage.com/selenium/how-to-run-selenium-headless-firefox-in-ubuntu/>


<https://christopher.su/2015/selenium-chromedriver-ubuntu/>








