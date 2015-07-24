# Python Web Frameworks
Collection of simple CRUD in some python web frameworks.
This examples is based on Python 3.4 and last version of web frameworks.

## Web Frameworks
* Flask
* Django
* Bottle
* Falcon
* Tornado
* Muffin

## API
The implementation of all examples follow this API.

### Root route
* **/api**

### Resources

#### Persons

##### Routes
* **/persons**
* **/persons/{id}**

##### GET /persons/
Return a collection of persons
```json
curl -i localhost:8080/api/persons/

HTTP/1.0 200 OK
Content-Type: application/json
Content-Length: 590

{
  "objects": [
    {
      "cod": 1,
      "email": "max@capefear.com",
      "name": "Max Cady",
    },
    {
      "cod": 1,
      "email": "jules@pulpfiction.com",
      "name": "Jules Winnfield",
    }
  ]
}

```
##### GET /persons/{id}/
Return instance of a person
```json
curl -i localhost:8080/api/persons/1/

HTTP/1.0 200 OK
Content-Type: application/json
Content-Length: 258

{
  "cod": 1,
  "email": "max@capefear.com",
  "name": "Max Cady",
}
```

##### POST /persons/
Create a instance of person
```json
curl -i -X POST -H 'Content-Type: application/json' -d '{"name": "Max Cady", "email": "max@capefear.com"}' http://localhost:8080/api/persons/

HTTP/1.0 201 CREATED
Content-Type: application/json
Content-Length: 67

{
  "cod": 1,
  "email": "max@capefear.com",
  "name": "Max Cady"
}
```

##### PUT /persons/1/
Update a instance of person
```json
curl -i -X POST -H 'Content-Type: application/json' -d '{"name": "Max Fear", "email": "max_fear@capefear.com"}' http://localhost:8080/api/persons/1/

HTTP/1.0 200 OK
Content-Type: application/json
Content-Length: 71

{
  "cod": 1,
  "email": "max_fear@capefear.com",
  "name": "Max Fear"
}
```

##### DELETE /persons/1/
Delte a instance of person
```json
curl -i -X DELETE http://localhost:8080/api/persons/1/

HTTP/1.0 204 NO CONTENT
Content-Type: text/html; charset=utf-8
Content-Length: 0
```
