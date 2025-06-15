values = []
for index in range(5):
    value = int(input(f"Number {index + 1}: "))
    values.append(value)

print("The first number is", values[0])
print("The last number is", values[-1])
print("The smallest number is", min(values))
print("The largest number is", max(values))
print("The average of the numbers is", sum(values) / len(values))

valid_users = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye',
               'swei45', 'BaseInterpreterInterface', 'BaseStdIn', 'Command',
               'ExecState', 'InteractiveConsole', 'InterpreterInterface',
               'StartServer', 'bob']
entered_user = input("Enter username: ")
if entered_user in valid_users:
    print("Access granted")
else:
    print("Access denied")
