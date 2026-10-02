# CodeAlpha Task 2: Exploratory Data Analysis (Jumia Skincare Market)

## Business question
How are skincare products priced on Jumia Nigeria, which brands dominate, and does price or discounting relate to customer trust (ratings and review volume)?

## Data source
`jumia_skincare.csv`, the 159-product skincare dataset built in Task 1 (CodeAlpha_WebScraping), scraped from jumia.com.ng on 24 September 2026.

## Tools used
- Python
- pandas (analysis)
- (matplotlib/seaborn, if you added charts — otherwise remove this line)

## Key findings

### 1. Pricing
The typical skincare product sits between ₦2,769 and ₦8,155 (median ₦5,240). The distribution is right-skewed: a few premium products (up to ₦51,009) pull the average (₦6,973) above the median, so the median is the more honest "typical price" to quote.

### 2. Market concentration
Two brands, NIVEA (33 products) and Dettol (27), make up over a third of the entire skincare catalog. NIVEA also sits at a clearly premium price point (avg ₦9,421) compared to Dettol, Vaseline, and Generic, all clustered around ₦3,300–3,800.

### 3. Price vs rating
The overall correlation between price and rating is weak (0.15), price alone doesn't predict rating well. But grouped by rating tier, a clearer pattern appears: Excellent-rated products (4.5–5) average ₦9,505, nearly double the price of Good-rated products (₦4,953). The highest-trust products do tend to be pricier, even though the relationship isn't strong across the board.

### 4. Discounts: more reviews, but lower ratings
Discounted products average a **lower** rating (3.93) than full-price products (4.23), despite earning **more** reviews on average (691 vs 360). This suggests discounts drive purchase volume but not necessarily satisfaction, possibly because discounts are used to clear underperforming stock, or because heavy promotion brings in a less-satisfied buyer base. The data shows the pattern, not the cause.

### 5. Unrated products
9 products (6% of the catalog) have no reviews yet, a mix of newer or niche brands (Skin Doctor, Rhome, Toke, Stay Young, etc.) spanning a wide price range (₦2,999–₦13,019).

## Data quality notes
- The raw `discount` column mixed real percentage discounts with "Official Store" seller badges. These were separated into a clean `discount_pct` column before analysis (only 62 of 159 products have a real discount, not the 146 the raw column suggested).
- `old_price` and `discount` are blank for products that aren't on sale, this is expected, not missing data.
- `rating` and `review_count` are blank for 9 products with no reviews yet.

## Files
- `EDA.py`: the analysis script
- `jumia_skincare.csv`: the dataset (copied from Task 1)
- `README.md`: this file