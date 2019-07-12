from websocket import create_connection
ws = create_connection('ws://192.168.87.146:8000/ws/chat/x/')
print("Sending 'Hello, World'...")
ws.send("Hello, World")
print("Sent")
print("Receiving...")
result =  ws.recv()
print("Received '%s'" % result)
ws.close()