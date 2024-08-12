# HOW TO RUN THE CODE

There are 2 ways in which you can run the application -> 

## 1. Using Docker

### Steps :

    1. Start the Docker Desktop in your system.

    2. Create a Docker Image using the Dockerfile, with the command -> 

        docker build --tag assignment .

    3. After building the image, Run the Docker Image in a container, with the command -> 

        docker run -d -p 5000:5000 assignment

    4. Open the browser and go to the webpage, to view the Application

        localhost/5000


## 2. Using Python Terminal

### Steps

    1. Enter the directory where app.py is present

    2. Run the python file, app.py using the command ->

        python app.py

    3. Open the browser and go to the webpage, to view the Application

        localhost/5000