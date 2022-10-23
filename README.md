# Flask Motivation API

[Motivation API](https://github.com/bdzhalalov/Motivator_motivations) uses Django and has an alternative presented by this project with the same functions, however, in this case, Flask is used.

## Dependencies

* Flask 2.2.2
* MongoDB 6.0.1
* Flask-PyMongo 2.3.0

## Features

* This is REST API with support CRUD operations.

* API run with `docker-compose` file.

* MongoDB are used in API as database for motivations.

* Access to endpoints provided with `API-key` header in requests.

* `API-key` checked by custom middleware for all requests to endpoints.

* You can test efficiency of endpoints with unittsets which are avialable in the project.

## Usage

* Create your own `.env` file for environment variables.

* Open terminal and go to directory with this project.

* Use next command to start API:
  `docker-compose up -d --build`
