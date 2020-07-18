import json

# json.load && json.loads diff
jsonStr = '{"name":"aspiring", "age": 17, "hobby": ["money","power", "read"],"parames":{"a":1,"b":2}}'
print(json.loads(jsonStr))

with open("test.json", "rb") as f:
    print(json.load(f))
f.close()
