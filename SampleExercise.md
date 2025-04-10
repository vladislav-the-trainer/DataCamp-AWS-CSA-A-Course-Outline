# Sample Exercise: Invoking a Lambda function using an Amazon API Gateway - Currency Converter

## Objective

In this hands-on lab, you will build an HTTP API that triggers a Lambda function. The function will convert a fixed amount of 1 USD into multiple other currencies using real-time conversion rates from an online source. You’ll test the API endpoint using the curl command-line tool. This exercise will help you validate your ability to create and configure one of the most common and powerful API Gateway setups.

## Instructions

### Step 1

Once logged in, Once logged in, you will have access to the AWS Management Console. Here, you will see several different widgets, including recently visited services, applications in the current region, getting started information, and much more.

To proceed, click hamburger menu (-☰ -), click **All sevices** and select **API Gateway** in **Networking & Content Delivery** section.

### Step 2

Here, you will see API gateway types available for creation. Take some time to read the description of each option available. We will need to create HTTP API for our integration.

* Click **Build** button in **HTTP API** section
* Specify the name of the new API (f.e. "convert_currency_http_api") and click **Next** button
* Click **Next** button twice to skip stages and routes configuration, we will do it later
* Click **Create** button

### Step 3

It is time to create our API route that will be used in the final URL.

* Click **Create** button in **Routes** section
* Choose **GET** as a method and type route name (f.e. "usd_converter")
* Click **Create** button

### Step 4

Now we need integrate the **GET** method with existing Lambda function.

* Choose newly created **GET** method under the route name and click **Create and attach an integration** button
* Choose integration type **Lambda function** from the drop-won list
* Find Lambda Function which name ending with "USD_Converter" and choose it
* Click **Create** button

### Step 5

It will not be possible to deploy the API until we create at least one stage. We can confirm it in the following way.

* Click **Deploy** button in the right upper corner
* Click **Create a new stage**
* Specify a stage name (f.e. "dev")
* Click **Create** button

### Step 6

Finally, we can deploy our stage and check the result.

* Copy the Invoke URL
* Click **Deploy** button in the right upper corner
* Choose the **dev** stage from the list and click **Deploy** button
* Choose Windows menu in the lower left corner and click **Comand Prompt**
* Execute the command inserting the link copied from buffer in the follwoing way:

```
curl https://<api-id>.execute-api.<region>.amazonaws.com/dev/usd_converter
```

If you see an output similar to this one, congratulations—you have completed the task!

```
{"amount": 1.0, "base": "USD", "date": "2025-04-09", "rates": {"AUD": 1.6651, "BGN": 1.7708, "BRL": 6.0548, "CAD": 1.4188, "CHF": 0.84002, "CNY": 7.3498, "CZK": 22.787, "DKK": 6.7623, "EUR": 0.90539, "GBP": 0.78257, "HKD": 7.7542, "HUF": 370.24, "IDR": 16944, "ILS": 3.8131, "INR": 86.67, "ISK": 131.37, "JPY": 144.51, "KRW": 1476.73, "MXN": 20.969, "MYR": 4.496, "NOK": 10.9728, "NZD": 1.7997, "PHP": 57.439, "PLN": 3.8889, "RON": 4.5067, "SEK": 10.024, "SGD": 1.3475, "THB": 34.505, "TRY": 38.01, "ZAR": 19.7157}}
```

### Question: Types of APIs

Which of the following types of APIs can you create using Amazon API Gateway?

- A. SOAP API  
- B. REST API  
- C. WebSocket API  
- D. HTTP API  

**Correct Answers:**  
✅ B. REST API  
✅ C. WebSocket API  
✅ D. HTTP API  
