from xmlrpc.server import SimpleXMLRPCServer
from xmlrpc.server import SimpleXMLRPCRequestHandler

from functions.string_length import string_length
from functions.string_reverse import string_reverse

class RequestHandler(SimpleXMLRPCRequestHandler):
   rpc_paths = ('/RPC2',)

with SimpleXMLRPCServer(('localhost', 9000), requestHandler=RequestHandler) as server:
   server.register_introspection_functions()

   # register both functions
   server.register_function(string_reverse)
   server.register_function(string_length)

   # start the server
   print("Starting the RPC Server...")
   server.serve_forever()