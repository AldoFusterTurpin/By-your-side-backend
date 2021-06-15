# Authors
- Aldo Fuster Turpin (aldo.fuster@estudiantat.upc.edu)
- Mireia Bosque Marí (mireia.bosque@estudiantat.upc.edu)
- Marc Almirall Bertran (marc.almirall@estudiantat.upc.edu)
- Marina Díaz Reyes (marina.diaz@estudiantat.upc.edu)

# By-your-side-backend
Backend of the By Your Side project for the PAE university subject (FIB, UPC).

# Execution instructions

## If you have Docker installed (recommended)

### To run the API and MongoDB, just do:
$ docker compose up -d --build

It will spawn 2 containers (one for the Python API and another one for MongoDB)

API will run on:
http://localhost:8000

Just go to API documentation:
http://127.0.0.1:8000/docs

### To clean your workspace just do:
$ docker compose down

## If you don't have Docker installed:
### Create python [virtual environment](https://docs.python.org/3/tutorial/venv.html):
$ python3 -m venv my-env

### Activate it:
Windows:
$ my-env\Scripts\activate.bat

Linux/Mac:
$ source my-env/bin/activate

### Install the requirements:
$ pip install -r requirements.txt

### Export MongoDB URL for testing purposes
$ export MONGODB_URL="mongodb://localhost:27017"

### Execute MongoDB locally

#### Start the API service using:
$ uvicorn app.main:app --reload

API will run on:
http://localhost:8000

API documentation:
http://127.0.0.1:8000/docs

# Extra information

Structure of the app:
https://fastapi.tiangolo.com/tutorial/bigger-applications/

#### To create Python API docker image
$ docker build -t pae_image .

#### Execute MongoDB inside docker for testing purposes
https://medium.com/codervlogger/python-mongodb-tutorial-using-docker-52f330852b4c
https://www.bmc.com/blogs/mongodb-docker-container/

#### To enter inside mongoDB container and explore
$ docker exec -it mongodb bash

#### To remove mongo docker image 
$ docker rmi mongo

#### To show logs from "mongodb" container
$ docker logs mongodb

#### Configure the location of your MongoDB database (for deployment):
$ export MONGODB_URL="mongodb+srv://<username>:<password>@<url>/<db>?retryWrites=true&w=majority"

# General Notes
Field(...) is used to mark a class attribute as mandatory.

# MongoDB Schema Design Guidelines
https://docs.mongodb.com/manual/core/data-modeling-introduction/
https://developer.mongodb.com/article/mongodb-schema-design-best-practices/
https://www.mongodb.com/blog/post/6-rules-of-thumb-for-mongodb-schema-design-part-1
https://www.mongodb.com/blog/post/6-rules-of-thumb-for-mongodb-schema-design-part-2
https://www.mongodb.com/blog/post/6-rules-of-thumb-for-mongodb-schema-design-part-3

