import yagmail
import socket
import json
import requests
import re
import time
def send_mail(config_json, file_path):
    # ### JSON file example
    # {
    #     "user": "xxxx@qq.com",
    #     "password": "xxxxxx",
    #     "receivers": ["xxxxx@xxx",... ]
    # }
    with open(config_json, 'r', encoding='utf8')as fp:
        config = json.load(fp)
    receivers = config['receivers']   #要接收邮件的邮箱
    user = config['user']   #要发送邮件的邮箱，可以自己发送给自己
    password = config['password']   #授权码
    # filepath = "data/2021-04-28/covid-2021-04-28 15:40:29.html" #要发送的附件
    filename = file_path.split('/')[-1].split('.')[0]
    subject = "Please check the attachment -- {}".format(filename)
    host_name = socket.gethostname()

    text = requests.get("http://txt.go.sohu.com/ip/soip").text
    ip = re.findall(r'\d+.\d+.\d+.\d+', text)[0]
    # ip = socket.gethostbyname(host_name)
    body = filename + ' from {} {}'.format(host_name, ip)

    yag = yagmail.SMTP(
        user=user,
        password=password,
        host='smtp.qq.com')

    ### custom logic start
    today = int(time.strftime("%w"))
    tmp_receivers = []
    if today in [1,3,5]:
        tmp_receivers.append(receivers[0])
    elif today in [2, 4, 7]:
        tmp_receivers.append(receivers[2])
        tmp_receivers.append(receivers[0])
    elif today == 6:
        tmp_receivers.append(receivers[1])
        tmp_receivers.append(receivers[0])
    receivers = tmp_receivers
    ### custom logic ends

    for receiver in receivers:
        yag.send(to=receiver,
                 subject=subject,
                 contents=body,
                 attachments=file_path)
    print('-----------------  Email has been sent ------------------')