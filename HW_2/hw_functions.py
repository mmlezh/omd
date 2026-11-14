import csv


def read_employees(filename):
    with open(filename, encoding='utf-8', newline='') as file:
        return list(csv.DictReader(file, delimiter=';'))


def hierarchy(employees):
    teams_by_department = {}

    for employee in employees:
        department = employee['Департамент']
        team = employee['Отдел']

        if department not in teams_by_department:
            teams_by_department[department] = set()

        teams_by_department[department].add(team)

    department_hierarchy = {
        department: sorted(teams)
        for department, teams in sorted(teams_by_department.items())
    }

    for department, teams in department_hierarchy.items():
        print(f'Команды департамента \'{department}\':')
        for team in teams:
            print(f'\t -{team}')

    return department_hierarchy


def calculate_department_summary(employees):
    salaries_by_department = {}

    for employee in employees:
        department = employee['Департамент']
        salary = int(employee['Оклад'])

        if department not in salaries_by_department:
            salaries_by_department[department] = []

        salaries_by_department[department].append(salary)

    department_summaries = []
    for department, salaries in sorted(salaries_by_department.items()):
        department_summaries.append(
            {
                'Департамент': department,
                'Численность': len(salaries),
                'Минимальный оклад': min(salaries),
                'Максимальный оклад': max(salaries),
                'Средний оклад': round(sum(salaries) / len(salaries), 2),
            }
        )

    return department_summaries


def department_summary_report(employees):
    department_summaries = calculate_department_summary(employees)

    column_titles = (
        'Департамент',
        'Сотрудников',
        'Мин. оклад',
        'Макс. оклад',
        'Средний оклад',
    )
    header = (
        f'{column_titles[0]:<15} {column_titles[1]:>11} '
        f'{column_titles[2]:>12} {column_titles[3]:>13} '
        f'{column_titles[4]:>15}'
    )
    print(header)
    print('-' * len(header))

    for department_summary in department_summaries:
        department = department_summary['Департамент']
        employee_count = department_summary['Численность']
        min_salary = department_summary['Минимальный оклад']
        max_salary = department_summary['Максимальный оклад']
        average_salary = department_summary['Средний оклад']
        print(
            f'{department:<15} {employee_count:>11} '
            f'{min_salary:>12} {max_salary:>13} {average_salary:>15.2f}'
        )

    return department_summaries


def write_department_summary(employees, output_filename):
    department_summaries = calculate_department_summary(employees)
    fieldnames = [
        'Департамент',
        'Численность',
        'Минимальный оклад',
        'Максимальный оклад',
        'Средний оклад',
    ]

    with open(
        output_filename, 'w', encoding='utf-8', newline=''
    ) as summary_file:
        writer = csv.DictWriter(
            summary_file, fieldnames=fieldnames, delimiter=';'
        )
        writer.writeheader()
        for department_summary in department_summaries:
            csv_row = department_summary.copy()
            csv_row['Средний оклад'] = format(
                department_summary['Средний оклад'], '.2f'
            )
            writer.writerow(csv_row)

    print(f'результат тут: {output_filename}')
    return output_filename


def main(
    report_number: int,
    input_filename='Corp_Summary.csv',
    output_filename='department_summary.csv',
):
    if isinstance(report_number, bool) or not isinstance(report_number, int):
        raise TypeError('номер отчёта должен быть целым числом')
    if report_number not in (1, 2, 3):
        raise ValueError('номер отчёта должен быть равен 1, 2 или 3')

    employees = read_employees(input_filename)

    if report_number == 1:
        return hierarchy(employees)
    if report_number == 2:
        return department_summary_report(employees)
    return write_department_summary(employees, output_filename)


if __name__ == '__main__':
    main(int(input('введите номер отчёта (1, 2 или 3): ')))
