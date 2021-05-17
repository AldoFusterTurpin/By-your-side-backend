# By-your-side-backend
Backend of the By Your Side project for the PAE university subject (FIB, UPC).

# If you have Docker installed just do:
docker compose up -d --build

It will spawn 2 containers (one for the Python API and another one for MongoDB)

API will run on:
http://localhost:8000

Just go to API documentation:
http://127.0.0.1:8000/docs

# If you don't have Docker installed
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

# Execute MongoDB locally

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
