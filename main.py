class Employee:
    def __init__(self, name, position, phone, email):
        self.name = name
        self.position = position
        self.phone = phone
        self.email = email


class Car:
    def __init__(self, manufacturer, year, model, cost_price, potential_sale_price):
        self.manufacturer = manufacturer
        self.year = year
        self.model = model
        self.cost_price = cost_price
        self.potential_sale_price = potential_sale_price


class Sale:
    def __init__(self, employee, car, date, real_sale_price):
        self.employee = employee
        self.car = car
        self.date = date
        self.real_sale_price = real_sale_price
import csv

class CarSalesApp:
    def __init__(self):
        self.employees = []
        self.cars = []
        self.sales = []

    def add_employee(self, employee):
        self.employees.append(employee)

    def remove_employee(self, employee):
        self.employees.remove(employee)

    def add_car(self, car):
        self.cars.append(car)

    def remove_car(self, car):
        self.cars.remove(car)

    def add_sale(self, sale):
        self.sales.append(sale)

    def remove_sale(self, sale):
        self.sales.remove(sale)

    def generate_employee_report(self):
        for employee in self.employees:
            print(
                f"Співробітник: {employee.name}, Посада: {employee.position}, Номер телефону: {employee.phone}, Email: {employee.email}")

    def generate_car_report(self):
        for car in self.cars:
            print(
                f"Автомобіль: {car.manufacturer} {car.model}, Рік випуску: {car.year}, Собівартість автомобіля: {car.cost_price}, Потенційна ціну родажу автомобіля: {car.potential_sale_price}")

    def generate_sale_report(self):
        for sale in self.sales:
            print(
                f"Продаж: Автомобіль: {sale.car.manufacturer} {sale.car.model}, Співробітник: {sale.employee.name}, Дата: {sale.date}, Реальна ціна продажу: {sale.real_sale_price}")

    def generate_sales_by_date_report(self, date):
        for sale in self.sales:
            if sale.date == date:
                print(
                    f"Продаж: Автомобіль: {sale.car.manufacturer} {sale.car.model}, Співробітник: {sale.employee.name}, Дата: {sale.date}, Реальна ціна продажу: {sale.real_sale_price}")

    def generate_sales_by_period_report(self, start_date, end_date):
        for sale in self.sales:
            if start_date <= sale.date <= end_date:
                print(
                    f"Продаж: Автомобіль: {sale.car.manufacturer} {sale.car.model}, Співробітник: {sale.employee.name}, Дата: {sale.date}, Реальна ціна продажу: {sale.real_sale_price}")

    def generate_sales_by_employee_report(self, employee):
        for sale in self.sales:
            if sale.employee == employee:
                print(
                    f"Продаж: Автомобіль: {sale.car.manufacturer} {sale.car.model}, Співробітник: {sale.employee.name}, Дата: {sale.date}, Реальна ціна продажу: {sale.real_sale_price}")

    def calculate_profit(self):
        total_profit = 0
        for sale in self.sales:
            total_profit += (sale.real_sale_price - sale.car.cost_price)
        return total_profit

    def save_data(self, filename):
        with open(filename, "w", newline="") as outfile:
            writer = csv.writer(outfile)

            writer.writerow(["Система управління продажами автомобілів"])
            for employee in self.employees:
                writer.writerow(["-"*50])
                writer.writerow(["Ім'я", "Посада", "Номер телефону", "email"])
                writer.writerow([employee.name, employee.position, employee.phone, employee.email])


            for car in self.cars:
                writer.writerow(["-" * 50])
                writer.writerow(["виробник", "рік", "модель", "собівартість автомобіля", "потенційна ціна продажу"])
                writer.writerow([car.manufacturer, car.year, car.model, car.cost_price, car.potential_sale_price])


            for sale in self.sales:
                writer.writerow(["-" * 50])
                writer.writerow(
                    ["ім'я працівника", "виробник автомобіля", "модель автомобіля", "Дата", "реальна ціна продажу"])
                writer.writerow([sale.employee.name, sale.car.manufacturer, sale.car.model, sale.date, sale.real_sale_price])

    def load_data(self, filename):
        self.employees = []
        self.cars = []
        self.sales = []

        with open(filename, "r") as infile:
            reader = csv.reader(infile)

            for row in reader:
                if len(row) == 4:
                    employee = Employee(row[0], row[1], row[2], row[3])
                    self.employees.append(employee)
                elif len(row) == 5:
                    car = Car(row[0], (row[1]), row[2], (row[3]), (row[4]))
                    self.cars.append(car)
                elif len(row) == 6:
                    employee = self.find_employee_by_name(row[0])
                    car = self.find_car_by_manufacturer_and_model(row[1], row[2])
                    sale = Sale(employee, car, row[3], float(row[4]))
                    self.sales.append(sale)

    def find_employee_by_name(self, name):
        for employee in self.employees:
            if employee.name == name:
                return employee
        return None

    def find_car_by_manufacturer_and_model(self, manufacturer, model):
        for car in self.cars:
            if car.manufacturer == manufacturer and car.model == model:
                return car
        return None









