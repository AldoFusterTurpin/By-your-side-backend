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

# Configure the location of your MongoDB database:
export MONGODB_URL="mongodb+srv://<username>:<password>@<url>/<db>?retryWrites=true&w=majority"

# Start the API service:
uvicorn app.main:app --reload

API will run on http://localhost:8000

API documentation:
http://127.0.0.1:8000/docs

Structure of the app:
https://fastapi.tiangolo.com/tutorial/bigger-applications/

# Execute the app using Docker:
# Create docker image
docker build -t pae_image .

# Run Docker container
docker run -d --name pae_container -p 80:80 pae_image

# Execute MongoDB inside docker for testing purposes
https://medium.com/codervlogger/python-mongodb-tutorial-using-docker-52f330852b4c
https://www.bmc.com/blogs/mongodb-docker-container/

# To execute docker compose file and start mongoDB container
docker compose up -d

# To enter inside mongoDB container and explore
docker exec -it mongodb bash

# To remove mongo docker image 
docker rmi mongo

# To show logs from container
docker logs mongodb

# Export MongoDB local URL for testing purposes
export MONGODB_URL="mongodb://localhost:27017"

# General Notes
Field(...) is used to mark a class attribute as mandatory.