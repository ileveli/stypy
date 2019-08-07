def city_temp(**param):
    for key,value in param.items():
        print(key,value)

a = {'bj':'32c','sh':'28c','hf':'35c','wh':'36c'}

city_temp(**a)