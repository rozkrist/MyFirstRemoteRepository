import json

person = {
     "name":"Jack",
     "last_name":"Green",
     "age":20
 }
with open("Persons.json","w") as f:
     json.dump(person,f)

