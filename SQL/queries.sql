-- ==========================================
-- Query 1: Top 5 Funds by AUM
-- ==========================================

SELECT
    d.scheme_name,
    d.fund_house,
    a.aum_crore
FROM fact_aum AS a
INNER JOIN dim_fund AS d
    ON a.amfi_code = d.amfi_code
ORDER BY a.aum_crore DESC
LIMIT 5;

-- ==========================================
-- Query 2: Average NAV per Month
-- ==========================================

SELECT
    strftime('%Y-%m', date) AS month,
    ROUND(AVG(nav), 2) AS average_nav
FROM fact_nav
GROUP BY strftime('%Y-%m', date)
ORDER BY month;

-- ==========================================
-- Query 3: SIP Year-over-Year Growth
-- ==========================================

SELECT
    strftime('%Y', date) AS year,
    SUM(amount_inr) AS total_sip_amount
FROM fact_transactions
WHERE transaction_type = 'SIP'
GROUP BY strftime('%Y', date)
ORDER BY year;

-- ==========================================
-- Query 4: Total Transaction Amount by State
-- ==========================================

SELECT
    state,
    SUM(amount_inr) AS total_transaction_amount
FROM fact_transactions
GROUP BY state
ORDER BY total_transaction_amount DESC;

-- ==========================================
-- Query 5: Funds with Expense Ratio less than 1%
-- ==========================================

SELECT
    d.scheme_name,
    d.fund_house,
    p.expense_ratio_pct
FROM fact_performance AS p
INNER JOIN dim_fund AS d
    ON p.amfi_code = d.amfi_code
WHERE p.expense_ratio_pct < 1
ORDER BY p.expense_ratio_pct ASC;

-- ==========================================
-- Query 6: Top 5 Fund Houses by Number of Schemes
-- ==========================================

SELECT
    fund_house,
    COUNT(scheme_name) AS total_schemes
FROM dim_fund
GROUP BY fund_house
ORDER BY total_schemes DESC
LIMIT 5;

-- ==========================================
-- Query 7: Top 5 Fund Houses by Average 3-Year Return
-- ==========================================

SELECT
    d.fund_house,
    ROUND(AVG(p.return_3yr_pct), 2) AS avg_3yr_return
FROM fact_performance AS p
INNER JOIN dim_fund AS d
    ON p.amfi_code = d.amfi_code
GROUP BY d.fund_house
ORDER BY avg_3yr_return DESC
LIMIT 5;

-- ==========================================
-- Query 8: Number of Transactions by Transaction Type
-- ==========================================

SELECT
    transaction_type,
    COUNT(*) AS total_transactions
FROM fact_transactions
GROUP BY transaction_type
ORDER BY total_transactions DESC;

-- ==========================================
-- Query 9: Average Transaction Amount by City Tier
-- ==========================================

SELECT
    city_tier,
    ROUND(AVG(amount_inr),2) AS avg_transaction_amount
FROM fact_transactions
GROUP BY city_tier
ORDER BY avg_transaction_amount DESC;

-- ==========================================
-- Query 10: Number of Mutual Fund Schemes by Category
-- ==========================================

SELECT
    category,
    COUNT(scheme_name) AS total_schemes
FROM dim_fund
GROUP BY category
ORDER BY total_schemes DESC;