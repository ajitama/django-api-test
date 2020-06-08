### 基本的なAPIとトークンの発行。APIのトークンによる認証実行



### 
ajitama@ajitama-srv:~$ python3 --version  
Python 3.8.2  
ajitama@ajitama-srv:~$ python3 -m django --version  
3.0.6  


### インストールパッケージ
apt install python3-pip  
pip3 install Django  

pip3 install djangorestframework  
pip3 install djangorestframework-jwt # token 認証用  

### sample request

- get api  
curl -X GET  -H "Content-Type: application/json"  localhost:8080/api/coupon_list/  

- post api  
curl -X POST  -H "Content-Type: application/json" -d '{"url": "http://hogehoge.test.com/2222222222", "request_code": "2222222222","arg1": "11111","arg2": 1}' localhost:8080/api/coupon_list/


- token request
$ curl http://localhost:8080/jwt-token -d "username=admin&password=admin"

{"token":"eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoxLCJ1c2VybmFtZSI6ImFkbWluIiwiZXhwIjoxNTkxNTgwNTgzLCJlbWFpbCI6ImFkbWluQGxvY2FsaG9zdC5jb20ifQ.i6qu_VIUuU-G_x9CqgbsPxlpoW7FL0tgzIcqCX8r33M"}
