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

# Start the service:
uvicorn app:app --reload

It will run on http://localhost:8000

API documentation:
http://127.0.0.1:8000/docs

Structure of the app:
https://fastapi.tiangolo.com/tutorial/bigger-applications/
