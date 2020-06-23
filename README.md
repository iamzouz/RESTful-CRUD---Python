# RESTful-CRUD---Python
CMA-CGM Assignment

Kindly find above my code for the requested RESTful CRUD API web application with python.<br>
Below are the structures of the RESTful CRUD APIs. (If you want to test it, with Postman for example)<br>
And please note that i used MySQL DB.


### GET /api/users  -  Get and list all users
```
GET     http://localhost/api/users/

//header

//body

```
___
### POST /api/users  -  Create a new user
```
POST     http://localhost/api/users/

//header
Content-Type          application/json

//body
{
	"fname":"Jhon",
	"lname":"Doe",
	"email":"jhondoe@test.com",
	"phone":"346546344"
}
```
___
### GET /api/users/{userId}  -  Get a single user
```
GET     http://localhost/api/users/{id}

//header

//body

```
___
### PUT /api/users/{userId}   -  Update a user
```
PUT     http://localhost/api/users/1

//header
Content-Type          application/json

//body
{
	"fname":"Jhonnnnnn",
	"lname":"Doe",
	"email":"jhondoe@test.com",
	"phone":"346546344"
}
```
___
### DELETE /api/users/{userId}  -  Delete a user
```
DELETE     http://localhost/api/users/1

//header

//body

```
