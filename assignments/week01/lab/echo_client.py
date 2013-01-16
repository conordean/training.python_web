#! /usr/bin/python

import sys
import socket


class EchoClient(object):
  """Interacts with Server, sending and recieving request data."""

  def __init__(self, host='127.0.0.1', port=50000):
    """Constructs the socket connection, configures the client."""
  
    # Create a TCP/IP socket
    self.client = socket.socket(2, 1, 0)   
 
    # Connect the socket to the port where the server is listening
    self.client.connect((host, port))

  def MakeRequest(self, request):
    # Send data to server
    self.client.sendall(request)

  def UserInput(self): 
    value = raw_input("Add, Subtract, Multiply, or Divide two integers. (4 + 4) ")
    return value

  def FetchResult(self):
    result = self.client.recv(1024)
    return result
  
  def CloseSocket(self):
    return self.client.close()


def main():
  while True:
    echo_client = EchoClient()
    message = echo_client.UserInput()
    try:
      # send data
      echo_client.MakeRequest(message)
      # print the response
      print echo_client.FetchResult()
    finally:
      print "Closing Socket"
      echo_client.CloseSocket()

main() 
