my_dict = {'Denis':1999, 'Arina':2004, 'Lenya':2006}
print(my_dict)
print(my_dict['Denis'])
my_dict['Petr'] = 2015
print(my_dict['Petr'])
print(my_dict.get('Anatoly'))
my_dict.update({'Sasha':2011, 'Sonya':1879})
a = my_dict.pop('Lenya')
print(my_dict)
print(a)

my_set = {1, 2, 3, 1, 2, 1, 3, 'Denis', True}
print(my_set)
my_set.add(5)
my_set.add(6)
my_set.remove(2)
print(my_set)