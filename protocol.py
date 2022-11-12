class protocol(object):
 def __init__(self, name, number,description):
  self.name = name
  self.number = number
  self.description = description

 def getProtocolInfo(self):
  return self.name + " " + str(self.number) + " " + self.description
# class protocol(object):
#     def __int__(self, name, number, description):
#         self.name = name
#         self.number = number
#         self.description = description
#
#     def getProtocolInfo(self):
#         return self.name + " " + str(self.number) + " " + self.description

    # __init__, which represents the class constructor

    # Basically, the self keyword is a reference to the object itself and
    # provides a way for its attributes and methods to access it.
