#Use Python 3.6 as a base image
FROM python:3.6
RUN apt-get update && apt-get install -y python3-pip
#WORKDIR ./application
COPY . .
RUN pip3 install -r requirements.txt
EXPOSE 5000
ENTRYPOINT ["/usr/local/bin/python3", "app.py"]
# Copy contents into image
 
# install pip dependencies from requirements file
 
# Expose correct port

# Create an entrypoint

