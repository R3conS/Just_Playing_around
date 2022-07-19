Feature: Testing my api
 
Scenario: Creating an employee should make him appear in /employee
  Given /employee does not contain my employee(sami, 43000, 23)
  When I create my employee
  Then he should appear in the /employee request


Scenario: Deleting an employee should make him disappear in /employee
  Given /employee does contain my employee
  When I delete my employee
  Then he should not appear in the /employee request