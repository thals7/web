#!C:\Users\SOMIN\AppData\Local\Programs\Python\Python39\python.exe
print("content-type: text/html; charset=utf-8\n")

from http import cookies
import cgi

form = cgi.FieldStorage()

userId = form.getvalue("userId")
password = form.getvalue("password")

cookie = cookies.SimpleCookie()
cookie["userId"] = userId
cookie["password"] = password

print(cookie)