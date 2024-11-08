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
for i in data :
    print(i)
    for j in data[i] :
        print(j,data[i][j])


