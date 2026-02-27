CREATE DATABASE student_result_db;

USE student_result_db;

CREATE TABLE students (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100) NOT NULL,
    roll_number VARCHAR(20) UNIQUE NOT NULL,
    subject1 INT,
    subject2 INT,
    subject3 INT,
    total INT,
    percentage FLOAT,
    grade VARCHAR(2)
);
