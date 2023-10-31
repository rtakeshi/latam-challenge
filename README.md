# LATAM Challenge Solution

For challenge description go to: https://github.com/rtakeshi/latam-challenge/blob/main/latam-challenge.md


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

## Docker Container

Using the jupyter/pyspark-notebook image, I was able to build an environment ready for implementing PySpark and Jupyter Notebook. This enables us to maintain consistency in this environment across any machine, simplifying deployment.


## TDD - pytest

By using PyTest, I will implement one test scenario for each question's solution.

I will prepare a dataset in staging quality layer to apply the functions; Test datasets will be stored in GCS in the folder "test"; the development will be guided through those test cases.

**Future improvements**

1. It is important to create more test cases scenarios;
2. Data transformations tests will not be implemented.


## Exploratory Data Analysis and Data Transformation

For this case purpose an classical ETL approach will be implemented; 

I will use the Exploratory Data Analysis to discover how to develop the tests cases;

**Future improvements**

1. If this application begins to consume dynamic data, consider implementing an ELT approach.

## Code Implementation

## Solution Analysis in Jupyter notebook

## Conclusion 


**Disclaimer**: This README.md file will be edited and committed outside of GitFlow. I will edit it whenever necessary to provide a clearer explanation of my solution.