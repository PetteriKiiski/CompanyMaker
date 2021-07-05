import socketserver, threading, sys, struct, pickle
def main():
	try:
		server = ChatServer(('10.0.0.147', 9653), RequestHandler)
		server.serve_forever()
	except Exception as err:
		print ('ERROR: {0}'.format(err))
		sys.exit(1)
class Server(socketserver.ThreadingMixIn, socketserver.TCPServer):pass
class RequestHandler(socketserver.StreamRequestHandler):
	def handle(self):
		SizeStruct = struct.Struct('!I')
		size_data = self.rfile.read(SizeStruct.size)
		size = SizeStruct.unpack(size_data)
		size = size[0]
		data = pickle.loads(self.rfile.read(size))
		with CallLock:
			reply = CallDict[data[0]](self, *data[1:])
		print (reply)
		reply = pickle.dumps(reply, 3)
		self.wfile.write(SizeStruct.pack(len(reply)))
		self.wfile.write(reply)
