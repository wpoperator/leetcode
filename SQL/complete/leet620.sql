SELECT *
FROM cinema
WHERE id % 2 <> 0 AND TRIM(description) <> 'boring' 
ORDER BY rating DESC;
