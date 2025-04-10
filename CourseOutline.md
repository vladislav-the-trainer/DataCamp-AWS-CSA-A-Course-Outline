# Course Outline: API Management with AWS

## Course Description

Are you ready to take your AWS skills to the next level? Look no further than our comprehensive API Management with AWS course designed for anyone wanting to master the full lifecycle of building and managing APIs in the AWS cloud. You will dive deep into Amazon API Gateway configuration and learn how to create, integrate, secure, and monitor APIs with a help of powerful AWS services like Lambda and CloudWatch. With interactive labs and real-world examples, you will gain hands-on experience through the AWS console and build a fully functional serverless API from scratch, preparing you for real-world projects and AWS certifications.

## Prerequisites

- Basic understanding of AWS Lambda, IAM and CloudWatch
- Familiarity with HTTP/REST APIs and JSON
- Experience using the AWS Management Console

---

## Chapter 1: Getting Started with Amazon API Gateway

### Lesson 1.1: Introduction to Amazon API Gateways

- Learner will be able to navigate the Amazon API Gateway console and access its main components
- Learner will discover the differences between stateless (REST, HTTP) and statefull (WebSocket API) deployments  
- Learner will be able to understand and apply the basic terminology used across the service (route, stage, resource, method etc.)

**Exercise**: Walk through the API Gateway service in the AWS Console. Explore the default settings for creating HTTP APIs.

### Lesson 1.2: Configuring HTTP APIs

- Learner will be able to configure a basic HTTP API and test it using a mock integration  
- Learner will be able to configure routes and test the endpoint using the AWS Console

**Exercise**: Create an HTTP API with a mock integration. Define a route and deploy it to a stage for public testing.

### Lesson 1.3: Testing API Gateway APIs

- Learner will be able to send API requests using Postman client and cURL command line tool  
- Learner will be able to explain the purpose of stages in API Gateway
  
**Exercise**: Use Postman and cURL to send GET requests to the API endpoint. Modify the stage name and re-deploy to see changes reflected.

---

## Chapter 2: Building a serverless app with API Gateway and Lambda

### Lesson 2.1: Invoking a Lambda function using an Amazon API Gateway

- Learner will be able to create a Lambda function that manipulates the provided data and perform the external call
- Learner will be able to connect the Lambda function to an HTTP API route  

**Exercise**: Integrate API Gateway HTTP route with a Lambda function that converts 1 USD to several other currencies and return the result. Test it with cURL.

### Lesson 2.2: Handling Input Parameters

- Learner will be able to pass query string parameters to Lambda via API Gateway
- Learner will be able to validate and transform request inputs in Lambda

**Exercise**: Modify your Lambda function to extract passed value from query string parameters. Add logic to return results based on thу input.

### Lesson 2.3: Returning JSON Responses

- Learner will be able to return JSON-formatted responses from Lambda to the client  
- Learner will understand how to handle different status codes and response structures

**Exercise**: Configure your Lambda function to return a structured JSON response. Include fields like converted amount, original currency, and timestamp.

### Lesson 2.4: Improving API Robustness

- Learner will be able to manage errors within the Lambda function  
- Learner will be able to return appropriate error messages and codes using API  

**Exercise**: Add error handling to a Lambda function to address missing parameters and unsupported values. Return proper HTTP error codes and messages.

---

## Chapter 3: Securing and Managing Access

### Lesson 3.1: API Keys and Usage Plans

- Learner will be able to configure API Gateway to use an API key  
- Learner will be able to create a usage plan and associate it with an API key  

**Exercise**: Create REST API and enable API key authorization on it. Create and attach a usage plan to enforce request limits.

### Lesson 3.2: Controlling multiple environments

- Learner will be able to create and deploy multiple stages for different environments  
- Learner will be able to manage access across development, testing, and production APIs  

**Exercise**: Create "test" and "prod" deployment stages for API. Add stage-specific configurations such as different Lambda aliases or log settings.

### Lesson 3.3: Rate Limiting and Throttling

- Learner will be able to apply throttling settings to control API usage  
- Learner will be able to use diffrent types of throttling-related settings for API 

**Exercise**: Apply a per-client throttling limit for the specific API key. Simulate multiple requests and check the change in the API behaviour.

---

## Chapter 4: Monitoring and Managing APIs

### Lesson 4.1: Logging and Observability

- Learner will be able to enable CloudWatch logging for API Gateway 
- Learner will be able to locate and investigate related logs  

**Exercise**: Configure CloudWatch logging for API Gateway. Trigger the API and check CloudWatch for request/response details.

### Lesson 4.2: Viewing API Metrics

- Learner will be able to use CloudWatch to analyze metrics such as latency and error rates  
- Learner will be able to set alarms based on API usage metrics  

**Exercise**: View API Gateway metrics in CloudWatch such as latency, error count, and request count. Set an alarm to notify when error rates spike. Trigger an alarm and observe the resulting notifications.

### Lesson 4.3: Versioning and Rollback Strategies

- Learner will be able to roll back environments to previous versions  
- Learner will understand how to work with stage variables and deployment history

**Exercise**: Apply a change to API with Lambda functions in backend. Roll back to a previous version using deployment history and confirm behavior change.
