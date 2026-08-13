CREATE USER 'user1'@'localhost' IDENTIFIED BY 'sql123';
GRANT SELECT,INSERT ON 주문 TO 'user1'@'localhost';
REVOKE INSERT ON 주문 FROM 'user1'@'localhost';

-- 부여된 권한 확인
SHOW GRANTS FOR 'user1'@'localhost';

-- Auto Commit 해제
set autocommit=0;
-- set autocommit=false;

-- 트랜잭션 시작-> 변경 -> 복구지점 설정
START TRANSACTION;
UPDATE 주문 SET 주문가격=20000 WHERE 주문번호='o1001';
SELECT * FROM 주문;
SAVEPOINT P1;

-- 삭제 이후 P1으로 복구(작업취소)
SET SQL_SAFE_UPDATES=0;
DELETE FROM 주문 WHERE 주문번호='O1003';
SELECT * FROM 주문;
ROLLBACK TO SAVEPOINT P1;
SELECT * FROM 주문;

-- 트랜잭션 최종 확정
COMMIT;

-- 계정 삭제
DROP USER 'user1'@'localhost';
SHOW GRANTS;