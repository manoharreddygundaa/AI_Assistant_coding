-- -- LMS Database Initialization Script
-- -- Create database and tables, then insert sample data

-- -- Create Database
-- CREATE DATABASE IF NOT EXISTS LMS;
USE LMS;

-- -- Create Instructors Table
-- CREATE TABLE Instructors (
--     instructor_id INT PRIMARY KEY,
--     name VARCHAR(100) NOT NULL,
--     email VARCHAR(100) UNIQUE NOT NULL,
--     department VARCHAR(100) 
-- );

-- -- Create Students Table
-- CREATE TABLE Students (
--     student_id INT PRIMARY KEY,
--     name VARCHAR(100) NOT NULL,
--     email VARCHAR(100) UNIQUE NOT NULL,
--     major VARCHAR(100)
-- );

-- -- Create Courses Table
-- CREATE TABLE Courses (
--     course_id INT PRIMARY KEY,
--     title VARCHAR(200) NOT NULL,
--     description TEXT,
--     credits INT
-- );

-- -- Create CourseInstructor Table (Many-to-Many relationship)
-- CREATE TABLE CourseInstructor (
--     course_id INT,
--     instructor_id INT,
--     PRIMARY KEY (course_id, instructor_id),
--     FOREIGN KEY (course_id) REFERENCES Courses(course_id),
--     FOREIGN KEY (instructor_id) REFERENCES Instructors(instructor_id)
-- );

-- -- Create Enrollments Table (Many-to-Many relationship)
-- CREATE TABLE Enrollments (
--     enrollment_id INT PRIMARY KEY AUTO_INCREMENT,
--     student_id INT,
--     course_id INT,
--     enrollment_date DATE,
--     FOREIGN KEY (student_id) REFERENCES Students(student_id),
--     FOREIGN KEY (course_id) REFERENCES Courses(course_id)
-- );

-- -- Inserting sample data for Instructors, Students, Courses, CourseInstructor assignments, and Enrollments

-- -- Insert Instructors
-- INSERT INTO Instructors (instructor_id, name, email, department) VALUES
-- (1, 'Dr. John Smith', 'john.smith@university.edu', 'Computer Science'),
-- (2, 'Prof. Jane Doe', 'jane.doe@university.edu', 'Information Technology'),
-- (3, 'Dr. Michael Johnson', 'michael.johnson@university.edu', 'Software Engineering');

-- -- Insert Students
-- INSERT INTO Students (student_id, name, email, major) VALUES
-- (1, 'Alice Brown', 'alice.brown@student.edu', 'Computer Science'),
-- (2, 'Bob Wilson', 'bob.wilson@student.edu', 'Information Technology'),
-- (3, 'Charlie Davis', 'charlie.davis@student.edu', 'Software Engineering'),
-- (4, 'Diana Evans', 'diana.evans@student.edu', 'Computer Science'),
-- (5, 'Edward Foster', 'edward.foster@student.edu', 'Data Science');

-- -- Insert Courses
-- INSERT INTO Courses (course_id, title, description, credits) VALUES
-- (1, 'Introduction to Computer Science', 'Basic concepts of programming and computer systems', 3),
-- (2, 'Data Structures and Algorithms', 'Fundamental data structures and algorithmic techniques', 4),
-- (3, 'Database Systems', 'Design and implementation of relational databases', 3),
-- (4, 'Web Development', 'Building dynamic web applications using HTML, CSS, and JavaScript', 3);

-- -- Assign Instructors to Courses (CourseInstructor table)
-- INSERT INTO CourseInstructor (course_id, instructor_id) VALUES
-- (1, 1),  -- John Smith teaches Intro to CS
-- (2, 2),  -- Jane Doe teaches Data Structures
-- (3, 3),  -- Michael Johnson teaches Database Systems
-- (4, 1),  -- John Smith teaches Web Development
-- (4, 2);  -- Jane Doe also teaches Web Development

