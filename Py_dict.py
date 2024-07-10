dict = {

    "Name" : "Ammad Javaid",
    "Age" : 15,
    "School" : "Garrison Boys High School", 
    "Class" : 9,
    "Add" : "Apt 5D Askari 2 Lahore Cantt",
    "Subjects" : ["Maths", "Computer", "Chm", "Physics", "English"],
    "DOB" : "8 August 2009",
}

null_dict = {}

nested_dict = {

    "Name" : "Ammad Javaid",
    "Score" : {

        "Pyhs" : 90,
        "Chem" : 80,
        "Comp" : 95,

    }


}
dict["Name"] = "Ammad"
dict["Surname"] = "Javaid"
dict["Siblings"] = ("Fahad", "Saud", "Asad", "Anu")
print(nested_dict["Score"]["Comp"])

print(len(dict))
print(list(dict.keys()))
print(list(dict.values()))
print(list(dict.items()))

pairs = list(dict.items())
print(pairs[0])

print(dict["Name"]) # not good because it stops the execution of further got
print(dict.get("Name"))

dict.update({"Citi" : "Lahore", "Country" : "Pakistan", "Army Cheif" : "Asim Muneer"})

print(dict)