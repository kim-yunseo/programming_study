-- 변경
ALTER TABLE 주문 RENAME COLUMN 배송도시 TO 배송도시코드;
ALTER TABLE 주문 MODIFY 배송도시코드 VARCHAR(256);

-- 인덱스 생성
CREATE INDEX idx_order_date ON 주문(주문일);
ALTER TABLE 주문 DROP INDEX idx_order_date;
-- DROP INDEX idx_order_date ON 주문;

-- 뷰
CREATE VIEW vw_order AS
SELECT 고객번호, COUNT(*) AS 주문건수, SUM(주문가격) AS 총주문금액 FROM 주문 GROUP BY 고객번호;
SELECT * FROM vw_order;
SELECT 고객번호, 주문건수, 총주문금액 FROM vw_order WHERE 총주문금액>=50000;