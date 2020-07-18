
list = ['../talkmovie_qq/qq_free.txt','../talkmovie_qq/qq_charge.txt',
        '../talkmovie_pptv/pptv_free.txt','../talkmovie_pptv/pptv_charge.txt',
        '../talkmovie_youku/youku.txt',
        '../talkmovie_iqiyi/iqiyi.txt','../talkmovie_iqiyi/iqiyi_charge.txt']

film_set = set()
for f in list:
    with open(f) as file:
        for line in file:
            try:
                json = eval(line)
                print(json['name'])
                film_set.add(json['name'])
            except Exception as e:
                print("异常")
                print(e)
    file.close()

print(film_set.__len__())
for film_name in film_set:
    with open('collect_film_name.txt', "a") as file:
        try:
            file.write(film_name + "\n")
        except e:
            print(e)
    file.close()

