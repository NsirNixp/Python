# _*_ coding:utf-8 _*_
# 实现客户端和服务端逻辑，通过套接字从服务器传输任意文件到客户端
# 使用一个简单的控制信息协议，而不是单独的套接字，用于控制和数据(如在ftp上)
# 分派没个客户端请求到一个线程处理，通过分块，循环传输整个文件


import sys, os, time
import thread
from socket import *

blksz = 1024
defhost = 'localhost'
defport = 50001

helptext = """
usage...
server=>getfile.py -mod serve  [-port nnn] [-host hhh|localhost]
client=>getfile.py [-mode client] -file fff [-port nnn] [-host hhh|localhost]
"""

def now():
	return time.asctime()


def parsecomandline():
	dict = {}
	args = sys.argv[1:]
	while len(args) >= 2:
		dict[args[0]] = args[1]
		args = args[2:]
	return dict

def client(host, port, filename):
	sock = socket()
	sock.connect((host,	post))
	sock.send((filename + '\n').encode())
	dropdir = os.path.split(filename)[1]
	file = open(dropdir, 'wb')
	while True:
		data = sock.recv(1024)
		if not data:
			break
		file.write(data)

	sock.close()
	file.close()
	print 'client got' ,filename, 'at' ,now()

def serverthread(clientsock):
	sockfile = clientsock.makefile('r')
	filename = sockfile.readline()[:-1]
	try:
		file = open(filename, 'rb')
		while True:
			byts = file.read(blksz)
			if not byts:
				break
			sent = clientsock.sent(byts)
			assert sent == len(byts)
	except:
		print 'error downloading file on server', filename
	clientsock.close()

def server(host, port):
	serversock = socket()
	serversock.bind((host, port))
	serversock.listen()

	while True:
		cliensock, addr = serversock.accept()
		print 'server connect by', addr ,'at', now()
		thread.start_new_thread(serverthread, (cliensock,))

def main(args):
	host = args.get('-host', defhost)
	port = int(args.get('-port', defport))
	if args.get('-mode') == 'server':
		if host == 'localhost':
			host = ''
		server(host, port)
	elif args.get('-file'):
		client(host, port, args['-file'])
	else:
		print helptext

if __name__ == '__main__':
	args = parsecomandline()
	main(args)
