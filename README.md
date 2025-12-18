🛒**GreyMarketsentinel** :  AI‑Based Grey Market & Illegal Product Sales Detection

Team DspyX

Vishvesh Paturkar – PICT, Pune

Tejas Bankar – PCCOE, Pune

Pratik Lanjewar – PCCOE, Pune


This project aims to detect grey market and potentially illegal product sales on e‑commerce platforms using data scraping, preprocessing, feature engineering, and risk intelligence.

Unauthorized sellers often exploit:

    Abnormal discounts

    Misleading product titles

    Fake or low‑trust reviews

    Inconsistent pricing patterns

Our system builds an analytical dataset that enables:

    Product‑level anomaly detection

    Seller behavior approximation

    Risk scoring for compliance and brand protection

📂 Repository Structure

├── data_collection.py          # Scrapes raw product & seller data
├── data_preprocessing.py       # Cleans data & generates derived features
├── snapdeal_raw_data.csv       # Raw scraped dataset
├── snapdeal_derived_data.csv   # Final analytical dataset
├── preprocessing_notebook.ipynb# Round‑2 preprocessing & visualization
└── README.md                   # Project documentation

📊 Dataset 1: Raw Dataset (snapdeal_raw_data.csv)

🔹 Description
This dataset contains only information directly scraped from Snapdeal product listings and product detail pages.
No transformations or assumptions are applied here.

🔹 Raw Columns
Column	Description
product_name	Product title as shown on the platform
category	Search category (e.g., headphones, power bank)
price	Current selling price
mrp	Original listed MRP
rating	Average product rating
review_count	Number of customer reviews
product_url	Product detail page URL
seller_name	Seller name (if available)
seller_rating	Seller rating (if available)



📈 Dataset 2: Derived Dataset (snapdeal_derived_data.csv)

🔹 Description
This dataset is created after cleaning, preprocessing, feature engineering, and risk signal generation.
It is the primary dataset used for analysis, visualization, and modeling.

🔹 Derived & Analytical Columns
🧮 Pricing & Discount Features
Column	Purpose
discount_pct	Identifies unusually high discounts
price_to_mrp_ratio	Detects underpricing
category_avg_price	Average price within category
price_deviation_from_category	Measures pricing anomaly
⭐ Trust & Review Features
Column	Purpose
rating_review_ratio	Detects fake trust patterns
review_density	Reviews relative to price
📝 Listing Behavior Features
Column	Purpose
generic_word_count	Detects misleading/promotional keywords
uppercase_ratio	Flags aggressive listing styles
⚠️ Risk Intelligence
Column	Purpose
extreme_discount_flag	Discount > 60%
suspicious_trust_flag	High rating + low reviews
aggressive_listing_flag	Keyword & casing abuse
risk_score	Aggregate risk signal
risk_level	Low / Medium / High risk
🧠 Seller Behavior Approximation
Column	Purpose
seller_cluster_id	Groups sellers/products by behavioral similarity

📌 Note
Even with limited seller metadata, we infer seller behavior using pricing, listing style, and trust signals, similar to real-world trust & safety systems.
🛠️ Preprocessing & Transformation Pipeline
1️⃣ Raw Data Inspection

    Missing value analysis

    Data type validation

    Category distribution

Visualizations:

    Missing value heatmap

    Listings per category bar chart

2️⃣ Data Cleaning

    Converted price, MRP, ratings to numeric

    Removed invalid price/MRP rows

    Retained missing seller fields as NULL

Visualizations:

    Before vs after row count

    Price distribution boxplots

3️⃣ Feature Engineering (Core Contribution)

    Created discount, trust, listing, and pricing anomaly features

    Normalized selected features for analytics

Visualizations:

    Discount distribution histogram

    Price vs rating scatter plot

    Category-wise price deviation boxplot

4️⃣ Risk Logic Design

Risk is assigned using domain‑driven rules:

    Extreme discounts → counterfeit / grey market risk

    High ratings + few reviews → fake trust

    Aggressive keywords → misleading listings

Visualizations:

    Risk level distribution

    Correlation heatmap of risk features


