-- 1. List the following details of each employee: employee number, last name, first name, sex, and salary
SELECT
    employees.emp_no,
    employees.last_name,
    employees.first_name,
    employees.sex,
    salaries.salary
FROM employees
JOIN salaries ON employees.emp_no = salaries.emp_no;

-- 2. List first name, last name, and hire date for employees who were hired in 1986.

SELECT 
    employees.first_name,
    employees.last_name,
    employees.hire_date
FROM employees
WHERE EXTRACT(YEAR FROM employees.hire_date) = 1986;

-- 3. List the manager of each department with the following information: department number, department name, the manager's employee number, last name, first name.
SELECT 
    departments.dept_no,
    departments.dept_name,
    employees.emp_no,
    employees.last_name,
    employees.first_name
FROM employees 
JOIN dept_manager ON employees.emp_no = dept_manager.emp_no
JOIN departments ON departments.dept_no = dept_manager.dept_no;

-- 4. List the department of each employee with the following information: employee number, last name, first name, and department name.
SELECT
    employees.emp_no,
    employees.last_name,
    employees.first_name,
    departments.dept_name
FROM employees 
JOIN dept_emp ON employees.emp_no = dept_emp.emp_no
JOIN departments ON departments.dept_no = dept_emp.dept_no;

-- 5. List first name, last name, and sex for employees whose first name is "Hercules" and last names begin with "B."
SELECT
    employees.first_name,
    employees.last_name,
    employees.sex
FROM employees 
WHERE employees.first_name = 'Hercules' AND employees.last_name LIKE 'B%';

-- 6. List all employees in the Sales department, including their employee number, last name, first name, and department name.
SELECT
    employees.emp_no,
    employees.last_name,
    employees.first_name,
    departments.dept_name
FROM employees 
JOIN dept_emp ON employees.emp_no = dept_emp.emp_no
JOIN departments ON departments.dept_no = dept_emp.dept_no
WHERE dept_name = 'Sales';

-- 7. List all employees in the Sales and Development departments, including their employee number, last name, first name, and department name.
SELECT
    employees.emp_no,
    employees.last_name,
    employees.first_name,
    departments.dept_name
FROM employees 
JOIN dept_emp ON employees.emp_no = dept_emp.emp_no
JOIN departments ON departments.dept_no = dept_emp.dept_no
WHERE dept_name IN ('Sales', 'Development');

-- 8. In descending order, list the frequency count of employee last names, i.e., how many employees share each last name.
SELECT
    employees.last_name,
    count(DISTINCT employees.emp_no) as number_of_employee_shared_last_name
FROM employees
GROUP BY employees.last_name
ORDER BY number_of_employee_shared_last_name DESC;


