-- NOTE: Make the respective tables displayed for every SELECT command.

-- (a) To show all information about the swimming coaches in the club
SELECT * FROM CLUB WHERE SPORTS = "SWIMMING";

-- (b) To list names of all coaches with their date of appointment (DATEOFAPP) in descending order
SELECT COACHNAME, DATEOFAPP FROM CLUB ORDER BY DATEOFAPP DESC;

-- (c) To display a report showing COACHNAME, PAY, AGE & BONUS (15% of PAY) for all coaches.
ALTER TABLE CLUB ADD BONUS INT;
UPDATE CLUB SET BONUS = PAY * 0.15;
SELECT COACHNAME, PAY, AGE, BONUS FROM CLUB;


-- (d) Give outputs of following commands

SELECT COUNT(DISTINCT SPORTS) FROM CLUB;
-- Output = 4

SELECT MIN(AGE) FROM CLUB WHERE SEX = 'F';
-- Output = 34

SELECT AVG(PAY) FROM CLUB WHERE SPORTS = "KARATE";
-- Output = 1100

SELECT SUM(PAY) FROM CLUB WHERE DATEOFAPP > '31/01/98';
-- Output = 7800

