Create Database college_db;

USE college_db;

create table students (
     student_id INT PRIMARY KEY AUTO_INCREMENT ,
     first_name VARCHAR(50) NOT NULL,
     last_name VARCHAR(50) NOT NULL,
     email VARCHAR(50) UNIQUE NOT NULL,
     date_of_birth DATE,
     department_id INT,
     enrollment_year INT,
     FOREIGN KEY (department_id)
    REFERENCES Departments(department_id),
    phone_number int
     
     );
     
create table departments(
department_id INT primary key auto_increment,
dept_name VARCHAR(100) NOT NULL,
hod_name VARCHAR(100),
budget decimal(12,2));

create table courses(
course_id INT primary key auto_increment,
course_name varchar(150) not null,
course_code varchar(20) unique,
credits int,
department_id int,
foreign key(department_id)
references departments(department_id));

create table enrollments(
enrollment_id int primary key auto_increment,
student_id int ,
course_id int,
enrollment_date date,
grade char(2),
foreign key(student_id)
references students(student_id),
foreign key(course_id)
references courses(course_id));

create table professors(
professor_id int primary key auto_increment,
prof_name varchar(100) not null,
email varchar(100) unique,
department_id int,
salary decimal(10,2),
foreign key(department_id)
references departments(department_id));

INSERT INTO departments (dept_name, hod_name, budget) VALUES
  ('Computer Science', 'Dr. Ramesh Kumar', 850000.00),
  ('Electronics', 'Dr. Priya Nair', 620000.00),
  ('Mechanical', 'Dr. Suresh Iyer', 540000.00),
  ('Civil', 'Dr. Ananya Sharma', 430000.00);
  
  INSERT INTO students (first_name, last_name, email, date_of_birth, department_id, 
enrollment_year) VALUES
  ('Arjun',  'Mehta',    'arjun.mehta@college.edu',    '2003-04-12', 1, 2022),
  ('Priya',  'Suresh',   'priya.suresh@college.edu',   '2003-07-25', 1, 2022),
  ('Rohan',  'Verma',    'rohan.verma@college.edu',    '2002-11-08', 2, 2021),
  ('Sneha',  'Patel',    'sneha.patel@college.edu',    '2004-01-30', 3, 2023),
  ('Vikram', 'Das',      'vikram.das@college.edu',     '2003-09-14', 1, 2022),
  ('Kavya',  'Menon',    'kavya.menon@college.edu',    '2002-05-17', 2, 2021),
  ('Aditya', 'Singh',    'aditya.singh@college.edu',   '2004-03-22', 4, 2023),
  ('Deepika','Rao',      'deepika.rao@college.edu',    '2003-08-09', 1, 2022);
  
  INSERT INTO courses (course_name, course_code, credits, department_id) VALUES
  ('Data Structures & Algorithms', 'CS101', 4, 1),
  ('Database Management Systems',  'CS102', 3, 1),
  ('Object Oriented Programming',  'CS103', 4, 1),
  ('Circuit Theory',               'EC101', 3, 2),
  ('Thermodynamics',               'ME101', 3, 3);
  
  INSERT INTO enrollments (student_id, course_id, enrollment_date, grade) VALUES
  (1, 1, '2022-07-01', 'A'), (1, 2, '2022-07-01', 'B'),
  (2, 1, '2022-07-01', 'B'), (2, 3, '2022-07-01', 'A'),
  (3, 4, '2021-07-01', 'A'), (4, 5, '2023-07-01', NULL),
  (5, 1, '2022-07-01', 'C'), (5, 2, '2022-07-01', 'A'),
  (6, 4, '2021-07-01', 'B'), (7, 5, '2023-07-01', NULL),
  (8, 1, '2022-07-01', 'A'), (8, 3, '2022-07-01', 'B');
  
  INSERT INTO professors (prof_name, email, department_id, salary) VALUES
  ('Dr. Anand Krishnan',  'anand.k@college.edu',   1, 95000.00),
  ('Dr. Meena Pillai',    'meena.p@college.edu',   1, 88000.00),
  ('Dr. Sunil Rajan',     'sunil.r@college.edu',   2, 82000.00),
  ('Dr. Latha Gopal',     'latha.g@college.edu',   3, 79000.00),
  ('Dr. Kartik Bose',     'kartik.b@college.edu',  4, 76000.00);
  
  select * from students;
  select * from departments;
  select * from courses;
  select * from enrollments;
  select * from professors;
  ALTER Table students ADD phone_number int;
  
  ALTER table courses  add max_seats int default(50);
 
 ALTER table enrollments modify grade char(2) check(grade in('A', 'B', 'C', 'D', 'E', 'F') OR grade  IS NULL);

