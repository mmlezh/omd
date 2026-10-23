import csv


def read_file(filename):
    with open(filename, newline="") as file:
        return list(csv.DictReader(file, delimiter=";"))


def hierarchy(employees):
    hierarchy = {}

    for employee in employees:
        department = employee["Департамент"]
        team = employee["Отдел"]

        if department not in hierarchy:
            hierarchy[department] = set()

        hierarchy[department].add(team)

    result = {
        department: sorted(teams)
        for department, teams in sorted(hierarchy.items())
    }

    for department, teams in result.items():
        print(f"команды департамента \'{department}\':")
        for team in teams:
            print(f"\t -{team}")

    return result


def calculate_department_summary(employees):
    salaries_by_department = {}

    for employee in employees:
        department = employee["Департамент"]
        salary = int(employee["Оклад"])

        if department not in salaries_by_department:
            salaries_by_department[department] = []

        salaries_by_department[department].append(salary)

    summary = []
    for department, salaries in sorted(salaries_by_department.items()):
        summary.append(
            {
                "Департамент": department,
                "Численность": len(salaries),
                "Минимальный оклад": min(salaries),
                "Максимальный оклад": max(salaries),
                "Средний оклад": round(sum(salaries) / len(salaries), 2),
            }
        )

    return summary


def department_summary_report(employees):
    summary = calculate_department_summary(employees)

    header = (
        f"{'Департамент':<15} {'Сотрудников':>11} "
        f"{'Мин. оклад':>12} {'Макс. оклад':>13} {'Средний оклад':>15}"
    )
    print(header)
    print("-" * len(header))

    for row in summary:
        print(
            f"{row['Департамент']:<15} "
            f"{row['Численность']:>11} "
            f"{row['Минимальный оклад']:>12} "
            f"{row['Максимальный оклад']:>13} "
            f"{row['Средний оклад']:>15.2f}"
        )

    return summary


def csv_summary_report(employees, output_filename):
    summary = calculate_department_summary(employees)
    fieldnames = [
        "Департамент",
        "Численность",
        "Минимальный оклад",
        "Максимальный оклад",
        "Средний оклад",
    ]

    with open(output_filename, "w", encoding="utf-8", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames, delimiter=";")
        writer.writeheader()
        for row in summary:
            row_for_csv = row.copy()
            row_for_csv["Средний оклад"] = f"{row['Средний оклад']:.2f}"
            writer.writerow(row_for_csv)

    print(f"результат тут: {output_filename}")
    return output_filename


def main():
    report_number = int(input())
    if report_number not in (1, 2, 3):
        raise ValueError("номер отчёта должен быть равен 1, 2 или 3")

    employees = read_file("Corp_Summary.csv")

    if report_number == 1:
        hierarchy(employees)
    elif report_number == 2:
        department_summary_report(employees)
    elif report_number == 3:
        csv_summary_report(employees, "department_summary.csv")


if __name__ == "__main__":
    main()
