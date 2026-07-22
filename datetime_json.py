from datetime import datetime
now = datetime.now()
print(now.year)
print(now.month)
print(now.day)
print(now.hour)
print(now.minute)
print(now.second)
print(now.strftime("%d/%m/%Y"))
print(now.strftime("%H:%M"))
import json
person = {"name": "Borz",
          "age": 18,
          "country": "Pakistan"
}
json_data = json.dumps(person)
print(json_data)
import json
json_text = '{"name":"Borz","age":18}'
person = json.loads(json_text)
print(person)
print(type(person))