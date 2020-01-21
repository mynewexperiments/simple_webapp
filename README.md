# Steps to run the web application

## Introduction

  A simple web service using Python Flask that listens to **Webhook events** to know when a repository has been created.
  For this example i have created a webhook event *Repository* .
  
## Create & configure a server

   You will need to expose your local host with port:5000 to the internet. I used **ngrok**  --> recommended by Github
   (https://developer.github.com/webhooks/configuring/#using-ngrok)
   ngrok would provide you a forwarded url --> use this as a **Payload Url** for the next section
   
## Create & configure Github webooks

  To create a Repository webhook please follow the documentation below
  (https://developer.github.com/webhooks/)
  For this you would need the **Payload Url** created above.
    
## Test the application

  - Create a Orgnaisation in **Github**
  - Create a python3 Virtualenv
  - pip install -r **requirements.txt**
  - Run pytests --> py.test tests
  - Start the python Flask application locally by executing the package **app.py** 
  - Create one or more repositories in the **org** with *Readme.md* as the first commit --> This would create a **Master branch**
  
  Once the branch is created, Flask App would automatically trigger the **update-branch-protection** Github Api and apply
  master branch protection on all **Repositories**
  
  - Two branch protection packages are available
    One that loops through all the branches and applies protection
    Another by passing in the args --> set, add, del
  
## Tests
    
   Unit tests are created to check the **route** & **health** of the Api
   
## Some References used

    (https://github.com/BrinnerTechie/github-branch-protection-rules)
    (https://stackoverflow.com/questions/51020398/github-api-enable-push-restrictions-for-branch)
   
## Next Steps or Improvements

  - Build A CI pipeline 
  - Upgrade Github Rest Api 3 --> GraphQL API v4
  - Add more tests(mock payload response) to improve code quality
  - Create a workflow Automate
    
  
  

