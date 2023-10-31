# Defining tag for last stable build
#2023-05-30
FROM jupyter/pyspark-notebook:spark-3.5.0


#Copying requirements and installing in container
COPY requirements.txt /tmp/requirements.txt
RUN pip install --no-cache-dir -r /tmp/requirements.txt




#Copying src files to be executed in the container
COPY src /home/jovyan/work/src
#copying raw data
COPY data/raw/ /home/jovyan/work/data/raw/

#Copying test files
COPY test /home/jovyan/work/test

#Permission to test directory
USER root
RUN chmod -R 777 /home/jovyan/work/test \
    && chmod -R 777 /home/jovyan 
RUN useradd -ms /bin/bash pytest_user
USER pytest_user

# Exposed port for Jupyter notebook usage
EXPOSE 8888

# init jupyter environment
CMD ["start-notebook.sh"]


