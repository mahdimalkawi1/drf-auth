# Authentication & Production Server

## Django REST Framework & Docker
### Author: Mahdi Malkawi - Ibrahim adnan
#### How to initialize/run your application (where applicable)
to run the app:
- docker-compose up 

## Getting Started

1- Base URL: The base URL for all API endpoints is: http://127.0.0.1:8000

2- Authentication: Some routes require an access token. To get an access token, use the /api/token/ route with appropriate credentials.

3- HTTP Clients: You can use any HTTP Client of your choice, such as  ThunderClient, to test the API endpoints.


## Routes
### Get Tokens
- HTTP Method: POST
- Route: /api/token/
- Token Required: No

### Example Request (using ThunderClient):

```

POST http://127.0.0.1:8000/api/token/

Content-Type: application/json

{
  "username": "your_username",
  "password": "your_password"
}


```
Example Response:

```
{
  "access_token": "YOUR_ACCESS_TOKEN",
  "refresh_token": "YOUR_REFRESH_TOKEN",
}

```
### Refresh Tokens :
- HTTP Method: POST
- Route: /refresh-tokens
- Token Required: Yes

This route allows you to refresh your access token using a valid refresh token.

Example Request (using ThunderClient):
```
POST http://127.0.0.1:8000/api/token/refresh/
Authorization: Bearer YOUR_REFRESH_TOKEN

```
### Example Response:

```
{
  "access_token": "NEW_ACCESS_TOKEN",
  "expires_in": 3600
}

```

### CRUD Routes for Snacks
Token Required: 
- read: no

- create, update, delete: yes

* api/v2/snacks/

### Create Snacks

HTTP Method: POST

Route: api/v2/snacks/

Token Required: Yes

Example Request (using ThunderClient):


```
POST http://127.0.0.1:8000/api/v2/snacks/
Authorization: Bearer YOUR_ACCESS_TOKEN
Content-Type: application/json

  {
    "owner": 1,
    "title": "mansaf",
    "desc": "the best"
  }
```
### Example Response:

```
  {
    "id": 1,
    "owner": 1,
    "title": "mansaf",
    "desc": "the best"
  }
```

### Read Snacks
HTTP Method: GET

Route: /api/v2/snacks/{id}

Token Required: no

Example Request (using ThunderClient):

```
GET http://127.0.0.1:8000/api/v2/snacks/1

```
### Example Response:

```
  {
    "id": 1,
    "owner": 1,
    "title": "mansaf",
    "desc": "the best"
  }
```

### Update Snacks

HTTP Method: PUT

Route: /api/v2/snacks/{id}

Token Required: Yes

Example Request (using ThunderClient):


```
PATCH http://127.0.0.1:8000/api/v2/snacks/1
Authorization: Bearer YOUR_ACCESS_TOKEN
Content-Type: application/json

{

    "title": "mansaf",
    "desc": "the best"
}

```
### Example Response:

```
  {
    "id": 1,
    "owner": 1,
    "title": "mansaf",
    "desc": "the best"
  }
```
### Delete Snacks

HTTP Method: DELETE

Route: /api/v2/snacks/{id}

Token Required: Yes

Example Request (using ThunderClient):

```
DELETE http://127.0.0.1:8000/api/v2/snacks/1
Authorization: Bearer YOUR_ACCESS_TOKEN
```
Example Response:

```
204 No Content
```

