protocolList = []
protocolList.append("ftp")
protocolList.append("ssh")
protocolList.append("smtp")
protocolList.append("http")

print("original list", protocolList)

#sort list in ascending order
protocolList.sort()
print("sorted list", protocolList)

#reverse the list
protocolList.reverse()
print("reversed list", protocolList)

#find the type
print(type(protocolList))

#find the length of the list
print(len(protocolList))

#access spefic position in the list
print("index of the ssh element in the list: "+str(protocolList.index("ssh")))

#remove an item
print("list before remove ssh", protocolList)
protocolList.remove("ssh")
print("list after remove ssh", protocolList)

#print whole list
print("\nprint whole protocol list")
for protocol in protocolList:
    print(protocol)

#get the number of ftp in the list
print("\nlist count", protocolList.count("ftp"))

# insert ssh at location 3"
print("\nlist before insert ssh", protocolList)
protocolList.insert(3,'ssh')
print("list after insert ssh", protocolList)

#return the last element from the list and also remove it
print("\nlist before pop", protocolList)
last=protocolList.pop()
print("list after pop", protocolList)
print("last element was", last)