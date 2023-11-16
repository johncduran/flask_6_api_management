# flask_6_api_management
HHA 504 Assignment 6


## Flask Setup
Setting up the flask app went more smoothly this time since there were no html or csv files that I had to integrate with it this time as I have noticed before that those would always give me issues when deploying.


I set up a home page to welcome anyone to my endpoint.


I then added a hello endpoint to test out how it would greet users once they input their names.


After that, I created another endpoint called /calculator that would allow a user to input any number they wanted and then it would multiply itself thus giving the output in json format.
![Creation of endpoints](Screenshots/Creation%20of%20endpoints.png)
![Calculator endpoint](Screenshots/Calculator%20endpoint.png)


I then confirmed that the output was indeed in json format by going to https://jsonlint.com/ and pasted the output in it to see if it was valid and it was.
![Json validation](Screenshots/Json%20validation.png)


## Flasgger Setup
With all of the endpoints I created in the app.py file I also added docstrings to provide the swagger documentation on how to read and explain how the endpoints function.


After that I at the top of the python file I added 'from flasgger import Swagger' to import the necessary library. Once I launched my app locally using 'python app.py' I went to the url and typed in /apidocs and was able to get the documentation generated based on my python file.
![Swagger documentation success](Screenshots/Swagger%20documentation%20success.png)

I also tested out the endpoint on this page by putting in a number into the calculator enpoint. 
![Swagger documentation test execution](Screenshots/Swagger%20documentation%20test%20execution.png)

## Azure Setup


I used the Google Shell terminal to allow my app to be run using the Azure Web App service. I used the command 'curl -sL https://aka.ms/InstallAzureCLIDeb | sudo bash' to install the Azure CLI. Then to confirm it installed properly I used the command 'az'. To allow access to Azure I used 'az login --use-device-code' and logged in using the code this command provided. Finally, I created a new resource group and gave my app a name using the following command 'az webapp up --resource-group <groupname> --name <app-name> --runtime <PYTHON:3.9> --sku <B1>'.
![Az Webapp creation](Screenshots/Az%20Webapp%20creation.png)


After all of this was done I then went into Azure itself to see that the resource group was created and the web app service was as well.


## Errors


There was only one error I faced when trying to launch the app through the Azure web app service. I was able to get the domain name for the web app https://john-api-endpiont.azurewebsites.net/. However, everytime I would open the link and wait for it to load it would give me an ":( Application Error". I then looked at the log stream to see what was causing the application to not launch properly.
![Az Webapp error](Screenshots/Az%20Webapp%20error.png)
![Az log stream](Screenshots/Az%20log%20stream.png)


With the first error I saw that there was an issue possibly with the requirements.txt file and trying to "import name 'Markup' from 'flask'" I then tried to change the file by changing 'flask' to 'Flask' as I thought that it might be a spelling issue, but that didn't fix it.


With the second error it said that it wasn't able to ping to port 8000 and so I added at the end of my python file to use port 8000 as I didn't specify it before. However, this didn't fix the issue either.
![Change in port connection](Screenshots/Change%20in%20port%20connection.png)


I then tried going into the settings in Configuration to see if it was a connection issue. I turned off SSH and HTTPS Only to see if those were causing it to not connect properly as it might be a security issue. However, that didn't fix it either. 
![Az configuration changes](Screenshots/Az%20configuration%20changes.png)

After trying all of these options this was one issue I couldn't fix.
