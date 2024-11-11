import pickle

data = {}
grades = []
with open("data.csv","rt") as file :
    next(file)
    for line in file :
        line = line.split(", ")
        info = line[1:3] #+ line[4]?
        info.append(line[4])
        grade = line[3]
        prog_lang = line[5][:-1]
        if grade not in data :
            data[grade] = {}
        if prog_lang not in data[grade] :
            data[grade][prog_lang] = []
        data[grade][prog_lang].append(info)

with open("filtered_data.txt","wb") as file :
    pickle.dump(data,file)

with open("filtered_data.txt","rb") as file :
    data = pickle.load(file)
    for i in data :
        print(i,":")
        for j in data[i] :
            print("  ",end="")
            print(j,":")
            for k in data[i][j] :
                print("  ",end="")
                print(k)




