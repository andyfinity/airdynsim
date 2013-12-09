def printr(name, data, indent=0):
    print(name + ":")
    for data_i in data:
        print(" " * indent,data_i,"=",data[data_i])