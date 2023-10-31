# Defining tag for last stable build
#2023-05-30
FROM jupyter/pyspark-notebook:spark-3.5.0


#Copying requirements and installing in container
COPY requirements.txt /tmp/requirements.txt
RUN pip install --no-cache-dir -r /tmp/requirements.txt

#Copying src files to be executed in the container
COPY src /home/jovyan/work/src

#Copying test files
COPY test /home/jovyan/work/test

# Create a non-root user (you can name it whatever you like)
USER root
RUN useradd -ms /bin/bash pytest_user
# Change permissions for the /workspace/test directory
RUN chmod -R 777 /workspace/test
# Switch back to the non-root user
USER pytest_user
# Set the working directory
WORKDIR /workspace


#copying and extracting
COPY /data/raw/ /home/jovyan/work/data/raw/


# Exposed port for Jupyter notebook usage
EXPOSE 8888

# init jupyter environment
CMD ["start-notebook.sh"]


