#!/usr/bin/env python

import socket
import httplib
import sys, os



class EchoServer(object):
  """Interacts with Client, recieving and sending data."""

  def __init__(self, host='', port=50000, backlog=5):
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
    print "Client Request: " + self.data
    return self.data
    
  def ProcessResponse(self, data):
    # Send data to client
    self.con.send(data) 

  def CloseSocket(self):
    self.con.close()

  def Payload(self):
    self.body = """
    <html> <body> \
    <h1>This is a header</h1> \
    <p> \
    and this is some regular text \
    </p> \
    <p> \
    and some more \
    </p> \
    </body> \
    </html> """
    return self.body

  def Response(self):
    body = self.Payload()
    ok = "HTTP/1.1 200 OK"
    empty = ""
    resp = "\r\n".join([ok, empty, body])
    return resp

  def ParseRequest(data):
    for line in data:
      if "GET" in line:
        print "FOUND GET"    


def main():
  echo_server = EchoServer()
  while True:
    data = echo_server.ProcessRequest(echo_server.size)
    try:
      if data: # if the connection was closed there would be no data
        echo_server.ProcessResponse(echo_server.Response())
    finally:
      print "Closing Socket"
      echo_server.CloseSocket()

main()
