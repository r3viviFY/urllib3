from urllib3.http2.connection import HTTP2ConnectionPlaintext
connection = HTTP2ConnectionPlaintext("localhost", 8080)
connection.connect()
connection.request("GET", "/")
response = connection.getresponse()
print(response.status, response.data)