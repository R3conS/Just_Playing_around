Feature: Test Orkikar Redirections
 
Scenario: Testing logo redirection to the index page
  Given I'm in /assurance-auto
  When I Click on the logo
  Then It should redirect me to the / page


Scenario: Testing Code de la route redirection
  Given I'm in /assurance-auto
  When I Click on the Code de la route text
  Then It should redirect me to the /code page


Scenario: Testing Permis de conduite/ Permis B redirection
  Given I'm in /assurance-auto
  When I Hover on the Permis de conduire text
  Then It should open a drop items
  When I Click on Permis B
  Then It should redirect me to /permis page
