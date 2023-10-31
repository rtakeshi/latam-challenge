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

**Future improvements**:

1. Infra should have its own repository and CI/CD pipeline with Terraform lifecycle.
2. We can implement DevSecOps at build time, incorporating SAST (Static Application Security Testing) to evaluate code vulnerabilities and test coverage, as well as SCA (Software Composition Analysis) to provide visibility into requirement vulnerabilities.

## Docker Container

Using the jupyter/pyspark-notebook image, I was able to build an environment ready for implementing PySpark and Jupyter Notebook. This enables us to maintain consistency in this environment across any machine, simplifying deployment.


## TDD - pytest

## Code Implementation

## Solution Analysis in Jupyter notebook

## Conclusion 


**Disclaimer**: This README.md file will be edited and committed outside of GitFlow. I will edit it whenever necessary to provide a clearer explanation of my solution.