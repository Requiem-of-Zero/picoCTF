import http.client
conn = http.client.HTTPSConnection("picoctf.org")
conn.request("GET", "/")
r1 = conn.getresponse()
print(r1.status, r1.reason)
# 200 ok
data1 = r1.read()
conn.request("GET", "/a")
r2 = conn.getresponse()
print(r2.status, r2.reason)
#404 Not found
data2 = r2.read()
conn.close()