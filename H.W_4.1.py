lst = [1, 0, 13, 7, 0, 5, 7, 0, 0, 0, 5]
new_lst = []
#знаходимо кількість елементів
zero = lst.count(0)
#проходимо по всіх елементах списку і створюємо умову
for el in lst:
    if el != 0:
        new_lst.append(el)
lst.clear()
# додаємо 0 в кінець списку за допомогою extend
lst.extend(new_lst + [0] * zero)
print(lst)
