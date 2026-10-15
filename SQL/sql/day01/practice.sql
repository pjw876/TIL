-- ① SELECT 기본
-- 1) 개발 부서, 급여 높은 순
SELECT name, salary FROM employees WHERE dept = '개발' ORDER BY salary DESC;
-- 2) 급여 4500~5200 (BETWEEN은 양끝 포함)
SELECT name, salary FROM employees WHERE salary BETWEEN 4500 AND 5200;
-- 3) 성이 '김' 또는 '이'
SELECT name FROM employees WHERE name LIKE '김%' OR name LIKE '이%';
-- 4) 부서 목록 (NULL도 하나로 나옴)
SELECT DISTINCT dept FROM employees;
-- 5) 상위 3명
SELECT name, salary FROM employees ORDER BY salary DESC LIMIT 3;   -- NULL이 맨 위! (PG는 DESC에서 NULL 먼저)
SELECT name, salary FROM employees ORDER BY salary DESC NULLS LAST LIMIT 3;
-- 6) NULL 비교
SELECT name FROM employees WHERE dept = NULL;      -- 0행 (NULL = NULL 은 참이 아님)
SELECT name FROM employees WHERE dept IS NULL;     -- 한소희

-- ② 집계
-- 7) COUNT(*) vs COUNT(col): NULL 처리 차이
SELECT COUNT(*) AS 전체, COUNT(dept) AS 부서있음, COUNT(salary) AS 급여있음 FROM employees;
-- 8) 부서별 인원/평균급여 (AVG는 NULL 제외)
SELECT dept, COUNT(*) AS cnt, ROUND(AVG(salary)) AS avg_sal, MAX(salary) AS max_sal
FROM employees GROUP BY dept ORDER BY cnt DESC;
-- 9) WHERE vs HAVING: 2022년 이후 입사자만 모아서(WHERE=행 필터), 2명 이상인 부서만(HAVING=그룹 필터)
SELECT dept, COUNT(*) AS cnt
FROM employees
WHERE hired >= '2022-01-01'
GROUP BY dept
HAVING COUNT(*) >= 2;
-- 10) 고객별 매출 (qty*price), 10만원 이상만
SELECT customer, SUM(qty * price) AS revenue
FROM orders GROUP BY customer HAVING SUM(qty * price) >= 100000 ORDER BY revenue DESC;
-- 11) 월별 매출
SELECT to_char(ordered, 'YYYY-MM') AS ym, SUM(qty*price) AS revenue
FROM orders GROUP BY ym ORDER BY ym;
