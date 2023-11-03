# Defining tag for last stable build
#2023-05-30
FROM jupyter/pyspark-notebook:spark-3.5.0


#Copying requirements and installing in container
COPY requirements.txt /tmp/requirements.txt
RUN pip install --no-cache-dir -r /tmp/requirements.txt




#Copying src files to be executed in the container
COPY src /home/jovyan/work/src
#copying raw data
COPY data/raw /home/jovyan/work/data/raw
#copying staging data
COPY data/staging /home/jovyan/work/data/staging
#copying TDD data
COPY data/test/test_data.csv /home/jovyan/work/data/test/test_data.csv
#Copying test files
COPY test /home/jovyan/work/test

# Exposed port for Jupyter notebook usage
EXPOSE 8888

# init jupyter environment
CMD ["start-notebook.sh"]


