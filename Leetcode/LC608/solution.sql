SELECT
id,
IF(t3.parent and t3.child,'Inner',IF(not t3.parent and t3.child,'Leaf','Root')) as type
FROM (
    SELECT
    id, 
    (SELECT count(*) FROM Tree t2 WHERE t1.id=t2.p_id) as parent,
    (SELECT count(*) FROM Tree t2 WHERE t2.id=t1.p_id) as child
    FROM Tree t1
) t3
order by id ASC