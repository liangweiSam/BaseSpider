# -*- coding:utf-8 -*-
import random
import base64
from Crypto.Cipher import AES
import rsa
import binascii
import re
import requests
import json

def getStr(amount):
	b = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
	c = ""
	for x in range(0, int(amount)):
		e = random.random() * len(b)
		e = int(e)
		c+= b[e]
	return c


def getEncText(a, b):
	BS = AES.block_size
	pad = lambda s: s + (BS - len(s) % BS) * chr(BS - len(s) % BS)
	a = pad(a)
	
	text = a.encode('utf-8')
	key = b.encode('utf-8')
	iv = '0102030405060708'.encode('utf-8')
	cryptor = AES.new(key, AES.MODE_CBC, iv = iv)
	ciphertext = cryptor.encrypt(text)
	return base64.b64encode(ciphertext)


def rsaEncrypt(text):
	pubkey = '010001'
	modulus = '00e0b509f6259df8642dbc35662901477df22677ec152b5ff68ace615bb7b725152b3ab17a876aea8a5aa76d2e417629ec4ee341f56135fccf695280104e0312ecbda92557c93870114af6c9d05c4f7f0c3685b7a46bee255932575cce10b424d813cfe4875d3e82047b97ddef52741d546b8e289dc6935b3ece0462db0a22b8e7'
	text2 = text[::-1]
	# biFromHex函数就是把明文反转
	# ** 代表 幂运算
	# RSA 算法 text ** p mod m
	rs = int(binascii.hexlify(text2.encode('utf-8')), 16)**int(pubkey, 16)%int(modulus, 16)
	print(int(binascii.hexlify(text2.encode('utf-8')), 16))
	print(binascii.hexlify(text2.encode('utf-8')))
	print(binascii.hexlify(text.encode('utf-8')))
	# rs = int(binascii.hexlify(text.encode('utf-8')), 16)**int(pubkey, 16)%int(modulus, 16)
	return format(rs, 'x').zfill(256)

def getMp3(params, encSecKey):
	headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.104 Safari/537.36 Core/1.53.4843.400 QQBrowser/9.7.13021.400',
			'Referer' : 'http://music.163.com/',
			'Range' : 'bytes=0-'
			}
	data = {
			'params' : params,
			'encSecKey' : encSecKey
	}
	response = requests.post('http://music.163.com/weapi/song/enhance/player/url?csrf_token=', data=data, headers=headers)
	jsonData = json.loads(response.text)
	mp3Url = jsonData['data'][0]['url']
	print(mp3Url)
	mp3Content = requests.get('http://m10.music.126.net/20180408120049/ba32e4768092aa3973635780aa6e1f89/ymusic/681e/45fc/220f/083f3b9525df5ded32f7d84f1ffbc895.mp3', headers=headers)
	with open('1.mp3', 'wb') as f:
		f.write(mp3Content.content)


if __name__ == '__main__':
	i = getStr(16)
	firstText = str(getEncText('{"ids":"[27955653]","br":128000,"csrf_token":""}', '0CoJUm6Qyw8W8jud'), 'utf-8')
	encText = str(getEncText(firstText, 'HYrEPZUIFTgfMT6W'), 'utf-8')
	encSecKey = rsaEncrypt('y59d51SonxqqIy2C')
	# text = 'HYrEPZUIFTgfMT6W'
	# print(2**5)
	# getMp3(encText, encSecKey)











