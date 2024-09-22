import sqlite3

# connect database
connection = sqlite3.connect("company_db.db")
cur = connection.cursor()

# Task 1
cur.execute("""
CREATE TABLE IF NOT EXISTS employees (
    id INTEGER PRIMARY KEY,
    name TEXT,
    position TEXT,
    age INTEGER,
    salary REAL,
    city TEXT
);
""")

# Task 2
employees = [
    ("Adam", "Developer", 29, 60000, "Praha"),
    ("Eva", "Manager", 45, 75000, "Brno"),
    ("Jan", "Analyst", 33, 50000, "Praha"),
    ("Petr", "Tester", 27, 48000, "Ostrava"),
    ("Lucie", "Designer", 38, 54000, "Praha"),
    ("Michal", "Developer", 41, 62000, "Brno"),
    ("Anna", "Support", 30, 40000, "Plzeň"),
    ("David", "HR", 50, 58000, "Praha"),
    ("Martin", "Developer", 35, 61000, "Brno"),
    ("Klara", "Manager", 36, 80000, "Praha"),
    ("Tomas", "Developer", 32, 55000, "Plzeň"),
    ("Marek", "HR", 42, 49000, "Ostrava"),
    ("Ivana", "Tester", 29, 47000, "Praha"),
    ("Jana", "Designer", 37, 56000, "Brno"),
    ("Roman", "Support", 34, 45000, "Praha"),
    ("Pavel", "Analyst", 31, 51000, "Brno"),
    ("Irena", "Manager", 46, 72000, "Praha"),
    ("Zdenek", "Developer", 28, 62000, "Plzeň"),
    ("Eliska", "Tester", 40, 48000, "Praha"),
    ("Simona", "Analyst", 36, 58000, "Brno")
]

cur.executemany("INSERT INTO employees (name, position, age, salary, city) VALUES (?, ?, ?, ?, ?)", employees)

# Task 3
def select_employees_by_city(city):
    cur.execute("SELECT * FROM employees WHERE city = ?", (city,))
    return cur.fetchall()

print("Zaměstnanci z Prahy:")
for employee in select_employees_by_city("Praha"):
    print(employee)

# Task 4
def select_young_employees_by_city(city, age_limit):
    cur.execute("SELECT * FROM employees WHERE city = ? AND age < ?", (city, age_limit))
    return cur.fetchall()

print("\nZaměstnanci z Prahy mladší než 40:")
for employee in select_young_employees_by_city("Praha", 40):
    print(employee)

#Task 5
def select_employees_by_salary(city, salary_threshold):
    cur.execute("SELECT * FROM employees WHERE city = ? AND salary > ?", (city, salary_threshold))
    return cur.fetchall()

print("\nZaměstnanci z Prahy s platem vyšším než 50 000:")
for employee in select_employees_by_salary("Praha", 50000):
    print(employee)

# Task 6
def select_employees_by_age_and_city(city1, city2, age_min, age_max):
    cur.execute("SELECT * FROM employees WHERE (city = ? OR city = ?) AND age > ? AND age < ?", (city1, city2, age_min, age_max))
    return cur.fetchall()

print("\nZaměstnanci z Prahy nebo Brna starší než 35 a mladší než 45:")
for employee in select_employees_by_age_and_city("Praha", "Brno", 35, 45):
    print(employee)

# Task 7
def select_employee_info():
    cur.execute("SELECT name, position, salary FROM employees")
    return cur.fetchall()

print("\nJméno, pozice a plat všech zaměstnanců:")
for employee_info in select_employee_info():
    print(employee_info)

# Task 8
def promote_employee(name, new_position):
    cur.execute("UPDATE employees SET position = ? WHERE name = ?", (new_position, name))
    if cur.rowcount == 0:
        cur.execute("INSERT INTO employees (name, position, age, salary, city) VALUES (?, ?, ?, ?, ?)",
                    (name, new_position, 29, 60000, "Praha"))  # Pokud Adam neexistuje, vlož nový záznam

promote_employee("Adam", "Senior Developer")

# Zamestnanci po aktualizaci
print("\nVšichni zaměstnanci po povýšení Adama:")
cur.execute("SELECT * FROM employees")
for employee in cur.fetchall():
    print(employee)

# save changes, close
connection.commit()
connection.close()
