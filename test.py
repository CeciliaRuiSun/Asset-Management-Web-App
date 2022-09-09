items = [{'category':'O1', 'name':'Table', 'quantity': 2},{'category':'O2', 'name':'Table', 'quantity': 2},{'category':'O3', 'name':'Table', 'quantity': 2},{'category':'O4', 'name':'Table', 'quantity': 2},{'category':'OT1', 'name':'Table', 'quantity': 2}]

r1 = next(filter(lambda x: x['name'] == 'Table', items), None)
r11 = next(filter(lambda x: x['name'] == '1', items), None)
r2 = filter(lambda x: x['name'] == 'Table', items)     # get an iterator
r22 = filter(lambda x: x['name'] == '1', items)

print(r1)
print(r11)


print(next(r2),next(r2),next(r2))       # pop the 1st, 2rd, 3rd record that matches
print("loop")
for x in r2:
    print(x)
#print(r22)