-- -- Enroll Students into Courses (Enrollments table)
-- INSERT INTO Enrollments (student_id, course_id, enrollment_date) VALUES
-- (1, 1, '2023-09-01'),  -- Alice in Intro to CS
-- (1, 2, '2023-09-01'),  -- Alice in Data Structures
-- (2, 2, '2023-09-01'),  -- Bob in Data Structures
-- (2, 3, '2023-09-01'),  -- Bob in Database Systems
-- (3, 1, '2023-09-01'),  -- Charlie in Intro to CS
-- (3, 3, '2023-09-01'),  -- Charlie in Database Systems
-- (3, 4, '2023-09-01'),  -- Charlie in Web Development
-- (4, 3, '2023-09-01'),  -- Diana in Database Systems
-- (4, 4, '2023-09-01'),  -- Diana in Web Development
-- (5, 1, '2023-09-01'),  -- Edward in Intro to CS
-- (5, 4, '2023-09-01');  -- Edward in Web Development

-- -- Insert Instructors
-- INSERT INTO Instructors (instructor_id, name, email, department) VALUES
-- (1, 'Dr. John Smith', 'john.smith@university.edu', 'Computer Science'),
-- (2, 'Prof. Jane Doe', 'jane.doe@university.edu', 'Information Technology'),
-- (3, 'Dr. Michael Johnson', 'michael.johnson@university.edu', 'Software Engineering');

-- -- Insert Students
-- INSERT INTO Students (student_id, name, email, major) VALUES
-- (1, 'Alice Brown', 'alice.brown@student.edu', 'Computer Science'),
-- (2, 'Bob Wilson', 'bob.wilson@student.edu', 'Information Technology'),
-- (3, 'Charlie Davis', 'charlie.davis@student.edu', 'Software Engineering'),
-- (4, 'Diana Evans', 'diana.evans@student.edu', 'Computer Science'),
-- (5, 'Edward Foster', 'edward.foster@student.edu', 'Data Science');

-- -- Insert Courses
-- INSERT INTO Courses (course_id, title, description, credits) VALUES
-- (1, 'Introduction to Computer Science', 'Basic concepts of programming and computer systems', 3),
-- (2, 'Data Structures and Algorithms', 'Fundamental data structures and algorithmic techniques', 4),
-- (3, 'Database Systems', 'Design and implementation of relational databases', 3),
-- (4, 'Web Development', 'Building dynamic web applications using HTML, CSS, and JavaScript', 3);

-- -- Assign Instructors to Courses (CourseInstructor table)
-- INSERT INTO CourseInstructor (course_id, instructor_id) VALUES
-- (1, 1),  -- John Smith teaches Intro to CS
-- (2, 2),  -- Jane Doe teaches Data Structures
-- (3, 3),  -- Michael Johnson teaches Database Systems
-- (4, 1),  -- John Smith teaches Web Development
-- (4, 2);  -- Jane Doe also teaches Web Development

-- -- Enroll Students into Courses (Enrollments table)
-- INSERT INTO Enrollments (student_id, course_id, enrollment_date) VALUES
-- (1, 1, '2023-09-01'),  -- Alice in Intro to CS
-- (1, 2, '2023-09-01'),  -- Alice in Data Structures
-- (2, 2, '2023-09-01'),  -- Bob in Data Structures
-- (2, 3, '2023-09-01'),  -- Bob in Database Systems
-- (3, 1, '2023-09-01'),  -- Charlie in Intro to CS
-- (3, 3, '2023-09-01'),  -- Charlie in Database Systems
-- (3, 4, '2023-09-01'),  -- Charlie in Web Development
-- (4, 3, '2023-09-01'),  -- Diana in Database Systems
-- (4, 4, '2023-09-01'),  -- Diana in Web Development
-- (5, 1, '2023-09-01'),  -- Edward in Intro to CS
-- (5, 4, '2023-09-01');  -- Edward in Web Development
select * from Instructors;
select * from Students;
select * from Courses;