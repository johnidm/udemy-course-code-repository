



Users
```
curl -X 'POST' \
  'http://127.0.0.1:8000/api/v1/user/' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "fullname": "Elica Ser",
  "email": "el@se.com",
  "password": "123456"
}'
```

```
curl -X 'GET' \
  'http://127.0.0.1:8000/api/v1/user/' \
  -H 'accept: application/json'
```


Blogs
```
curl -X 'GET' \
  'http://127.0.0.1:8000/api/v1/blog/' \
  -H 'accept: application/json'
```

```
curl -X 'GET' \
  'http://127.0.0.1:8000/api/v1/blog/1' \
  -H 'accept: application/json'
```

```
curl -X 'DELETE' \
  'http://127.0.0.1:8000/api/v1/blog/1' \
  -H 'accept: */*'
```

```
curl -X 'POST' \
  'http://127.0.0.1:8000/api/v1/blog/' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -H 'authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1aWQiOjIsInVmbiI6IkVsaWNhIFNlciIsInN1YiI6ImVsQHNlLmNvbSIsImV4cCI6MTcwODE4MTg0NH0.-p_KyyTFAvOGips7KyVZA_LTngZwy0oTqLkSOWxyfe0' \
  -d '{
  "title": "Best Practice in CSharp",
  "content": "no content yet"
}'
```


```
curl -X 'PUT' \
  'http://127.0.0.1:8000/api/v1/blog/1' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "title": "Best Practice in Python 3.12 - All You Should Have to Do",
  "content": "no content yet"
}'
```

Auth
```
curl -X 'POST' \
  'http://127.0.0.1:8000/api/v1/auth/login' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/x-www-form-urlencoded' \
  -d 'grant_type=&username=el%40se.com&password=123456'
```

```
curl -X 'GET' \
  'http://127.0.0.1:8000/api/v1/auth/me' \
  -H 'accept: application/json' \
  -H 'authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1aWQiOjIsInVmbiI6IkVsaWNhIFNlciIsInN1YiI6ImVsQHNlLmNvbSIsImV4cCI6MTcwODE4MTg0NH0.-p_KyyTFAvOGips7KyVZA_LTngZwy0oTqLkSOWxyfe0'
```

