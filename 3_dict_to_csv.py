import csv


def main():
    table_for_csv = [
        {'name' : 'Sweeney', 'age' : 29, 'job' : 'Barber'},
        {'name' : 'Judas', 'age' : 52, 'job' : 'Priest'},
        {'name' : 'Harry', 'age' : 42, 'job' : 'Wizard'},
        {'name' : 'Diana', 'age' : 61, 'job' : 'Princess'},
    ]
    filename = 'candidates.csv'
    columns = ['name', 'age', 'job']
    with open(filename, 'w', encoding='utf-8', newline='') as file_handler:
        writer = csv.DictWriter(file_handler, columns, delimiter=';')
        writer.writeheader()
        for candidate_cv in table_for_csv:
            writer.writerow(candidate_cv)


if __name__ == "__main__":
    main()
