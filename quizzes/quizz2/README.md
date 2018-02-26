## How to run

```sh
FLASK_APP=hello.py flask run
```

### GET hello world message
```sh
curl -i http://127.0.0.1:5000/
```

### POST Users
```sh
curl -i -X POST http://127.0.0.1:5000/users -d "name=Shikai"
```
This step could be repeated several times to add multiple users

___Response___
```sh
HTTP/1.0 201 CREATED
Content-Type: application/json
Content-Length: 35
Server: Werkzeug/0.14.1 Python/3.6.4
Date: Mon, 26 Feb 2018 22:29:33 GMT

{
  "id": 1,
  "name": "Shikai"
}
```

### GET Users
```sh
curl -i -X GET http://127.0.0.1:5000/users/1 
```
The number should not exceed the current users, or no user message will be returned

___Response___
```sh
HTTP/1.0 200 OK
Content-Type: application/json
Content-Length: 35
Server: Werkzeug/0.14.1 Python/3.6.4
Date: Mon, 26 Feb 2018 22:31:35 GMT

{
  "id": 1,
  "name": "Shikai"
}
```

### DELETE Users
```sh
curl -i -X DELETE http://127.0.0.1:5000/users/1
```

___Response___
```sh
HTTP/1.0 204 NO CONTENT
...
```
