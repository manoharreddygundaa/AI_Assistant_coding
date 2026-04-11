CREATE DATABASE collegee;
USE collegee;

CREATE TABLE myprojec (
    project_id INT PRIMARY KEY AUTO_INCREMENT,
    student_name VARCHAR(50),
    project_title VARCHAR(100),
    domain VARCHAR(50),
    guide_name VARCHAR(50),
    marks INT
);

INSERT INTO myprojec (student_name, project_title, domain, guide_name, marks) VALUES
('Ravi', 'Online Food Delivery System', 'Web Development', 'Dr. Sharma', 85),
('Priya', 'AI Chatbot', 'Artificial Intelligence', 'Dr. Meena', 90);


---

### Part 2: Payment Processing (Python)

I am testing a sandbox payment gateway for an e-commerce platform.

Write a Python script that:

Accepts input for amount, currency, and payment method
Validates the inputs (e.g., amount > 0, valid currency format, non-empty method)
Simulates sending a payment request (you can mock this, no real API needed)
Displays whether the transaction is successful or failed
Logs failed transactions into a file (e.g., failed_transactions.txt)

Requirements:

Keep the code simple and readable
Use basic Python (no advanced frameworks)
Add comments to explain each part

---

Make sure both SQL and Python outputs are correct, executable, and easy for a beginner to understand.
