CREATE DATABASE coursera;

USE coursera;

CREATE TABLE courses (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(150) NOT NULL,
    instructor_id INT NOT NULL,
    total_time TINYINT NOT NULL,
    credit TINYINT NOT NULL,
    time_created DATETIME DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE instructors (
    id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(100) NOT NULL,
    last_name VARCHAR(100) NOT NULL,
    time_created DATETIME DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE students (
    pin CHAR(10) NOT NULL PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    time_created DATETIME DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE students_courses_xref (
    student_pin CHAR(10) NOT NULL,
    course_id INT NOT NULL,
    completion_date DATE NULL,
    PRIMARY KEY (student_pin, course_id),
    FOREIGN KEY (student_pin) REFERENCES students(pin),
    FOREIGN KEY (course_id) REFERENCES courses(id)
);

INSERT INTO courses (name, instructor_id, total_time, credit, time_created) VALUES
('Analysis', 1, 20, 10, '2020-03-16 13:26:44.283'),
('Linear Algebra', 1, 30, 15, '2020-03-16 13:27:26.300'),
('Statistics', 2, 30, 15, '2020-03-16 13:27:38.417'),
('Geometry', 3, 35, 20, '2020-03-16 13:27:54.013');

INSERT INTO instructors (first_name, last_name, time_created) VALUES
('Neno', 'Dimitrov', '2020-03-16 13:25:34.973'),
('Petko', 'Valchev', '2020-03-16 13:26:00.143'),
('Petar', 'Penchev', '2020-03-16 13:26:12.613');

INSERT INTO students (pin, first_name, last_name, time_created) VALUES
('9412011005', 'Krasimir', 'Petrov', '2020-03-16 13:23:58.777'),
('9501011014', 'Elena', 'Foteva', '2020-03-16 13:24:29.853'),
('9507141009', 'Ivan', 'Ivanov', '2020-03-16 13:23:39.220');

INSERT INTO students_courses_xref (student_pin, course_id, completion_date) VALUES
('9412011005', 1, '2019-07-16'),
('9412011005', 2, '2019-08-20'),
('9501011014', 1, '2019-07-16'),
('9501011014', 2, '2019-08-01'),
('9501011014', 3, '2019-10-01'),
('9501011014', 4, '2019-12-05'),
('9507141009', 4, '2019-08-20');
