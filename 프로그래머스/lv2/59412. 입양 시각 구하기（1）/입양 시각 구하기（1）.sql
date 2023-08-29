-- 코드를 입력하세요
SELECT hour(DATETIME) as HOUR, COUNT(ANIMAL_ID) as "COUNT"
FROM ANIMAL_OUTS
where hour(DATETIME) between "09:00" and "19:59"
group by HOUR
order by HOUR