#A tuple is like a list, except its size cannot change and
#  cannot add more elements than originally specified.

# The parentheses delimit a tuple.
tuple=("ftp","ssh","http","snmp")
print("print tuple value at position 1", tuple[0])
#change value to uppercase
tuple[0]="FTP"

#error
# Traceback (most recent call last):
#   File "/home/isuru/Projects/Python/03-tuples.py", line 8, in <module>
#     tuple[0]="FTP"
# TypeError: 'tuple' object does not support item assignment

