﻿Serverless Web App with Amplify, API Gateway, Lamda and DynamoDB
 
An overview. 
The body mass index (BMI) app can be incredibly useful for individuals aiming to track their health and fitness by calculating their BMI, a measure of body fat based on height and weight. 

Here's how each AWS service contributes to developing this BMI app:
AWS Amplify: Aws amplify was used to facilitate building and deploying web applications easily,  and hosting of the BMI application's user interface.

AWS Lambda: I used the Aws Lambda to execute code in response to events, and  to perform computations and logic for BMI calculations based on input data.

IAM (Identity and Access Management): This very important service was used to manage access to AWS services and resources, ensuring secure control over who can access and modify the application and its data.

DynamoDB: To ensure the app was serverless , I used this database service used to store and manage the BMI application's data, such as user names,  weight, height, and deduced BMI (body mass index).

![app architecture](https://github.com/iykecharles/AWS-Projects/assets/69170598/48da114a-1b8e-4b5d-ba06-66ecc718b692)


Firstly, i connected my source code(index.html)  from my local drive then inputted some  basic information like the app name (bmi, in this case), environment name, and then dragged and dropped the source code in the stilulated area. The code was deployed within seconds to display the initial web application without the backend.

![Screenshot (10)](https://github.com/iykecharles/AWS-Projects/assets/69170598/b27df7bb-7b4b-497b-8577-32c0ab5205a4)

![Screenshot (11)](https://github.com/iykecharles/AWS-Projects/assets/69170598/8f98762c-2eea-45c4-bfe7-c28f717c1fc3)


![Screenshot (12)](https://github.com/iykecharles/AWS-Projects/assets/69170598/097a40ae-7566-40f3-836a-996ebc06312a)

Next, I proceeded to set up my lambda function which would handle the business logic for the various functionalities of the body mass index application. The lambda function executed codes in response to events triggered by the user actions. That is, when a user inputs his weight and height, the lambda function would perform calculation for the body mass index. It also interacts with the dynamodb database by writing the data(height, weight, name) to the database. I eventually connected the lambda to the API gateway endpoints so that when a user interacts with the app at the frontend, the lambda function is triggered allowing a seamless interaction with the backend (database) .  I chose python as my programming language to write the function. 

![Screenshot (13)](https://github.com/iykecharles/AWS-Projects/assets/69170598/f485ea68-5843-4fdc-846a-7310eec01179)

The rest API used here allows for interaction between client side (web browser) and the server side(lambda functions, dynamodb). That is, a user inputs his data and the rest API sends the request to the backend for processing.

![Screenshot (14)](https://github.com/iykecharles/AWS-Projects/assets/69170598/140a2b95-8620-4619-8815-eee1e8f3fb37)

![Screenshot (15)](https://github.com/iykecharles/AWS-Projects/assets/69170598/dae5b6f1-bcf4-43e8-8032-b535bf7cdd83)

To submit user input for the BMI app, the http method "POST" was used to ensure that data is sent to the server and to calculate and process the BMI on the server side.

![Screenshot (16)](https://github.com/iykecharles/AWS-Projects/assets/69170598/799d2e63-ea93-4a16-ab1e-1d451a38b908)

The crucial CORS was activated to allow the BMI app to be hosted on one domain and still be able to request or access hosted on different domains.  This ensures the BMI app would function properly as it interacts with APIs with security breach.

![Screenshot (18)](https://github.com/iykecharles/AWS-Projects/assets/69170598/2fee6e7f-ad60-4d45-9247-07b76e4bbf71)


![Screenshot (19)](https://github.com/iykecharles/AWS-Projects/assets/69170598/8cc0c9d0-2748-4d1d-8e6b-3fb1b3b7987a)

CORS created. Next step is to deploy the API. 

![Screenshot (20)](https://github.com/iykecharles/AWS-Projects/assets/69170598/a7101627-939e-43d8-9376-00e9a9c4b68b)

DynamoDB

To store our user data, I chose the dynamodb for this project because of its robustness and scalability feature which would facilitate swift data retrieval and data management within the app. Another reason I chose DynamoDB is that it is a fully managed and serverless NoSQL database service provided by AWS. It automatically scales based on demand and doesn't require provisioning or managing servers. Dynamodb also integrates with other AWS services seamlessly, and is reliable with in-built replication and backup features. I created the table named "bmi_table" and used the "name" of the app users as the table's primary key.


![Screenshot (21)](https://github.com/iykecharles/AWS-Projects/assets/69170598/6f009c35-54a7-4bc6-ad75-ba74958d4bac)

![Screenshot (22)](https://github.com/iykecharles/AWS-Projects/assets/69170598/d7b39262-1852-49cc-bb9d-5abff32514fe)

Lambda, DynamoDB and IAM integration. 

After the table was created, i put the name of the created table(bmi_table) in my lambda fucntion and had to give the necessary permissions to my lambda functions to enablew it carry out its role. Within the IAM , I configured the necessary permissions which would grant my lambda function access  to the DynamoDB table. The permissions created was to perform the read, write, update, scan, delete and query functions.  

![Screenshot (24)](https://github.com/iykecharles/AWS-Projects/assets/69170598/fbe66fa0-fc82-489a-8642-b127a0758093)

![Screenshot (25)](https://github.com/iykecharles/AWS-Projects/assets/69170598/72763eed-9b4d-4788-9935-e5ffb1175d78)

![Screenshot (26)](https://github.com/iykecharles/AWS-Projects/assets/69170598/ff500ac1-c137-4d9f-bf39-f7927c0fc508)

Following that, I conducted a thorough test of my lambda function using various test values to ensure that everything was functioning correctly at that stage.

![Screenshot (27)](https://github.com/iykecharles/AWS-Projects/assets/69170598/0c466d63-799f-44a6-bf8a-e1565875f40c)

Testing was okay. Hurrah! 💃💃💃

![Screenshot (28)](https://github.com/iykecharles/AWS-Projects/assets/69170598/1e1b1192-7c28-4bb2-bd27-62ccf0a56407)

Had to check the created table to see if the data was correctly stored in the created table "bmi_table". And it was. 

![Screenshot (29)](https://github.com/iykecharles/AWS-Projects/assets/69170598/5404ee73-78d9-4a1b-b4f6-0fd9970e819c)

![Screenshot (30)](https://github.com/iykecharles/AWS-Projects/assets/69170598/989cb63b-661c-4169-8169-964476c1f60d)

API Gateway, lambda and DynamoDB integration. 

In order to establish a connection between the frontend and backend, I needed to revise the API Gateway ARN (Amazon Resource Name) within my index.html file. I took this very crucial step to ensure that the frontend can communicate with the backend services, allowing my BMI app's user interface to effectively interact with the Lambda functions and DynamoDB table through the API Gateway, enabling seamless data exchange and functionality.

![Screenshot (31)](https://github.com/iykecharles/AWS-Projects/assets/69170598/9101d0bf-2ff9-4d01-93d6-2402a40981cb)

Then I dragged and dropped  the updated index html file on AWS Amplify for final deployment.

![Screenshot (32)](https://github.com/iykecharles/AWS-Projects/assets/69170598/4acef3cf-8ac4-400a-bf7f-6220f88e840b)

![Screenshot (33)](https://github.com/iykecharles/AWS-Projects/assets/69170598/1242f559-1c96-4af7-a041-94624cf049f4)

And our page is ready!

![Screenshot (34)](https://github.com/iykecharles/AWS-Projects/assets/69170598/b80d90aa-d376-430c-a04d-543413acc1e5)


Testing the page to confirm that my user data would be stored in the database. And it was so.

![Screenshot (35)](https://github.com/iykecharles/AWS-Projects/assets/69170598/3fd0addc-360e-4ef4-b445-c2fb6a3e0f2e)

![Screenshot (37)](https://github.com/iykecharles/AWS-Projects/assets/69170598/6cfdf298-8a2a-4d6c-8334-0c510c8cb9f7)

