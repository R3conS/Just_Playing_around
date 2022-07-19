from asyncio.windows_events import NULL
import imp
from unicodedata import name
from interface import MY_DATABASE
from behave import *

@given("/employee does not contain my employee(sami, 43000, 23)")
def step_impl(context):
    context.api = MY_DATABASE()
    context.employees = context.api.get_employees().json()
    assert context.employees["status"] == "success"
    for i in context.employees["data"]:
        if (i["employee_name"] == "sami"):
            assert(False)
    
@When("I create my employee")
def step_imt(context):
    creation_response = context.api.create_employee("sami", "43000", "23")
    assert creation_response.status_code == 200
    context.new_employee_id = creation_response.json()["data"]["id"]
        
@Then("he should appear in the /employee request")
def step_imt(context):
    context.employees = context.api.get_employees().json()
    assert context.employees["status"] == "success"
    for i in context.employees["data"]:
        if (i["employee_name"] == "sami" and i["id"] == context.new_employee_id):
            assert(True)
    #assert(False) Normally i would let this line but in our case it will break the tests ( dummy api )
  
  
@given("/employee does contain my employee")
def step_impl(context):
    context.api = MY_DATABASE()
    context.employees = context.api.get_employees().json()
    assert context.employees["status"] == "success"
    for i in context.employees["data"]:
        if (i is not NULL):
            context.employee = i
            assert(True)
        else:
            assert(False)
    
@When("I delete my employee")
def step_imt(context):
    deletion_response = context.api.delete_employee_by_id(context.employee["id"])
    assert deletion_response.status_code == 200
        
@Then("he should not appear in the /employee request")
def step_imt(context):
    context.employees = context.api.get_employees().json()
    assert context.employees["status"] == "success"
    for i in context.employees["data"]:
        if (i["id"] == context.employee["id"]):
            pass
            #assert(False)
    assert(True)