ALTER table departments change hod_name head_of_dept VARCHAR(100);

ALTER table students drop phone_number;

SHOW COLUMNS FROM departments;

INSERT INTO students (first_name, last_name, email, date_of_birth, department_id, 
enrollment_year) VALUES
  ('Shiva',  'Tharani',    'shiva@college.edu',    '2005-09-17', 1, 2023),
  ('Vidhya',  'nivi',   'vidhya@college.edu',   '2006-03-20', 1, 2023);
  
  UPDATE enrollments SET grade = 'B' where enrollment_id=5;
  
  SET SQL_SAFE_UPDATES = 0;
  DELETE FROM enrollments WHERE grade IS NULL;
  SET SQL_SAFE_UPDATES = 1;
  
  SELECT * from students where enrollment_year = 2022 order by first_name;
  
  select * from courses where credits>3; 
  
  select * from professors where salary between 80000 and 95000;
  
  select * from students where email like '%college.edu' ;
  
  select  COUNT(*) from students order by enrollment_year;
  
  SELECT CONCAT(s.first_name, ' ', s.last_name) AS student_name, d.dept_name FROM students s JOIN departments d
ON s.department_id = d.department_id;

SELECT e.enrollment_id, CONCAT(s.first_name, ' ', s.last_name) AS student_name, c.course_name, e.enrollment_date, e.grade
FROM enrollments e JOIN students s ON e.student_id = s.student_id JOIN courses c ON e.course_id = c.course_id;
  
SELECT s.student_id, CONCAT(s.first_name, ' ', s.last_name) AS student_name FROM students s LEFT JOIN enrollments e ON s.student_id = e.student_id
WHERE e.student_id IS NULL;

SELECT c.course_name, COUNT(e.student_id) AS enrollment_count FROM courses c LEFT JOIN enrollments e ON c.course_id = e.course_id
GROUP BY c.course_id, c.course_name;

SELECT
    d.dept_name,
    p.prof_name,
    p.salary
FROM departments d
LEFT JOIN professors p
ON d.department_id = p.department_id;

SELECT
    c.course_name,
    COUNT(e.student_id) AS enrollment_count
FROM courses c
LEFT JOIN enrollments e
ON c.course_id = e.course_id
GROUP BY c.course_id, c.course_name;

SELECT
    d.dept_name,
    ROUND(AVG(p.salary), 2) AS average_salary
FROM departments d
LEFT JOIN professors p
ON d.department_id = p.department_id
GROUP BY d.department_id, d.dept_name;

SELECT
    dept_name,
    budget
FROM departments
WHERE budget > 600000;

SELECT
    e.grade,
    COUNT(*) AS grade_count
FROM enrollments e
JOIN courses c
ON e.course_id = c.course_id
WHERE c.course_code = 'CS101'
GROUP BY e.grade;

SELECT
    d.dept_name,
    COUNT(DISTINCT e.student_id) AS total_students
FROM departments d
JOIN courses c
ON d.department_id = c.department_id
JOIN enrollments e
ON c.course_id = e.course_id
GROUP BY d.department_id, d.dept_name
HAVING COUNT(DISTINCT e.student_id) > 2;

  SELECT
    s.student_id,
    CONCAT(s.first_name,' ',s.last_name) AS student_name,
    COUNT(e.course_id) AS total_courses
FROM students s
JOIN enrollments e
ON s.student_id = e.student_id
GROUP BY s.student_id,s.first_name,s.last_name
HAVING COUNT(e.course_id) >
(
    SELECT AVG(course_count)
    FROM
    (
        SELECT COUNT(course_id) AS course_count
        FROM enrollments
        GROUP BY student_id
    ) AS avg_table
);

SELECT
    c.course_name,
    c.course_code
FROM courses c
WHERE NOT EXISTS
(
    SELECT *
    FROM enrollments e
    WHERE e.course_id = c.course_id
    AND (e.grade <> 'A' OR e.grade IS NULL)
);

SELECT
    p.prof_name,
    p.salary,
    d.dept_name
FROM professors p
JOIN departments d
ON p.department_id=d.department_id
WHERE p.salary=
(
    SELECT MAX(salary)
    FROM professors p2
    WHERE p2.department_id=p.department_id
);

