# Defining tag for last stable build
#2023-05-30
FROM jupyter/pyspark-notebook:spark-3.5.0


#Copying requirements and installing in container
COPY requirements.txt /tmp/requirements.txt
RUN pip install --no-cache-dir -r /tmp/requirements.txt

#Copying src files to be executed in the container
COPY src /home/jovyan/work/src


# Env variables
ENV ZIP_FILE farmers-protest-tweets-2021-2-4.json.zip
ENV UNZIP_FILE farmers-protest-tweets-2021-2-4.json
ENV DATA_DIR /home/jovyan/work/data


#copying and extracting
COPY /data/raw/$ZIP_FILE /tmp/$ZIP_FILE
RUN unzip /tmp/$ZIP_FILE -d /tmp/
RUN ls -a /tmp/
COPY /tmp/$UNZIP_FILE $DATA_DIR/$UNZIP_FILE
RUN rm /tmp/$ZIP_FILE



# Exposed port for Jupyter notebook usage
EXPOSE 8888

# init jupyter environment
CMD ["start-notebook.sh"]


