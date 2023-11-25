FROM python:3.7 
# this will be the base system on which everything will be deployed .here we're creating  base image
COPY . /app
# here we will create a app folder in the base image where we will copy all the files
WORKDIR /app
#this will be the working directory
RUN pip install -r requirements.txt
#we need to first install all the necessary libraries when we run the docker image
EXPOSE $PORT
#to access the application inside the container we need some port to access it .The cloud server will automatically assign the port
CMD gunicorn --workers=4 --bind 0.0.0.0:$PORT app:app
#the gunicorn command will run the python application on heroku server and the workers will divide the request and then we will bind it with the local address of the heroku server and our port


# ------------------------------------------------------------------------------------------------------------------


#then we will creating two folders .github/workflows and when we push our folder to github it recognizes this folder and goes into .yaml file where we havee our necessary configurations so it uses those things and build our docker image

