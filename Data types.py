#List
values = [2, 3, "Madhuri", "Mahi", 1121, "Mahi"]
print(values[2])
values[2] = "MADHURI"
values.remove("Mahi")
print(values)
values.append("Aara")
print(values)  #[2, 3, 'MADHURI', 1121, 'Mahi', 'Aara']
print(values[0:5])  #[2, 3, 'MADHURI', 1121, 'Mahi']
values.insert(3, "Vinjamuri")
print(values)   #[2, 3, 'MADHURI', 'Vinjamuri', 1121, 'Mahi', 'Aara']
print(values[-1])  #Aara

#Tuple - same as list but immutable means not able to update/delete
val = (2, 3, "Madhuri", "Mahi", 11.21, "Aara")
print(val[5])

#Dictionary
Dic = {1: "Mahi", 2: "Madhuri", "3": "Aara", 4: 11.21}
print(Dic[4])
Dic[4] = "Aaradhya"
print(Dic)
Dict={}
Dict["First Name"] = "Madhuri"
Dict["Last Name"] = "Mahi"
Dict["Middle Name"] = "Aara"
print(Dict)
print(Dict["Middle Name"])
