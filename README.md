# By-your-side-backend
Backend of the By Your Side project for the PAE university subject (FIB, UPC).

# Create python virtual environment (https://docs.python.org/3/tutorial/venv.html):
python3 -m venv my-env

# Activate it:
# Windows:
my-env\Scripts\activate.bat

# Linux/Mac:
source my-env/bin/activate

# Install the requirements:
pip install -r requirements.txt

# Export MongoDB URL for testing purposes
export MONGODB_URL="mongodb://localhost:27017"

# Start MongoDB test container
docker compose up -d --build

# Start the API service using:
uvicorn app.main:app --reload

API will run on:
http://localhost:8000

API documentation:
http://127.0.0.1:8000/docs

# #########################################################

Structure of the app:
https://fastapi.tiangolo.com/tutorial/bigger-applications/

# Execute the app using Docker:
# Create docker image
docker build -t pae_image .

# To run both API and MongoDB using Docker
------------------------------
Work in progress:
API running outside container and mongodb inside container is working.
BUT ...
API running inside container and mongodb inside container is not working: can access API docs but error when executing 
GET /clients (or any HTTP method) because can't connect to the MongoDB container from the API (Python) container
(Docker network stuff to investigate).
The error is a timeout:
pymongo.errors.ServerSelectionTimeoutError(...)

docker run -d --name pae_container -p 8000:8000 -e MONGODB_URL="mongodb://localhost:27017" pae_image
or
docker run -d -p 8000:8000 -e MONGODB_URL="mongodb://localhost:27017" --name pae_container --net=mynet pae_image
------------------------------

# Execute MongoDB inside docker for testing purposes
https://medium.com/codervlogger/python-mongodb-tutorial-using-docker-52f330852b4c
https://www.bmc.com/blogs/mongodb-docker-container/

# To enter inside mongoDB container and explore
docker exec -it mongodb bash

# To remove mongo docker image 
docker rmi mongo

# To show logs from "mongodb" container
docker logs mongodb

# Configure the location of your MongoDB database (for deployment):
export MONGODB_URL="mongodb+srv://<username>:<password>@<url>/<db>?retryWrites=true&w=majority"

# Do not use the below line to start the API because an error will be thrown (RuntimeError: Task <Task pending name='Task-24' coro=<RequestResponseCycle.run_asgi() running at /Users/aldofusterturpin/git/By-your-side-backend/my-env/lib/python3.9/site-packages/uvicorn/protocols/http/h11_impl.py:394> cb=[set.discard()]> got Future <Future pending> attached to a different loop)
python3 -m app.main

# General Notes
Field(...) is used to mark a class attribute as mandatory.