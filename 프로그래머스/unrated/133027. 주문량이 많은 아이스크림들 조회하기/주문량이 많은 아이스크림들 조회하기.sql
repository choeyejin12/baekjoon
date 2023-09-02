-- 코드를h 입력하세요
SELECT h.FLAVOR from FIRST_HALF as h left JOIN JULY as j
on h.FLAVOR = j.FLAVOR
group by j.FLAVOR
order by h.TOTAL_ORDER + sum(j.TOTAL_ORDER) desc
limit 3