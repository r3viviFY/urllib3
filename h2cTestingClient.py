from urllib3.http2.connection import HTTP2ConnectionNoTLS
connection = HTTP2ConnectionNoTLS("localhost", 8080)
connection.connect()
connection.request("GET", "/")
response = connection.getresponse()
print(response.status, response.data)