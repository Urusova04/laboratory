users = ['user1', 'user2', 'user3', 'user1', 'user4', 'user2']
list_ = {
    "Общее количество": 0,
    "Уникальные посещения": 0}
# TODO Добавьте словарь и замените в нем нулевые значения статисчикой посещений
list_["Общее количество"]=len(users)
list_["Уникальные посещения"]=len(set(users))
print(list_)