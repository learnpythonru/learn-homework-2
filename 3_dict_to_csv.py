import csv


def main():
    table_for_csv = [
        {'name' : 'Sweeney', 'age' : 29, 'job' : 'Barber'},
        {'name' : 'Judas', 'age' : 52, 'job' : 'Priest'},
        {'name' : 'Harry', 'age' : 42, 'job' : 'Wizard'},
        {'name' : 'Diana', 'age' : 61, 'job' : 'Princess'},
    ]
    with open('candidates.csv', 'w', encoding='utf-8', newline='') as candidates:
        columns = ['name', 'age', 'job']
        writer = csv.DictWriter(candidates, columns, delimiter=';')
        writer.writeheader()
        for candidate_cv in table_for_csv:
            writer.writerow(candidate_cv)
    candidates.close()


if __name__ == "__main__":
    main()
