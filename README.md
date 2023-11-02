# LATAM Challenge Solution

For challenge description go to: https://github.com/rtakeshi/latam-challenge/blob/main/latam-challenge.md

## Gitflow

### Branches

1. main
2. dev
3. build
4. test
5. data-exploration


**Disclaimer**: This README.md file will be edited and committed outside of GitFlow. I will edit it whenever necessary to provide a clearer explanation of my solution.


## Infra

Using Terraform, i provisioned and created Google Cloud Storage to receive staging data.

### Google Cloud Storage

My Google Cloud Storage bucket, named 'latam-challenge-rtkseo-bucket,' will contain two folders:

'staging': This folder will contain the staging data quality dataset used for solving the questions.

'test': This folder will hold test data related to staging data quality to implement Test-Driven Development (TDD).


**Future improvements**:

1. Declaring Cloud Build Trigger as Infrastructure as Code (IaC).
2. Provisioning and creating a Cloud Run instance to receive the built container from the Artifact Registry.
3. While using a public Google Cloud Storage instance may be acceptable for development and non-sensitive data, it's important to emphasize that security configurations are vital in production environments. Proper IAM permissions, network security, and data access controls are critical to protect sensitive data and ensure compliance with security standards.

**Difficulties**: It was hard to configure my container to use correctly hadoop file system connectors for GCS; i decided to copy my staging data to local container to continue my development


## Build - CI Pipeline for Artifact Registry

A CI pipeline was created via the Google Cloud Platform Console.

The main goal of this pipeline is to continuously build and integrate my container into the Artifact Registry.


**Future improvements**:

1. Infra should have its own repository and CI/CD pipeline with Terraform lifecycle.
2. The cloudbuild.yaml file is hard writen for my free trial account of GCP
3. We can implement DevSecOps at build time, incorporating SAST (Static Application Security Testing) to evaluate code vulnerabilities and test coverage, as well as SCA (Software Composition Analysis) to provide visibility into requirement vulnerabilities.
4. Due to the decision to complete the challenge's development locally, it is necessary to integrate unit tests into the CI by setting up the PySpark environment at build time.

**Difficulties**: I faced some problems when building my container. These issues stemmed from my limited knowledge of how to use Docker Hub jupyter/pyspark container.

## Docker Container

Using the jupyter/pyspark-notebook image, I was able to build an environment ready for implementing PySpark and Jupyter Notebook. This enables us to maintain consistency in this environment across any machine, simplifying deployment.


## Data Exploration


After the initial phase of exploration, it was identified that the "farmers-protest-tweets" file comprises multiple columns, and a schema was created in the "aux > tweet_payload_schema" file. During the discovery process, data curation was carried out to determine which columns would be utilized in the solutions for the questions.

**Disclaimer**: The data was found to be outdated in comparison to the Data dictionary provided by Twitter's documentation.

q1. Las top 10 fechas donde hay más tweets. Mencionar el usuario (username) que más publicaciones tiene por cada uno de esos días.

**Columns: id, date, user.username**

q2. Los top 10 emojis más usados con su respectivo conteo.

**Columns: id, content**

q3. El top 10 histórico de usuarios (username) más influyentes en función del conteo de las menciones (@) que registra cada uno de ellos. 

The "mentionedUsers" at the main tweet level appear to be filled with null values, necessitating the transformation of the content to retrieve the users.

**Columns: id, content, user.username**

After the data curation process, it was decided to create a staging table with only four columns:

-id
-date
-username
-content

### Data Quality Check

There are no duplications by tweet ID, and there are no null values in the dataset. 

The quality analysis is implemented in src/challenge.ipynb

## Data Transformation

For this purpose, a classical ETL approach will be implemented to extract columns that will be used in the solutions to the questions.

A Jupyter notebook for data transformation will be created at the following path: src/transform/farmers_proest_tweet_transformation.ipynb.

The resulting dataset will be stored in GCS to be read by the functions.

It was stored using boto3 python package

**Future improvements**

1. If this application begins to consume dynamic data, consider implementing an ELT approach.
2. When dealing with dynamic data, it becomes essential to incorporate data quality checks into the data transformation step.

## TDD - pytest

By using PyTest, I will implement one test scenario for each question's solution.

I will prepare a dataset in staging quality layer to apply the functions; Test datasets will be stored in my container in the folder "test"; the development will be guided through those test cases.

### Mocked Data

By using the Python Faker package, I was able to develop two Python programs with the assistance of ChatGPT to generate mocked data for my experimental scenarios.

The mocked data consisted of an ID, date, content using random emojis, random mentions, and usernames.

The "mock_data.py" generated data for my TDD development.
The "mock_volume_data.py" generated data for the PySpark memory and time usage analysis. By adjusting parameters, I was able to create two datasets with 2.2GB and 20GB of data.
My mocked data generators are located in the "data/test" folder.

### Developing expected results for test cases

To obtain my expected results for test cases, I encountered difficulties when attempting to automate the generation in ChatGPT. The solution provided was to create a sandbox notebook (not included in this repository) in order to generate the expected results manually.

As a result, for each question's solution, I had to develop a preliminary version in my local sandbox. I understand that this approach is not in line with good TDD (Test-Driven Development) practices.

**Future improvements**

1. It is important to create more test cases scenarios;
2. While data transformation tests are not included in this project, it is crucial to define appropriate scenarios for data integration testing, especially when dealing with dynamic data.

## Code Implementation and Solution Analysis 

I chose to use PySpark because of its ability to process large volumes of data in a distributed manner, leveraging cluster scalability for future deployments.

With PySpark's flexibility and parallel processing capabilities, I can efficiently handle future data growth, making it an ideal choice for Big Data projects and scalable data analysis.

For each question, I will utilize memory usage and execution time measurements.

Memory analizing: Memory profiler cannot read memory registers used by PySpark/JVM i had utilize job analysis in Spark Web UI to understand memory usage and execution time in each scenario 




### PySpark Memory Optimization

By default Spark has differents kinds of memory usage:

Storage (spark.driver.memory): Cache and store frequently accessed data, you can cache() or persist() to use Storage memory.

Executor (spark.executor.memory): Memory allocated for task executions and data processing in Spark.

PySpark's read operations are lazy by default. This lazy loading approach is one of the key features of PySpark, and it helps optimize memory usage. Data is only loaded into memory when it's necessary for performing computations or when an action is triggered.

#### Steps applied to reduce memory usage:

1. Schema definition
2. Lazy data load by default
3. No caching and no persistance used
4. Keep data volume in control by the using needs


#### PySpark Time Optimization

Persisting data Memory Only, creating a cache




### Analysis

For this particular case, I will create two different configurations for SparkSessions:

1. The first one, named "FarmersProtestTweets," will have the default SparkSession configuration for memory allocation to executors and drivers.
2. The second one, "FarmersProtestTweetsOptimization," will allocate 4GB of memory to both the Spark driver and executor.

To better understand the solution i will analyze more deeply the function using 20gb Dataset.
The main results can be found in src/challenge.ipynb





## Conclusions



