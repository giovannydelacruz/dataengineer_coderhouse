/* Ejercicio #1 */

SELECT *
FROM agents
WHERE name like 'M%' or name like '%o';

/* Ejercicio #2 */

SELECT occupation
FROM customers
WHERE occupation like '%Engineer%'
ORDER BY name;

/* Ejercicio #3 */

SELECT customerid, name,
                        CASE WHEN Age >30 THEN 'Sí'
                        ELSE 'No' AS Mayor30
FROM customers;

/* Ejercicio #4 */

WITH ingenieros AS (
SELECT *
FROM customers
WHERE occupation like '%Engineer%'
ORDER BY name), 
mayores_de_30 AS (SELECT customerid, name,
                        CASE WHEN Age >30 THEN 'Sí'
                        ELSE 'No' AS Mayor30
                        FROM customers)

SELECT *, Mayor30,
                        CASE WHEN productsold = 1 THEN "Compro"
                        ELSE "No Compro" AS compro
FROM calls
INNER JOIN ingenieros ON calls.customerid = ingenieros.customerid
INNER JOIN mayores_de_30 ON calls.customerid = mayores_de_30.customerid;

/* Ejercicio #5 */

/* Consulta 1 */
WITH ingenieros AS (
SELECT *
FROM customers
WHERE occupation like '%Engineer%'
ORDER BY name)

SELECT COUNT(*), SUM(productsold)
FROM calls
INNER JOIN ingenieros ON calls.customerid = ingenieros.customerid;






