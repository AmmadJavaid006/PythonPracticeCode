dictionery = {

    "table" : ["a piece of furniture", "list of facts and figures"],
    "cat" : "small animal"

}

print(dictionery)

print("Table's meaning only " + str(dictionery.get("table")))
print("Cat meaning only is " + str(dictionery.get("cat")))


set = {"python", "java", "C++", "python", "javascript"
        "java", "python", "java", "C++", "C"}


print("Subjects are: " + str(set))
print("Classrooms needed are: " + str(len(set)))
