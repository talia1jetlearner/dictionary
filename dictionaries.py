d= {
    "name":"jessica",
    "age":14,
    "country":"germany"
}
print(d)
print(d.keys())
print(d.values())
print(d["country"])
for i in d.keys():
    print(i,d[i])

if "country" in d :
    print (d["country"])
else:
    print("key does not exist")
d["profession"]="student"
print(d)    
d["age"]=19
print(d)
d["marks"]=[86,56,76]
print(d["marks"][1])
#nested dictionary
classroom={
    "dylan":{
        "age":13,
        "marks": [67,45,87]
    },
    "rebecca":{
        "age": 16,
        "marks": [98,96,93]
    }
}
print(classroom.keys())
print(classroom.values())
