# By-your-side-backend
Backend of the By Your Side project for the PAE university subject (FIB, UPC).


# Install the requirements:
pip install -r requirements.txt

# Configure the location of your MongoDB database:
export MONGODB_URL="mongodb+srv://<username>:<password>@<url>/<db>?retryWrites=true&w=majority"

# Start the service:
uvicorn app:app --reload

It will run on http://localhost:8000