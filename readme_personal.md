Hello everyone

First of all, thanks for give me the chance to take this test.

Im gonna explain about my solution

ETL Job
I choose pandas, because its an easy way to load and transform data in python, maybe it can be PySpark too but this time i prefer pandas. I create some functions to take apart the main code from the clean, transformation and making ranking steps. Then i export to csv file (OutputFiles/rankings.csv) because its an easy way to show the results but it can be a database connection or something else.

Data Model
I choose ERD Tool from pgAdmin 4 because its was already installed on my personal computer and used to use this database for pesonal projects.

Deployment
I choose Docker because its a easy way to run Python code in any enviroment. To run my code there are 2 alternatives:
    1. Build a new docker image from the de-challenge repository, the requirements are in the requirements.txt file and the image configuration in Dockerfile file (example: docker build -t franciscontreras/walmart_etl:v1 .) the run it (docker run -v localpath:/de-challenge/OutputFiles franciscontreras/walmart_etl:v1)
    2. Pull and run from my Docker Hub. (docker pull franciscontreras/walmart_etl) 

*To get the output csv file with rankings in your local drive, you can run the docker container with this parameter: 
docker run -v localpath:/de-challenge/OutputFiles franciscontreras/walmart_etl:v1
where localpath can be any folder in your local drive
this option make a local mount with the container folder named OutputFiles
**the two options need Docker to be installed

Greetings
