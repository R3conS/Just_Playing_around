## Api presentation

The purpuse of an api ( application programming interface ) is to exchange data and fonctionality from different services.
In our case this api is used to manipulate a employe database


## Test Strategy 

/employees When running an endpoint we know the typical result so we can predict it
/employee/{id} Whe already know the employee with an id ( from employees )
/delete/{id} employee in question won't be visible in /employees


## Framework use ( PythonBehave )

|       Pros                    |           Con                          |
|-                              | -                                      |
|supports the Gherkin language  |  Sharing steps between feature files   |
|popular                        |                                        |

## Automatisation process

Playing with the existing api

## QA Report ??

## Project cmd 

python3 -m behave -s --no-capture --color