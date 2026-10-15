-- Day 1 연습용 데이터: 직원/부서/주문
DROP TABLE IF EXISTS orders, employees;

CREATE TABLE employees (
    id      serial PRIMARY KEY,
    name    text NOT NULL,
    dept    text,
    salary  int,
    hired   date
);

INSERT INTO employees (name, dept, salary, hired) VALUES
 ('김민수','개발',5200,'2021-03-02'),
 ('이서연','개발',6100,'2019-07-15'),
 ('박지훈','개발',4500,'2023-01-09'),
 ('최유진','디자인',4800,'2020-11-23'),
 ('정하늘','디자인',5000,'2022-05-30'),
 ('강도윤','영업',4200,'2018-02-12'),
 ('윤서아','영업',3900,'2024-04-01'),
 ('임재현','영업',NULL,'2024-08-19'),
 ('한소희',NULL,4400,'2023-09-04');

CREATE TABLE orders (
    id       serial PRIMARY KEY,
    customer text NOT NULL,
    product  text NOT NULL,
    qty      int NOT NULL,
    price    int NOT NULL,
    ordered  date NOT NULL
);

INSERT INTO orders (customer, product, qty, price, ordered) VALUES
 ('A','키보드',1,50000,'2026-09-01'),
 ('A','마우스',2,20000,'2026-09-03'),
 ('B','키보드',1,50000,'2026-09-03'),
 ('B','모니터',1,200000,'2026-09-10'),
 ('C','마우스',3,20000,'2026-09-12'),
 ('C','키보드',2,50000,'2026-10-01'),
 ('A','모니터',1,200000,'2026-10-02'),
 ('D','마우스',1,20000,'2026-10-05');
