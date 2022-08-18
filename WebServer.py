# -*- coding = utf-8 -*-
# @Time : 2021/10/21 16:16
# @Author:Yu
# @File: WebServer.py
# @Software: PyCharm

from multiprocessing import Process
from threading import Thread
import re
import socket
import sys

host = "127.0.0.1"
HTML_ROOT = "./"

def handleRequest(tcpSocket):
	"""
	handle the request of client
	:param tcpSocket:
	:return:
	"""
	# 1. Receive request message from the client on connection socket
	message = tcpSocket.recv(1024)
	print("request message:", message)

	# 2. Extract the path of the requested object from the message
	requestLine = message.splitlines()
	#7for line in requestLine:
	#	print(line)
	requestStartLine = requestLine[0]

	#  3. Read the corresponding file from disk
	request_obj = re.match(r"\w+ +(/[^ ]*) ", requestStartLine.decode("utf-8")).group(1)
	'''
	if request_obj == "/":
		request_obj =="/index.html"
	'''
	try:
		f = open(HTML_ROOT+request_obj, "rb")
	# 4. Store in temporary buffer
		data = f.read()
	# 5. Send the correct HTTP response error 404 NOT FOUND
	except IOError:
		# 404 notfound
		# the response data
		response_line = ' HTTP/1.1 404 Not Found\r\n'
		response_header = 'Date: THU, 28 OCT 2021 17:00:00 GMT'
		response_header += 'Content-Type: text/html'
		response_header += 'charset=utf-8\r\n'
		response_body = '<h1>404 Not Found</h1>'
		response_body += '<h2>Sorry, the page is missing...<h2>'


	# 6. Send the content of the file to the socket
	else:
		# the correct response 200 OK
		f.close()
		response_line = ' HTTP/1.1 200 OK\r\n'
		response_header = 'Date: THU, 28 OCT 2021 17:00:00 GMT; Content-Type: text/html; charset=utf-8\r\n'
		response_body = data.decode("utf-8")
	finally:
		response_data = response_line + response_header + "\r\n" + response_body
		tcpSocket.send(bytes(response_data, "utf-8"))
		print(response_data)
	# 7. Close the connection socket
		tcpSocket.close()


def startServer(serverAddress, serverPort):
	"""
	start the process in server
	:param serverAddress:
	:param serverPort:
	:return:
	"""
	# 1. Create server socket
	sevSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM, socket.getprotobyname("tcp"))

	# Set port reuse, let the program exit the port number immediately release
	sevSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

	# 2. Bind the server socket to server address and server port
	sevSocket.bind((serverAddress, serverPort))
	# 3. Continuously listen for connections to server socket
	try:
		print("start listen to ", serverAddress, serverPort)
		sevSocket.listen(128)
	except socket.error:
		print("cannot listen to ", serverAddress)
		exit()
	print("connection established...%s" % serverAddress)
    # 4. When a connection is accepted, call handleRequest function, passing new connection socket (see https://docs.python.org/3/library/socket.html#socket.socket.accept)
	while True:
		clntSocket, ip_port = sevSocket.accept() # accept - return a connected socket
		client = Process(target=handleRequest, args=(clntSocket,))
		client.start()
		# 5. Close server socket
		clntSocket.close()


if __name__ == "__main__":
	global port # 8500
	port = int(input("please input the port you want to run the web page:"))
	startServer(host, port)

