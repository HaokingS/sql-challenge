-- Create table titles

CREATE TABLE public.titles
(
    title_id character varying(5),
    title character varying(45),
    PRIMARY KEY (title_id)
);

ALTER TABLE IF EXISTS public.titles
    OWNER to postgres;

-- Create table employees

CREATE TABLE public.employees
(
    emp_no character varying(10) NOT NULL,
    emp_title_id character varying(5),
    birth_date date,
    first_name character varying(45),
    last_name character varying(45),
    sex character varying(1),
    hire_date date,
    PRIMARY KEY (emp_no)
);

ALTER TABLE IF EXISTS public.employees
    OWNER to postgres;

-- Create table salaries

CREATE TABLE public.salaries
(
    emp_no character varying(10),
    salary integer
);

ALTER TABLE IF EXISTS public.salaries
    OWNER to postgres;

-- Create table departments

CREATE TABLE public.departments
(
    dept_no character varying(5),
    dept_name character varying(45),
    PRIMARY KEY (dept_no)
);

ALTER TABLE IF EXISTS public.departments
    OWNER to postgres;

-- Create table dept_emp

CREATE TABLE public.dept_emp
(
    emp_no character varying(10),
    dept_no character varying(5)
);

ALTER TABLE IF EXISTS public.dept_emp
    OWNER to postgres;

-- Create table dept_manager

CREATE TABLE public.dept_manager
(
    dept_no character varying(5),
    emp_no character varying(10)
);

ALTER TABLE IF EXISTS public.dept_manager
    OWNER to postgres;