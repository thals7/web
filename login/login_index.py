#!C:\Users\SOMIN\AppData\Local\Programs\Python\Python39\python.exe

from http import cookies
import cgi, cgitb

form = cgi.FieldStorage()

print("content-type: text/html; charset=utf-8\n")

print('''<!doctype html>
<html>
<head>
  <title>Set Cookie Program</title>
  <meta charset="utf-8">
</head>
<body>
  <form action="create_cookie.py" method="post">
  <p>
  Input user ID and Password
  </p>
  <p>
  ID : <input type="text" name="userId"><br>
  Password : <input type="text" name="password"></p>
  <p></p>
  <input type="submit" value="login">
</form>
</body>
</html>''')