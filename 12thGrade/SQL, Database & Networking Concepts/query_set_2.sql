-- NOTE: Make the respective tables displayed for every SELECT command.

-- (a) Select all data for Nonmedical stream students from STUDENT
SELECT *  FROM STUDENT WHERE Stream = "Nonmedical";

-- (b) List all the students sorted by AvgMarks in descending order
SELECT * FROM STUDENT ORDER BY AvgMarks DESC;

-- (c) Give outputs of following SQL commands

SELECT MIN(AvgMarks) FROM STUDENT WHERE AvgMarks < 75;
-- Output = 64.4

SELECT SUM(Stipend) FROM STUDENT WHERE Grade = 'B';
-- Output = 1150

SELECT AVG(Stipend) FROM STUDENT WHERE Class = "12A";
-- Output = 475

SELECT COUNT(DISTINCT) FROM STUDENT;
-- Output = 10

-- (d) Write names of those students who are in class 12 sorted by Stipend
SELECT Name FROM STUDENT WHERE Class = "12%" ORDER BY Stipend;
