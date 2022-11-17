services1 = {"ftp": 21, "ssh": 22, "smtp": 25, "http": 80}
print("printing services1 dic", services1)

services2 = {"ftp": 21, "ssh": 22, "snmp": 161, "ldap": 389}
print("printing services2 dic", services2)

# merge two dictionaries
# update method will merge conflicting elements
services1.update(services2)
print("\nafter merging services1 with services2, printing services1\n", services1)

# change value
services1["http"] = 8080
print("\n\nprint changed values by key", services1)

# length function
print("\n\nservices1 length is:\n ", len(services1))

# get all the keys in the dictionary
print("\n\nprint all keys only\n", services1.keys())

# get all items
items = services1.items()
print("\n\nall items in the dictionary\n", items)

# sort dictionary elements in ascending order
items: dict = dict(sorted(items))
print("\nascending order\n", items)

# loop through dictionary
for key, value in services1.items():
    print("key: ", key)
    print("value", value)

# adding value
print("\n\nbefore adding\t", services1)
services1["https"] = 443
print("after adding\t", services1)
