import requests
import json

class MY_DATABASE:
    USER_AGENT = "Not Gonna Block ME XD"
    
    def get_employees(self):
        return requests.get('https://dummy.restapiexample.com/api/v1/employees', headers={"User-Agent": self.USER_AGENT})

    def get_employee_by_id(self, id):
        request_string = "https://dummy.restapiexample.com/api/v1/employee/" + id
        return requests.get(request_string, headers={"User-Agent": self.USER_AGENT})
    
    def create_employee(self, name, salary, age): # 	{"name":"test","salary":"123","age":"23"}
        employee_dict = dict(name = name, salary = int(salary), age = int(age) )
        employee_json = json.dumps(employee_dict)
        request_string = "https://dummy.restapiexample.com/api/v1/create"
        return requests.post(request_string, headers={"User-Agent": self.USER_AGENT}, json= employee_json)
    
    def update_employee_by_id(self, id):
        request_string = "https://dummy.restapiexample.com/api/v1/update/" + str(id)
        return requests.put(request_string, headers={"User-Agent": self.USER_AGENT}) 

    def delete_employee_by_id(self, id):
        request_string = "https://dummy.restapiexample.com/api/v1/delete/" + str(id)
        return requests.delete(request_string, headers={"User-Agent": self.USER_AGENT})
