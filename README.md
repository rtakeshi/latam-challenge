# LATAM Challenge Solution

For challenge description go to: https://github.com/rtakeshi/latam-challenge/blob/main/latam-challenge.md

## Objectives

1. The primary goal of this case solution is to explore memory usage and optimization within a distributed and scalable data processing environment like Spark.
2. Exploring scalable cloud solutions such as Cloud Storage, Cloud Build, and Cloud Run in GCP.
3. Implement an reproductible environment using Docker ready to execute Jupyter and PySpark
4. Implement an automated Cloud Build CI for my Docker image to GCP Artifact Registry.
5. Establishing and adhering to a Git flow to establish an efficient workflow for organizing features, builds, and testing tasks.
6. Implementing Test-Driven Development (TDD) to address the challenge questions.
7. Implementing data transformations to define data quality layers.
8. Exploring analytical data transformation techniques to tackle the challenge questions.

As a bonus, I will also explore Infra as Code concepts to create a Google Cloud Storage (GCS) to store my test and staging datasets.


## Gitflow


I've organized my Gitflow with separate branches to match different contexts of the development activities:

1. main: This branch serves as the primary branch and contains all confirmed, production-ready changes. It receives merges only from the dev branch.
2. dev: The dev branch is where I integrate the various stages of my development work. It serves as a staging area for the development environment. It's where changes from other feature branches are merged, and it's the primary source for merging into main.
3. build: The build branch is dedicated to activities related to Continuous Integration (CI) and constructing the container for the solution. It ensures that the application can be built and deployed successfully.
4. test: In the test branch, I focus on creating test scenarios and handling everything related to Test-Driven Development (TDD). This branch is crucial for ensuring the reliability and quality of the code.
5. data-exploration: This branch is dedicated to data exploration activities. It's where I work on tasks related to data analysis, exploration, and preparation for the main development efforts.
6. analysis: The analysis branch is where I concentrate on analytical tasks, including the creation of experimental scenarios, data analysis, and other related activities that help inform decision-making and improvements.
7. others: Various branches used for resolving the challenge questions.

For my commits, I've applied message patterns to enhance contextual understanding, following the same logic as applied to naming branches

**Disclaimer**: This README.md file will be edited and committed outside of GitFlow. I will edit it whenever necessary to provide a clearer explanation of my solution.




## Build - CI Pipeline for Artifact Registry

A CI pipeline was created via Google Cloud Platform Console.

The main goal of this pipeline is to continuously build and integrate my container into the Artifact Registry.


**Future improvements**:

1. Infra should have its own repository and CI/CD pipeline with Terraform lifecycle.
2. The cloudbuild.yaml file is hard writen for my free trial account of GCP 
3. We can implement DevSecOps at build time, incorporating SAST (Static Application Security Testing) to evaluate code vulnerabilities and test coverage, as well as SCA (Software Composition Analysis) to provide visibility into requirement vulnerabilities.
4. Due to the decision to complete the challenge's development locally, it is necessary to integrate unit tests into the CI by setting up the PySpark environment at build time.

**Difficulties**: I faced some problems when building my container. These issues stemmed from my limited knowledge of how to use Docker Hub jupyter/pyspark container.

### Docker Container

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


### Post-Challenge Errata (04/11/2023)
When this section was written, I was initially planning to implement a refined data quality layer to address my analytical questions. However, in the end, it became clear that it didn't align with the goals of my analysis.

I actually implemented an ELT approach, and, for clarity, this section should be labeled "Data Extraction.

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
3. In Mocking data, it will be good to create a new Large partioned Parquet file to go deeply in memory usage and optmization.

## Code Implementation and Solution Analysis

I chose to use PySpark due to its capacity to process extensive datasets in a distributed fashion, capitalizing on cluster scalability for potential deployments.

PySpark's adaptability and parallel processing capabilities allow me to effectively manage future data expansion, rendering it a prime selection for Big Data projects and scalable data analysis.

Memory profiler cannot access memory registers utilized by PySpark/JVM. I had to utilize job analysis in the Spark Web UI to comprehend memory usage and execution time in each data volume scenario.

For this case, I treated every question as an independent job, with the expectation of the existence of a SparkSession to execute it.

### PySpark Memory Optimization

By default Spark has differents kinds of memory usage:

Storage (spark.driver.memory): Cache and store frequently accessed data, you can cache() or persist() to use Storage memory.

Executor (spark.executor.memory): Memory allocated for task executions and data processing in Spark.

PySpark's read operations are lazy by default. This lazy loading approach is one of the key features of PySpark, and it helps optimize memory usage. Data is only loaded into memory when it's necessary for performing computations or when an action is triggered.

#### Steps applied to reduce memory usage:

1. Schema Definition: The first step involved defining the DataFrame schema to optimize memory usage.
2. Lazy Data Load by Default: Lazy loading was used by default, meaning that data was only loaded when needed, avoiding unnecessary memory consumption.
3. No Caching or Persistence: Caching and persistence were deliberately avoided, ensuring that data was not stored in memory, thereby conserving resources.
4. Data Volume Control: To keep data volume in check, data was loaded and manipulated on an as-needed basis, avoiding unnecessary in-memory storage.

These measures helped optimize memory usage during data processing.

### PySpark Time Optimization

