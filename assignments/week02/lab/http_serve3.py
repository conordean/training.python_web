#!/usr/bin/env python

import socket
import httplib
import sys, os


class EchoServer(object):
  """Interacts with Client, recieving and sending data."""

  def __init__(self, host='', port=50001, backlog=5):
    """Constructs the socket connection, configures the server."""

    # Create a TCP/IP socket
    self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
    # Bind the socket to the port
    self.server.bind((host, port))
    print 'Server started on port: ', port
    # Listen for incoming connections
    self.server.listen(backlog)
    print("Server listening\n")
    ## create the socket
    # set an option to tell the OS to re-use the socket
    self.server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    self.size = 1024 # number of bytes to receive at once

  def ProcessRequest(self, size):
    # Wait for a connection
    self.con, self.cli = self.server.accept()
    print 'New connection from ', self.cli
    self.data = self.con.recv(size)
    return self.data
    
  def ProcessResponse(self, data):
    # Send data to client
    self.con.send(data) 

  def CloseSocket(self):
    self.con.close()

  def ParseRequest(self, request):
    i = request.split()
    (verb, http) = i[0], i[2]
    return (verb, http)

  def Payload(self, body):
    body = """
	<html> <body> \
	<h1>""" + body + """</h1> \
	</body> </html> """
    return body

  def ClientErrorResponse(self):
    bad = "HTTP/1.1 400 Bad Request"
    body = self.Payload(bad)
    empty = ""
    resp = "\r\n".join([bad, empty, body])
    return resp

  def Response(self):
    ok = "HTTP/1.1 200 OK"
    body = self.Payload(ok)
    empty = ""
    resp = "\r\n".join([ok, empty, body])
    return resp


def main():
  echo_server = EchoServer()
  while True:
    data = echo_server.ProcessRequest(echo_server.size)
    try:
      if data: # if the connection was closed there would be no data
        (verb, http) = echo_server.ParseRequest(data)
        if verb == 'GET' and http == "HTTP/1.1":
          echo_server.ProcessResponse(echo_server.Response())
        else:
          echo_server.ProcessResponse(echo_server.ClientErrorResponse())
          raise ValueError('%s %s is a bad request' % (verb, http))
    finally:
      print "Closing Socket"
      echo_server.CloseSocket()

main()
