list_a = ['Murzik', 'Barsik', 'Pantera']

#for x in range(len(list_a)):
#    print(list_a[x], sep=', ', end=' ')

print(f"{', '.join([str(i) for i in list_a])}")