1. Exclusive SparkSession: I allocated memory exclusively for a dedicated SparkSession, separate from the execution environment of memory-optimized functions.
2. Explicit Memory Allocation: Within these sessions, I configured specific memory allocations for Spark Storage Memory and Spark Execution Memory.
3. Optimization Based on Reports: After analyzing job execution reports in the Spark Web UI, I determined the most suitable moments to apply caching and in-memory persistence.
4. Working in Bottlenecks: I focused on optimizing the execution time of functions at bottleneck points to improve overall performance.

### Q1 Transformations

1. As my first step, I conducted a basic date-wise tweet count analysis to identify the dates with the highest tweet volumes.
2. After pinpointing the dates with maximum tweet volume, I performed an inner join with my original dataframe to reduce data volume for subsequent phases of my implementations.
3. By obtaining the top 10 dates with the highest tweet counts, I created an analytical window function to rank the users who tweeted on these top 10 days.
4. Afterward, it was straightforward to identify the user with the top rank. In the event of a tie, the tie-breaker criterion was the alphabetical order of usernames.

### Q2 Transformations

1. By using the Python Emoji Library version 1.4.1, I was able to apply the emoji regex function to extract all the emojis contained within the 'content' column;
2. To accomplish this, I declared a local function named 'extract_emojis' inside the 'q2_memory' and 'q2_time' functions. This function was later converted into a Spark User Defined Function (UDF). While it's generally considered a best practice to declare UDFs at the SparkSession level, for this case solution, i opted to run inside my Q2 funtions to better manipulate my SparkSessions;
3. With the UDF in place, aggregating and counting the emojis found in the data files became a straightforward task.

**Future Improvements**

1. UDF reduce PySpark performance, and make harder to optmize codes outside Spark Environment, to avoid that, is a good practice to develop your own Emoji regex reading expression by using PySpark internal functions.

### Q3 Transformations

1. By using a regex expression to identify mentions in the content column, I extracted all mentioned users in tweets using the PySpark SQL function regexp_extract with a tweet mention regex pattern.
2. To transform my resulting DataFrame into a user mentions DataFrame, it was necessary to collect mentions in step 1 in an array format for subsequent exploding.
3. After that, it was straightforward to count and order my data to answer the question.

### Analysis

For this particular case, I will create two different configurations for SparkSessions:

1. The first one, named "FarmersProtestTweets" will have the default SparkSession configuration for memory allocation to executors and drivers.
2. The second one, "FarmersProtestTweetsOptimization," will allocate 2GB of memory to executor and 8gb to storage.

In the initial analysis, there were no significant differences in time and memory usage between the real dataset and the 2.2GB dataset in the Q1 memory and time solutions. To gain a better understanding of the solution, I will conduct a more in-depth analysis using a 22GB dataset.

The main results can be found in "src/challenge.ipynb."

**Future improvements**

1. Analyzing the Spark UI for all three question scenarios is time-consuming. Therefore, I decided to extrapolate the analysis conducted in Q1 to Q2 and Q3.
2. While there are different types of data manipulation in all three questions, my technique for optimizing time and memory would be the same for now. I recommend exploring other data optimization techniques in PySpark (https://spark.apache.org/docs/latest/tuning.html).

## Conclusions

The primary goal of this case solution was to explore memory usage and optimization in a distributed and scalable data processing environment, such as Spark. To achieve this objective, the solution was grounded in the performance analysis of a Spark environment in scenarios with varying data volumes.

The default configuration of a PySpark session without optimizations was used as a control to identify the main bottlenecks that needed optimization. It was identified that in cases involving the reading of simple, unpartitioned data formats like CSV, the primary bottleneck occurred during the initial read due to the time required for resource allocation for the DataFrame, which couldn't leverage parallelism due to the original data structure.

By employing in-memory and disk caching techniques, it was possible to observe a significant reduction in the execution time of these operations, while also increasing the utilization of JVM memory.

To make this solution reproducible and scalable, a Docker image was created, implementing a Jupyter repository image containing a pre-configured PySpark environment. The decision to use a pre-made image presented challenges for various other implementations, including unit testing during the build process.

The implementation of the CI pipeline made it possible to have this environment ready for automated deployment. However, there were instances of build failures due to the difficulty of implementing unit tests during the build process with the chosen Docker image.

With the goal of creating a TDD-based process, test cases were implemented for each of the questions, using mocked datasets to validate the results during development. I encountered difficulties in generating expected results for my tests using the ChatGPT console. At this point, there was a deviation in the test scenario construction process to maintain a suitable TDD flow in question development.

After an initial data analysis, it was found that the best approach for using this data would be to create the concept of Staging since most of the provided data was disposable for meeting the challenge's solution. Therefore, I developed a preliminary stage of data creation in the quality layer at the Staging (Silver) level.

With the assistance of ChatGPT, it was possible to easily develop the necessary transformations to meet the challenge, guided by TDD.

I set up an environment for infrastructure resources to be provisioned through Infrastructure as Code (IaC) within the application's context.

All of this development was carried out in accordance with my planned Gitflow. However, there were numerous incorrect commits, and I found it challenging to manage on my own. These issues arose due to shortcomings in my initial planning of the Gitflow workflow.

Finally, using the set of techniques implemented in this repository, it was possible to meet the challenge's requirements!



## Bonus - Infra as Code

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
