-- List the following details of each employee: employee number, last name, first name, sex, and salary.

SELECT 
    employees.emp_no,
    employees.last_name,
    employees.first_name,
    employees.sex,
    salaries.salary
FROM data_management.sql_challenge_astra.employees AS employees
JOIN data_management.sql_challenge_astra.salaries AS salaries ON employees.emp_no = salaries.emp_no;

-- List first name, last name, and hire date for employees who were hired in 1986.

SELECT 
    employees.first_name,
    employees.last_name,
    employees.hire_date
FROM `data_management.sql_challenge_astra.employees` AS employees
WHERE EXTRACT(YEAR FROM employees.hire_date) = 1986;

-- List the manager of each department with the following information: department number, department name, the manager's employee number, last name, first name.

SELECT 
    departments.dept_no,
    departments.dept_name,
    employees.emp_no,
    employees.last_name,
    employees.first_name
FROM `data_management.sql_challenge_astra.employees` AS employees 
JOIN `data_management.sql_challenge_astra.dept_manager` AS dept_manager ON employees.emp_no = dept_manager.emp_no
JOIN `data_management.sql_challenge_astra.departments` AS departments ON departments.dept_no = dept_manager.dept_no;

--List the department of each employee with the following information: employee number, last name, first name, and department name.
SELECT
    employees.emp_no,
    employees.last_name,
    employees.first_name,
    departments.dept_name
FROM `data_management.sql_challenge_astra.employees` AS employees 
JOIN `data_management.sql_challenge_astra.dept_emp` AS dept_emp ON employees.emp_no = dept_emp.emp_no
JOIN `data_management.sql_challenge_astra.departments` AS departments ON departments.dept_no = dept_emp.dept_no;

-- List first name, last name, and sex for employees whose first name is "Hercules" and last names begin with "B."
SELECT
    employees.first_name,
    employees.last_name,
    employees.sex
FROM `data_management.sql_challenge_astra.employees` AS employees 
WHERE employees.first_name = "Hercules" AND employees.last_name LIKE "B%";

-- List all employees in the Sales department, including their employee number, last name, first name, and department name.
SELECT
    employees.emp_no,
    employees.last_name,
    employees.first_name,
    departments.dept_name
FROM `data_management.sql_challenge_astra.employees` AS employees 
JOIN `data_management.sql_challenge_astra.dept_emp` AS dept_emp ON employees.emp_no = dept_emp.emp_no
JOIN `data_management.sql_challenge_astra.departments` AS departments ON departments.dept_no = dept_emp.dept_no
WHERE dept_name = "Sales";

-- List all employees in the Sales and Development departments, including their employee number, last name, first name, and department name.
SELECT
    employees.emp_no,
    employees.last_name,
    employees.first_name,
departments.dept_name #change later, should be dept_name
FROM `data_management.sql_challenge_astra.employees` AS employees 
JOIN `data_management.sql_challenge_astra.dept_emp` AS dept_emp ON employees.emp_no = dept_emp.emp_no
JOIN `data_management.sql_challenge_astra.departments` AS departments ON departments.dept_no = dept_emp.dept_no --change later, should be dept_no 
WHERE dept_name = "Sales" OR dept_name = "Development";

-- In descending order, list the frequency count of employee last names, i.e., how many employees share each last name.
SELECT
    employees.last_name,
    count(DISTINCT(employees.emp_no)) as number_of_employee_shared_last_name
FROM `data_management.sql_challenge_astra.employees` AS employees
GROUP BY 1
ORDER BY 2 DESC;