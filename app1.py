first_name = input("First name:")
last_name = input("Last name:")
full_name = first_name + last_name
gender = input("Gender:")
yearofBirth = int(input("Year of birth:"))
ssn = input("SSN:")
address = input("Adress:")
yearOfDeath = 1996
age = yearOfDeath - yearofBirth

print("Name is {}".format(first_name))
print("Name and last name are {}. Age is {}. SSN is {}. Gender is{}. Adress is {}".format(full_name,
age,ssn,gender,address))
import json

kisi_dict = {"Name":first_name,
        "Surname:":last_name,
        "Gender":gender,
        "Year of birth":yearofBirth,
        "SSN":ssn,
        "adress":address,
        "Age:":age
        }

kisi_json = json.dumps(kisi_dict)

print(kisi_json)

with open('kisi.json', 'w') as json_dosya:
  json.dump(kisi_dict, json_dosya)

#--------------------------------------------------------------
#Order 

order1 = 225
order2 = 6420.5
order3 = 159.45

total = order1 + order2 + order3

print("Total:", total)



