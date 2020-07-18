import redis

r = redis.Redis(host='127.0.0.1', port=6379, decode_responses=True)
with open("qq_free.txt") as file:
    for line in file:
        try:
            print(line)
            json = eval(line)
            r.delete('qqfilm'+json['name'])
            r.set('qqfilm'+json['name'], str(json))
            print(json)
        except Exception as e:
            print("异常")
            print(e)
file.close()

#
with open("qq_charge.txt") as file:
    for line in file:
        try:
            print(line)
            json = eval(line)
            r.delete('qqfilm'+json['name'])
            r.set('qqfilm'+json['name'], str(json))
            print(json)
        except Exception as e:
            print("异常")
            print(e)
file.close()
r.close()
#
