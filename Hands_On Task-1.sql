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