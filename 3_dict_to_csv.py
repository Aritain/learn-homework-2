"""
Домашнее задание №2

Работа csv

1. Создайте список словарей с ключами name, age и job и значениями по вашему выбору. В списке нужно создать не менее 4-х словарей
2. Запишите содержимое списка словарей в файл в формате csv

"""

import csv

def main():
	people = [
		{'name': 'David', 'age': '20', 'occupation':'Engineer'},
		{'name': 'Rosa', 'age': '25', 'occupation':'Accountant'},
		{'name': 'Marc', 'age': '30', 'occupation':'Lawyer'},
		{'name': 'Ingrid', 'age': '35', 'occupation':'Doctor'},
		{'name': 'Lewis', 'age': '40', 'occupation':'Manager'},
	]
	with open('people.csv', 'w', newline='') as file:
		fields = ['name', 'age', 'occupation']
		writer = csv.DictWriter(file, fields, delimiter = ';')
		writer.writeheader()
		for person in people:
			writer.writerow(person)

if __name__ == "__main__":
	main()
