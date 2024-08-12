immutable_var = (1, 2, 'Mercy', True)
print(immutable_var)
# immutable_var [0] = 100 не сработает, т.к. список является неизменяемым, а значит его нельзя изменить
mutable_list = [1, 2, 'Mercy', True]
print(mutable_list)
mutable_list[0] = 100
print(mutable_list)
semi = ([1, 2], 'Mercy', True)
print(semi)
semi[0][1] = 500
print(semi)