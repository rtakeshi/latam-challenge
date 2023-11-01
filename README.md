# LATAM Challenge Solution

For challenge description go to: https://github.com/rtakeshi/latam-challenge/blob/main/latam-challenge.md

Day 1:  Defining scopes, CI pipeline creation, Docker image customization, project structure


## Infra

Using Terraform, I provisioned and created Google Cloud Storage to receive staging data.

**Future improvements**:

1. Declaring Cloud Build Trigger as Infrastructure as Code (IaC).
2. Provisioning and creating a Cloud Run instance to receive the built container from the Artifact Registry.
3. For this project, I will not implement VPC networking and IAM permissions. I will use a public Google Cloud Storage instance.

## Build - CI Pipeline for Artifact Registry


A CI pipeline was created via the Google Cloud Platform Console.

The main goal of this pipeline is to continuously build and integrate my container into the Artifact Registry.

Unit tests executions will be done in build time with cloud build.


**Future improvements**:

1. Infra should have its own repository and CI/CD pipeline with Terraform lifecycle.
2. The cloudbuild.yaml file is hard writen for my free trial account of GCP
3. We can implement DevSecOps at build time, incorporating SAST (Static Application Security Testing) to evaluate code vulnerabilities and test coverage, as well as SCA (Software Composition Analysis) to provide visibility into requirement vulnerabilities.

**Difficulties**: I faced some problems when building my container. These issues stemmed from my limited knowledge of how to use Docker Hub containers.

## Docker Container

Using the jupyter/pyspark-notebook image, I was able to build an environment ready for implementing PySpark and Jupyter Notebook. This enables us to maintain consistency in this environment across any machine, simplifying deployment.

**Difficulties**: When deciding to use a Docker Hub container, I encountered some permission issues when installing new packages in the operating system. To avoid future problems in execution, i decided to use the root user.

## Data Exploration


After the initial phase of exploration, it was identified that the "farmers-protest-tweets" file comprises multiple columns, and a schema was created in the "aux > tweet_payload_schema" file. During the discovery process, data curation was carried out to determine which columns would be utilized in the solutions for the questions.

**Disclaimer**: The data was found to be outdated in comparison to the Data dictionary provided by Twitter's documentation.

q1. Las top 10 fechas donde hay más tweets. Mencionar el usuario (username) que más publicaciones tiene por cada uno de esos días.

Columns: id, date, user.username


q2. Los top 10 emojis más usados con su respectivo conteo.

Columns: id, content


q3. El top 10 histórico de usuarios (username) más influyentes en función del conteo de las menciones (@) que registra cada uno de ellos. 

The "mentionedUsers" at the main tweet level appear to be filled with null values, necessitating the transformation of the content to retrieve the users.

Columns: id, content, user.username

After the data curation process, it was decided to create a staging table with only four columns:

-tweet_id

-tweet_date

-tweet_username

-tweet_content


## Data Transformation

For this purpose, a classical ETL approach will be implemented to extract columns that will be used in the solutions to the questions.

The resulting dataset will be stored in GCS to be read by the functions.

**Future improvements**

1. If this application begins to consume dynamic data, consider implementing an ELT approach.

## TDD - pytest

By using PyTest, I will implement one test scenario for each question's solution.

I will prepare a dataset in staging quality layer to apply the functions; Test datasets will be stored in GCS in the folder "test"; the development will be guided through those test cases.

**Future improvements**

1. It is important to create more test cases scenarios;
2. While data transformation tests are not included in this project, it is crucial to define appropriate scenarios for data integration testing, especially when dealing with dynamic data.


## Code Implementation

## Solution Analysis in Jupyter notebook

## Conclusion 


**Disclaimer**: This README.md file will be edited and committed outside of GitFlow. I will edit it whenever necessary to provide a clearer explanation of my solution.