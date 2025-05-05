class Person:
    def __init__(self, name, money, mood, health_rate):
        self.name = name
        self._money = max(0, money)
        self.mood = mood
        self._health_rate = max(0, min(100, health_rate))  # Clamp between 0 and 100

    @property
    def money(self):
        return self._money

    @money.setter
    def money(self, value):
        self._money = max(0, value)

    @property
    def health_rate(self):
        return self._health_rate

    @health_rate.setter
    def health_rate(self, value):
        self._health_rate = max(0, min(100, value))

    def sleep(self, hours):
        if hours == 7:
            self.mood = "happy"
        elif hours < 7:
            self.mood = "tired"
        else:
            self.mood = "lazy"

    def eat(self, meals):
        if meals == 3:
            self.health_rate = 100
        elif meals == 2:
            self.health_rate = 75
        elif meals == 1:
            self.health_rate = 50

    def buy(self, items):
        cost = items * 10
        if self.money >= cost:
            self.money -= cost
        else:
            print("Not enough money to buy items.")


class Car:
    def __init__(self, name, fuel_rate, velocity):
        self.name = name
        self.fuel_rate = max(0, fuel_rate)
        self.velocity = velocity

    def run(self, distance, velocity):
        self.velocity = velocity
        fuel_needed = distance * 0.1
        if self.fuel_rate >= fuel_needed:
            self.fuel_rate -= fuel_needed
            print(f"The car ran {distance} km at {velocity} km/h.")
        else:
            print("Not enough fuel to run.")
            self.stop()

    def stop(self):
        self.velocity = 0
        print("The car has stopped.")


class Employee(Person):
    def __init__(self, name, money, mood, health_rate, emp_id, car, email, salary, distance_to_work):
        super().__init__(name, money, mood, health_rate)
        self.id = emp_id
        self.car = car
        self.email = email
        self._salary = max(1000, salary)  # Minimum salary rule
        self.distance_to_work = distance_to_work

    @property
    def salary(self):
        return self._salary

    @salary.setter
    def salary(self, value):
        if value >= 1000:
            self._salary = value
        else:
            print("Salary cannot be less than 1000.")

    def work(self, hours):
        self.mood = "happy" if hours == 8 else "tired" if hours > 8 else "lazy"

    def drive(self, distance):
        self.car.run(distance, self.car.velocity)

    def refuel(self, amount):
        self.car.fuel_rate += amount

    def send_mail(self, to, subject, body):
        print(f"Sending mail to {to} with subject: '{subject}'\nBody: {body}")


class Office:
    def __init__(self, name):
        self.name = name
        self.employees = []

    def get_all_employees(self):
        return self.employees

    def get_employee(self, emp_id):
        for emp in self.employees:
            if emp.id == emp_id:
                return emp
        print(f"No employee found with ID: {emp_id}")
        return None

    def hire(self, employee):
        self.employees.append(employee)
        print(f"Employee {employee.name} hired.")

    def fire(self, emp_id):
        original_count = len(self.employees)
        self.employees = [emp for emp in self.employees if emp.id != emp_id]
        if len(self.employees) < original_count:
            print(f"Employee with ID {emp_id} fired.")
        else:
            print(f"No employee found with ID: {emp_id}.")

    def calculate_lateness(self, arrival_time, work_start_time):
        return max(0, arrival_time - work_start_time)

    def deduct(self, emp_id, amount):
        emp = self.get_employee(emp_id)
        if emp:
            emp.salary -= amount
            print(f"{amount} deducted from employee {emp.id}'s salary.")

    def reward(self, emp_id, amount):
        emp = self.get_employee(emp_id)
        if emp:
            emp.salary += amount
            print(f"{amount} added to employee {emp.id}'s salary.")

#######################################################################################################           

my_car = Car(name="Toyota", fuel_rate=50, velocity=100)

emp1 = Employee(
    name="John Doe",
    money=500,
    mood="neutral",
    health_rate=80,
    emp_id=101,
    car=my_car,
    email="john@example.com",
    salary=2000,
    distance_to_work=20
)


office = Office(name="TechCorp")


office.hire(emp1)


print("All employees in office:")
for emp in office.get_all_employees():
    print(f"{emp.name} (ID: {emp.id})")


emp1.sleep(6)
emp1.eat(2)
emp1.work(9)
emp1.drive(emp1.distance_to_work)

office.reward(emp_id=101, amount=500)
office.deduct(emp_id=101, amount=200)

office.fire(emp_id=101)