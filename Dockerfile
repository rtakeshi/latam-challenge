# Defining tag for last stable build
#2023-05-30
FROM jupyter/pyspark-notebook:spark-3.5.0


#Copying requirements and installing in container
COPY requirements.txt /tmp/requirements.txt
RUN pip install --no-cache-dir -r /tmp/requirements.txt

#Copying src files to be executed in the container
COPY src /home/jovyan/work/src

#Copying example data to the container
COPY data /home/jovyan/work/data
# Env variables
ENV ZIP_FILE farmers-protest-tweets-2021-2-4.json.zip
ENV DATA_DIR /home/jovyan/work/data

#copying and extracting
COPY /data/raw/$ZIP_FILE $DATA_DIR/
RUN unzip $DATA_DIR/$ZIP_FILE -d $DATA_DIR/

RUN rm $DATA_DIR/$ZIP_FILE



# Exposed port for Jupyter notebook usage
EXPOSE 8888

# init jupyter environment
CMD ["start-notebook.sh"]


