import socket, sys, struct, pickle
def handle_request(*data):
	SizeStruct = struct.Struct('!I')
	info = pickle.dumps(data)
	try:
		with SocketManager(Address) as sock:
			sock.sendall(SizeStruct.pack(len(info)))
			sock.sendall(info)
			size_info = sock.recv(SizeStruct.size)
			size = SizeStruct.unpack(size_info)
			rval = sock.recv(size[0])
		return pickle.loads(rval)
	except socket.error as err:
		print (err)
		sys.exit(1)
class SocketManager:
	def __init__(self, address):
		self.address = address
	def __enter__(self, *ignore):
		self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.sock.connect(self.address)
		return self.sock
	def __exit__(self, *ignore):
		self.sock.close()