SELECT *
FROM
(
    SELECT
        d.dept_name,
        AVG(p.salary) AS avg_salary
    FROM departments d
    JOIN professors p
    ON d.department_id=p.department_id
    GROUP BY d.department_id,d.dept_name
) AS dept_avg
WHERE avg_salary>85000;

CREATE VIEW vw_student_enrollment_summary AS
SELECT
    s.student_id,
    CONCAT(s.first_name,' ',s.last_name) AS student_name,
    d.dept_name,
    COUNT(e.course_id) AS total_courses,

    ROUND(
        AVG(
            CASE
                WHEN e.grade='A' THEN 4
                WHEN e.grade='B' THEN 3
                WHEN e.grade='C' THEN 2
                WHEN e.grade='D' THEN 1
                WHEN e.grade='F' THEN 0
            END
        ),2
    ) AS GPA

FROM students s

LEFT JOIN departments d
ON s.department_id=d.department_id

LEFT JOIN enrollments e
ON s.student_id=e.student_id

GROUP BY
s.student_id,
student_name,
d.dept_name;

CREATE VIEW vw_course_stats AS

SELECT

    c.course_name,
    c.course_code,

    COUNT(e.student_id) AS total_enrollments,

    ROUND(
        AVG(
            CASE

                WHEN e.grade='A' THEN 4
                WHEN e.grade='B' THEN 3
                WHEN e.grade='C' THEN 2
                WHEN e.grade='D' THEN 1
                WHEN e.grade='F' THEN 0

            END
        ),2
    ) AS avg_gpa

FROM courses c

LEFT JOIN enrollments e
ON c.course_id=e.course_id

GROUP BY
c.course_id,
c.course_name,
c.course_code;

SELECT *
FROM vw_student_enrollment_summary
WHERE GPA>3.0;

  UPDATE vw_student_enrollment_summary
SET GPA=4
WHERE student_id=1;

DROP VIEW vw_course_stats;
DROP VIEW vw_student_enrollment_summary;

DELIMITER $$

CREATE PROCEDURE sp_enroll_student(IN p_student_id INT, IN p_course_id INT, IN p_enrollment_date DATE)
BEGIN
IF EXISTS ( SELECT 1 FROM enrollments WHERE student_id = p_student_id AND course_id = p_course_id ) THEN
SIGNAL SQLSTATE '45000'
SET MESSAGE_TEXT = 'Duplicate enrollment is not allowed';
ELSE
INSERT INTO enrollments
(student_id, course_id, enrollment_date) VALUES (p_student_id, p_course_id, p_enrollment_date);
END IF;
END$$
DELIMITER ;

CREATE TABLE department_transfer_log (
log_id INT AUTO_INCREMENT PRIMARY KEY,
student_id INT,
old_department INT,
new_department INT,
transfer_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP );

DELIMITER $$

CREATE PROCEDURE sp_transfer_student(IN p_student_id INT,IN p_new_department INT)
BEGIN
DECLARE old_dept INT;
DECLARE EXIT HANDLER FOR SQLEXCEPTION
BEGIN
ROLLBACK;
END;
START TRANSACTION;
SELECT department_id
INTO old_dept
FROM students
WHERE student_id = p_student_id;
UPDATE students
SET department_id = p_new_department
WHERE student_id = p_student_id;
INSERT INTO department_transfer_log ( student_id, old_department, new_department) VALUES ( p_student_id, old_dept, p_new_department);
COMMIT;
END$$
DELIMITER ;
  
  CALL sp_transfer_student(1,999);
  
  START TRANSACTION;

INSERT INTO enrollments (student_id, course_id, enrollment_date)
VALUES (3,2,'2026-06-18');
SAVEPOINT sp1;
INSERT INTO enrollments (student_id, course_id, enrollment_date) VALUES (3,999,'2026-06-18');
ROLLBACK TO sp1;
COMMIT;

EXPLAIN FORMAT=JSON
SELECT s.first_name, s.last_name, c.course_name
FROM enrollments e JOIN students s ON s.student_id=e.student_id JOIN courses c ON c.course_id=e.course_id
WHERE s.enrollment_year=2022;

CREATE INDEX idx_enrollment_year
ON students(enrollment_year);

CREATE UNIQUE INDEX idx_student_course
ON enrollments(student_id,course_id);

CREATE INDEX idx_course_code
ON courses(course_code);

SHOW TABLES;

DESC students;