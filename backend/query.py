# 1. List the following details of each employee: employee number, last name, first name, sex, and salary
first_query = """
SELECT
    employees.emp_no AS "Employee Number",
    employees.last_name AS "Last Name",
    employees.first_name AS "First Name",
    employees.sex AS "Sex",
    salaries.salary AS "Salary"
FROM employees
JOIN salaries ON employees.emp_no = salaries.emp_no
"""

# 2. List first name, last name, and hire date for employees who were hired in 1986
second_query = """SELECT 
    employees.first_name AS "First Name",
    employees.last_name AS "Last Name",
    employees.hire_date AS "Hire Date"
FROM employees
WHERE EXTRACT(YEAR FROM employees.hire_date) = 1986
"""

# 3. List the manager of each department with the following information: department number, department name, the manager's employee number, last name, first name
third_query = """SELECT 
    departments.dept_no AS "Department Number",
    departments.dept_name AS "Department Name",
    employees.emp_no AS "Employee Number",
    employees.last_name AS "Last Name",
    employees.first_name AS "First Name"
FROM employees 
JOIN dept_manager ON employees.emp_no = dept_manager.emp_no
JOIN departments ON departments.dept_no = dept_manager.dept_no"""

# 4. List the department of each employee with the following information: employee number, last name, first name, and department name
fourth_query = """SELECT
    employees.emp_no AS "Employee Number",
    employees.last_name AS "Last Name",
    employees.first_name AS "First Name",
    departments.dept_name AS "Department Name"
FROM employees 
JOIN dept_emp ON employees.emp_no = dept_emp.emp_no
JOIN departments ON departments.dept_no = dept_emp.dept_no
"""

# 5. List first name, last name, and sex for employees whose first name is "Hercules" and last names begin with "B."
fifth_query = """SELECT
    employees.first_name AS "First Name",
    employees.last_name AS "Last Name",
    employees.sex "Sex"
FROM employees 
WHERE employees.first_name = 'Hercules' AND employees.last_name LIKE 'B%'
"""

# 6. List all employees in the Sales department, including their employee number, last name, first name, and department name
sixth_query = """SELECT
    employees.emp_no AS "Employee Number",
    employees.last_name AS "Last Name",
    employees.first_name AS "First Name",
    departments.dept_name AS "Department Name"
FROM employees 
JOIN dept_emp ON employees.emp_no = dept_emp.emp_no
JOIN departments ON departments.dept_no = dept_emp.dept_no
WHERE dept_name = 'Sales'
"""

# 7. List all employees in the Sales and Development departments, including their employee number, last name, first name, and department name
seventh_query = """SELECT
    employees.emp_no AS "Employee Number",
    employees.last_name AS "Last Name",
    employees.first_name AS "First Name",
    departments.dept_name AS "Department Name"
FROM employees 
JOIN dept_emp ON employees.emp_no = dept_emp.emp_no
JOIN departments ON departments.dept_no = dept_emp.dept_no
WHERE dept_name IN ('Sales', 'Development')
"""

# 8. In descending order, list the frequency count of employee last names, i.e., how many employees share each last name
eight_query = """SELECT
    employees.last_name AS "Last Name",
    count(DISTINCT employees.emp_no) as number_of_employee_shared_last_name
FROM employees
GROUP BY employees.last_name
ORDER BY number_of_employee_shared_last_name DESC
"""


