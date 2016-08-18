#coding=gbk 
#Developed by Snooze, 2014-12-18
import requests
import re
import time
####
username = "~~~~~~"
password =  "~~~~~~"
blabla = 'Little hand one shake, big rice arrive hand.' #your blabla here
###


def login():
  #get cookie
  login_data = {'username': username, 
    'password': password, 
    'quickforward': 'yes', 
    'handlekey': 'ls'}
  while True:
    try:
      r = requests.post("http://www.1point3acres.com/bbs/member.php?mod=logging&action=login&loginsubmit=yes&infloat=yes&lssubmit=yes&inajax=1",
        data = login_data)
      break;
    except Exception as ex:
      print(Exception,":",ex)
      time.sleep(1)
  my_cookies = r.cookies
  
  #find the odd WTF "formhash"
  while True:
    try:
      r = requests.post("http://www.1point3acres.com/bbs/",
        cookies = my_cookies)
      break
    except Exception as ex:
      print(Exception,":",ex)
      time.sleep(1)    
  pattern = b'formhash=.*?&'
  formhash = re.findall(pattern,r.content,re.S)[0][9:17]
  my_info = (my_cookies, formhash)
  
  return my_info

  
def sign(cookies, formhash):
  #SIGN NOW!
  sign_data = {'formhash': formhash, 
    'qdxq': 'fd', 
    'qdmode': '1', 
    'todaysay': blabla,
    'fastreply': '0'}
  #while True:
  try:
    r = requests.post("http://www.1point3acres.com/bbs/plugin.php?id=dsu_paulsign:sign&operation=qiandao&infloat=1&sign_as=1&inajax=1",
      data = sign_data,
      cookies = cookies)
    #break
  except Exception as ex:
    print(Exception,":",ex)
    #time.sleep(1)
      
  if "ÂÜ²·" in r.content:
    print('Successfully signed! -3-')
    return False
  else:
    print('Failed! - -#')
    return True
  
my_info = login()
sign(my_info[0],my_info[1])

