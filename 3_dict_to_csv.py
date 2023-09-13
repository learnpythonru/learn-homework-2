"""

Домашнее задание №2


"""

import csv

people_list = [
    {"name": "Mark", "age": 21, "job": "lawyer"},
    {"name": "Anne", "age": 35, "job": "sailor"},
    {"name": "Peter", "age": 39, "job": "web-designer"},
    {"name": "Lada", "age": 18, "job": "personal manager"},
    {"name": "Misha", "age": 25, "job": "economist"}
]

def main():
    with open("people.csv", "w", encoding="utf-8") as output_file:
        fields = ["name", "age", "job"]
        writer = csv.DictWriter(output_file, fields, delimiter=";")
        writer.writeheader()
        for person in people_list:
            writer.writerow(person)

if __name__ == "__main__":
    main()
