#! /usr/bin/python

import sys
import socket


class EchoServer(object):
  """Interacts with Client, recieving and sending data."""

  def __init__(self, host="127.0.0.1", port=50000, backlog=5):
    """Constructs the socket connection, configures the server."""

    # Create a TCP/IP socket
    self.server = socket.socket(2, 1, 0)
    # Bind the socket to the port
    self.server.bind((host, port))
    print 'Server started on port: ', port
    # Listen for incoming connections
    self.server.listen(backlog)
    print("Server listening\n")

  def ProcessRequest(self):
    # Wait for a connection
    self.con, self.cli = self.server.accept()
    print 'New connection from ', self.cli
    self.data = self.con.recv(1024)
    print "Client Request: " + self.data
    return self.data
    
  def ProcessResponse(self, response):
    # Send data to client
    self.con.sendall('The result is ' + str(response))

  def DoMath(self, data):
    self.data = self.data.split()
    if self.data[1] == '+':
      result = int(self.data[0]) + int(self.data[2])
    elif self.data[1] == '-':
      result = int(self.data[0]) - int(self.data[2])
    elif self.data[1] == '*':
      result = int(self.data[0]) * int(self.data[2])
    elif self.data[1] == '/':
      result = int(self.data[0]) / int(self.data[2])
    return result

  def CloseSocket(self):
    self.con.close()


def main():
  echo_server = EchoServer()
  while True:
    data = echo_server.ProcessRequest()
    try:
      echo_server.ProcessResponse(echo_server.DoMath(data))
    finally:
      print "Closing Socket"
      echo_server.CloseSocket()

main()
