# -*- coding: utf-8 -*-
"""
Created on Sat Nov 21 16:06:37 2020

@author: Sewcary
"""


from instapy_cli import client
username = 'faraniang' #your username
password = 'Nourou27!' #your password 
image = '1.jpg' #here you can put the image directory
text = 'Here you can put your caption for the post' + '\r\n' + 'you can also put your hashtags #pythondeveloper #webdeveloper'
with client(username, password) as cli:
    cli.upload(image, text)