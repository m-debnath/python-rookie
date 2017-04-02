# This file is for learning strings
var="Hello world!"
print(var)

# getting substring From to To-1
var1="Mukul778"
var2="Software Testing"
print("var1[0]:",var1[0]);
print("var2[1:9]:",var2[1:9])
print("warez" in var2)
print("-" * 40)

newvar = var.replace("ello", "4444")
print(newvar)
print(newvar.upper()) # Strings are immutable

joinedvar = "|".join(newvar)
print(newvar) # Strings are immutable
print(joinedvar)
print("".join(reversed(joinedvar)))
print(joinedvar.split("|"))

split_list = var.split(" ")
print(split_list)

osplit_list = var.split("o")
print(osplit_list)