from employee.employee import Employee, Boss

if __name__ == '__main__':
    employee_1 = Employee('Damian', 27, 1000, 'podstawowe')
    employee_1.introduce_yourself()
    employee_2 = Employee('Adam', 40, 2000, 'średnie')
    employee_2.introduce_yourself()
    employee_3 = Employee('Piotr', 24, 1500, 'średnie')
    employee_3.introduce_yourself()
    boss = Boss('Arek', 55, 5000, 'Jestem tu bossem')
    boss.introduce_yourself()
    boss.add_employee(employee_1)
    boss.add_employee(employee_2)
    boss.add_employee(employee_3)
    print(boss.employee_list)