def main_menu():
    print("Система управління продажами автомобілів")
    print("-" * 30)
    print("1. Додати співробітника")
    print("2. Видалити працівника")
    print("3. Додати автомобіль")
    print("4. Видаліть автомобіль")
    print("5. Додайте Продаж")
    print("6. Видалити продаж")
    print("7. Створення звіту про співробітників")
    print("8. Створіть звіт про автомобіль")
    print("9. Створення звіту про продаж")
    print("10. Створення звіту про продажі за датою")
    print("11. Створення звіту про продажі за періодами")
    print("12. Зробіть звіт про продажі співробітників")
    print("13. Розрахувати прибуток")
    print("14. Збереження даних")
    print("15. Завантажити дані")
    print("16. Вихід")

    choice = input("Введіть свій вибір: ")
    return choice


app = CarSalesApp()

while True:
    choice = main_menu()

    if choice == "1":

        name = input("Введіть ім'я співробітника: ")
        position = input("Введіть посаду співробітника: ")
        phone = input("Введіть телефон співробітника: ")
        email = input("Введіть електронну адресу співробітника: ")
        employee = Employee(name, position, phone, email)
        app.add_employee(employee)
        print("Співробітника успішно додано.")

    elif choice == "2":

        name = input("Введіть ім'я співробітника: ")
        employee = app.find_employee_by_name(name)
        if employee:
            app.remove_employee(employee)
            print("Співробітника успішно видалено.")
        else:
            print("Працівника не знайдено.")

    elif choice == "3":

        manufacturer = input("Введіть виробника автомобіля: ")
        year = int(input("Введіть рік автомобіля: "))
        model = input("Введіть модель автомобіля: ")
        cost_price = float(input("Введіть собівартість автомобіля: "))
        potential_sale_price = float(input("Введіть потенційну ціну продажу автомобіля: "))
        car = Car(manufacturer, year, model, cost_price, potential_sale_price)
        app.add_car(car)
        print("Автомобіль успішно додано.")

    elif choice == "4":

        manufacturer = input("Введіть виробника автомобіля: ")
        model = input("Введіть модель автомобіля: ")
        car = app.find_car_by_manufacturer_and_model(manufacturer, model)
        if car:
            app.remove_car(car)
            print("Автомобіль успішно видалено.")
        else:
            print("Автомобіль не знайдено.")

    elif choice == "5":

        employee_name = input("Введіть ім'я співробітника: ")
        employee = app.find_employee_by_name(employee_name)
        if employee:
            manufacturer = input("Введіть виробника автомобіля: ")
            model = input("Введіть модель автомобіля: ")
            car = app.find_car_by_manufacturer_and_model(manufacturer, model)
            if car:
                date = input("Введіть дату продажу (YYYY-MM-DD): ")
                real_sale_price = float(input("Введіть реальну ціну продажу: "))
                sale = Sale(employee, car, date, real_sale_price)
                app.add_sale(sale)
                print("Продаж успішно додано.")
            else:
                print("Автомобіль не знайдено.")
        else:
            print("Працівника не знайдено.")

    elif choice == "6":

        employee_name = input("Введіть ім'я співробітника: ")
        employee = app.find_employee_by_name(employee_name)
        if employee:
            manufacturer = input("Введіть виробника автомобіля: ")
            model = input("Введіть модель автомобіля: ")
            car = app.find_car_by_manufacturer_and_model(manufacturer, model)
            if car:
                date = input("Введіть дату продажу (YYYY-MM-DD): ")
                sale = Sale(employee, car, date, 0)
                if sale in app.sales:
                    app.remove_sale(sale)
                    print("Продаж успішно видалено.")
                else:
                    print("Продаж не знайдено.")
            else:
                print("Автомобіль не знайдено.")
        else:
            print("Працівника не знайдено.")

    elif choice == "7":

        app.generate_employee_report()

    elif choice == "8":

        app.generate_car_report()

    elif choice == "9":

        app.generate_sale_report()

    elif choice == "10":

        date = input("Введіть дату (YYYY-MM-DD): ")
        app.generate_sales_by_date_report(date)

    elif choice == "11":

        start_date = input("Введіть дату початку (YYYY-MM-DD): ")
        end_date = input("Введіть кінцеву дату (YYYY-MM-DD): ")
        app.generate_sales_by_period_report(start_date, end_date)

    elif choice == "12":

        employee_name = input("Введіть ім'я співробітника: ")
        employee = app.find_employee_by_name(employee_name)
        if employee:
            app.generate_sales_by_employee_report(employee)
        else:
            print("Працівника не знайдено.")

    elif choice == "13":

        profit = app.calculate_profit()
        print(f"Загальний прибуток: {profit}")

    elif choice == "14":

        filename = input("Введіть назву файлу, щоб зберегти дані: ")
        app.save_data(filename)
        print("Дані успішно збережено.")

    elif choice == "15":

        filename = input("Введіть назву файлу для завантаження даних: ")
        app.load_data(filename)
        print("Дані успішно завантажено.")

    elif choice == "16":

        break

    else:
        print("Невірний вибір. Будь ласка спробуйте ще раз.")

print("Дякуємо за використання Системи управління продажами автомобілів!")