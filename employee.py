class Employee:

    def __init__(self, name, age, salary, title):
        self.name = name
        self.age = age
        self.salary = salary
        self.title = title

    def introduce_yourself(self):
        print('Cześć jestem', self.name, 'mam', self.age, 'lat', 'zarabiam', self.salary, 'złotych', 'i posiadam wykształcenie', self.title)

    def salary_incrise(self, value):
        self.salary = self.salary + value

    def __repr__(self):
        return self.name


class Boss(Employee):
    def __init__(self, name, age, salary, title):
        super(Boss, self).__init__(name, age, salary, title)
        self.employee_list = []

    def add_employee(self, new_employee):
        self.employee_list.append(new_employee)

    def introduce_yourself(self):
        print('Cześć jestem', self.name, 'mam', self.age, 'lat', 'zarabiam', self.salary, 'złotych', 'i jestem tu bossem')
