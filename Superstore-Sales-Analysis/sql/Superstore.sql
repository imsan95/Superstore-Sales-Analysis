--use the database
use [P_Superstore];

-- Retrieve all columns and records from the Superstore table
--This query fetches all data from the Superstore table. It helps to get an overview of the dataset.
SELECT * FROM superstore;

-- Count the total number of rows (records) in the Superstore table
--This counts the total number of records available in the dataset.
SELECT COUNT(*) AS Total_Records FROM superstore;

-- Get a list of unique product categories in the dataset
--DISTINCT ensures that duplicate categories are removed, so we only see unique values.
SELECT DISTINCT Category FROM superstore;

-- Calculate total sales for each product category
/*
SUM(Sales): Adds up the sales for each category.
GROUP BY Category: Groups data by category so that we get total sales per category.
ORDER BY Total_Sales DESC: Sorts results in descending order of sales.
*/
SELECT Category, SUM(Sales) AS Total_Sales
FROM Superstore
GROUP BY Category
ORDER BY Total_Sales DESC;

-- Calculate total sales for each product category (Rounded to 2 decimal places)
SELECT 
    Category, 
    FORMAT(SUM(Sales), 'N2') AS Total_Sales
FROM Superstore
GROUP BY Category
ORDER BY Total_Sales DESC;

-- Get total sales for each month
/*
FORMAT([Order Date], 'yyyy-MM'): Converts the Order Date column into a YYYY-MM format for monthly grouping.
This helps analyze sales trends over time.
*/
SELECT FORMAT([Order_Date], 'yyyy-MM') AS Month, SUM(Sales) AS Total_Sales
FROM Superstore
GROUP BY FORMAT([Order_Date], 'yyyy-MM')
ORDER BY Month;

--------Intermediate Queries--------

-- Find the top 5 products with the highest total profit
/*
SUM(Profit): Adds up the total profit per product.
TOP 5: Limits results to the top 5 products with the highest profit.
*/
-- Find the customer with the highest total sales
--Groups sales by CustomerName and sorts by highest sales first.

SELECT Customer_Name, SUM(Sales) AS Total_Sales
FROM Superstore
GROUP BY Customer_Name
ORDER BY Total_Sales DESC;

-- Calculate the average discount per product category
/*
AVG(Discount): Calculates the average discount for each category.
Helps in identifying categories that receive higher discounts.
*/

SELECT Category, AVG(Discount) AS Avg_Discount
FROM Superstore
GROUP BY Category
ORDER BY Avg_Discount DESC;

-- Calculate the average discount for each category and display as a percentage
SELECT 
    Category, 
    FORMAT(AVG(Discount) * 100, 'N2') + '%' AS Avg_Discount
FROM Superstore
GROUP BY Category
ORDER BY AVG(Discount) DESC;

-- Rank customers based on their total sales
/*
RANK() OVER (ORDER BY SUM(Sales) DESC): Assigns a rank to each customer based on their total sales.
Helps identify top customers by sales.
*/
SELECT Customer_Name, SUM(Sales) AS Total_Sales,
       RANK() OVER (ORDER BY SUM(Sales) DESC) AS Rank
FROM Superstore
GROUP BY Customer_Name
ORDER BY Rank;

-- Find total sales and profit per state
/*
Groups data by state and shows total sales and profit.
Helps identify best and worst performing states.
*/
SELECT State, SUM(Sales) AS Total_Sales, SUM(Profit) AS Total_Profit
FROM Superstore
GROUP BY State
ORDER BY Total_Sales DESC, Total_Profit DESC;

-- Analyze the impact of discount on profit
/*
Groups by discount level to check average profit and number of orders.
Helps in understanding if higher discounts affect profits negatively.
*/
SELECT Discount, AVG(Profit) AS Avg_Profit, COUNT(*) AS Orders
FROM Superstore
GROUP BY Discount
ORDER BY Discount;

-- Rounds Avg_Profit Discount to 2 decimal places
SELECT 
    ROUND(Discount,2) AS discount, 
    ROUND(AVG(Profit), 2) AS Avg_Profit,  
    COUNT(*) AS Orders
FROM Superstore
GROUP BY Discount
ORDER BY Discount;
