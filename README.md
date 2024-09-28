# Simple-Flask-template  
This is the example project for the article written in [medium](https://medium.com/@winhtaikaung76/docker-%E1%80%94%E1%80%B2%E1%80%B7-development-%E1%80%9C%E1%80%AF%E1%80%95%E1%80%BA%E1%80%80%E1%80%BC%E1%80%99%E1%80%9A%E1%80%BA-e98ad953d517)

In order to run this project you have set up  docker already in your machine and set following variables.

## Environment Variables
```
ENV=development
DB_URL_FORMAT=postgresql://{}:{}@{}:{}/{}

DB_HOST=postgres
DB_PORT=5432
PORT=5000

DB_NAME=db_flask_test
DB_USER_NAME=postgres
DB_PASSWORD=123456
```
## Running the Application
then run following commands for building and running the containers

    docker-compose build
    docker-compose up

if you want to shutdown the containers

    docker-compose down


## DO WHAT THE FUCK YOU WANT TO PUBLIC LICENSE(v2)

 
Copyright (C) 2024 Win Htaik Aung <winhtaikaung28@hotmail.com>

Everyone is permitted to copy and distribute verbatim or modified
copies of this license document, and changing it is allowed as long
as the name is changed.
 
 DO WHAT THE FUCK YOU WANT TO PUBLIC LICENSE
 TERMS AND CONDITIONS FOR COPYING, DISTRIBUTION AND MODIFICATION

 You just DO WHAT THE FUCK YOU WANT TO.