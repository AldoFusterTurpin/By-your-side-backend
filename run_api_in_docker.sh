docker rmi --force pae_image \
&& docker rm --force pae_container \
&& docker build -t pae_image . \
&& docker run -d -p 8000:8000 -e MONGODB_URL="mongodb://localhost:27017" --name pae_container pae_image