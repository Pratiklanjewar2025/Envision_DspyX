from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
import time
import re

# ======================
# CONFIG
# ======================
CATEGORIES = {
    "bluetooth_headphones": "https://www.snapdeal.com/search?keyword=bluetooth%20headphones",
    "power_bank": "https://www.snapdeal.com/search?keyword=power%20bank",
    "smart_watch": "https://www.snapdeal.com/search?keyword=smart%20watch",
    "perfume": "https://www.snapdeal.com/search?keyword=perfume",
    "men_shoes": "https://www.snapdeal.com/search?keyword=men%20shoes"
}

PAGES_PER_CATEGORY = 1
MAX_PRODUCTS = 120
SELLER_SCRAPE_EVERY = 2

# ======================
# DRIVER SETUP
# ======================
options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")

driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install()),
    options=options
)

rows = []

# ======================
# SEARCH PAGE SCRAPING
# ======================
print("🔍 Collecting raw marketplace data...")

for category, base_url in CATEGORIES.items():
    for page in range(PAGES_PER_CATEGORY):
        if len(rows) >= MAX_PRODUCTS:
            break

        driver.get(f"{base_url}&page={page}")
        time.sleep(5)

        products = driver.find_elements(By.CLASS_NAME, "product-tuple-listing")

        for p in products:
            if len(rows) >= MAX_PRODUCTS:
                break

            try:
                name = p.find_element(By.CLASS_NAME, "product-title").text
                product_url = p.find_element(By.CLASS_NAME, "dp-widget-link").get_attribute("href")

                try:
                    price = p.find_element(By.CLASS_NAME, "product-price").text
                    price = price.replace("Rs.", "").replace(",", "").strip()
                except:
                    price = None

                try:
                    mrp = p.find_element(By.CLASS_NAME, "product-desc-price").text
                    mrp = mrp.replace("Rs.", "").replace(",", "").strip()
                except:
                    mrp = None

                try:
                    style = p.find_element(By.CLASS_NAME, "filled-stars").get_attribute("style")
                    rating = round((float(re.findall(r"\d+", style)[0]) / 100) * 5, 1)
                except:
                    rating = None

                try:
                    reviews = p.find_element(By.CLASS_NAME, "product-rating-count").text
                    reviews = reviews.replace("(", "").replace(")", "")
                except:
                    reviews = None

                rows.append({
                    "product_name": name,
                    "category": category,
                    "price": price,
                    "mrp": mrp,
                    "rating": rating,
                    "review_count": reviews,
                    "product_url": product_url,
                    "seller_name": None,
                    "seller_rating": None
                })

            except:
                continue

# ======================
# SELLER INFO FROM PDP
# ======================
print("🏪 Collecting seller information...")

for i, row in enumerate(rows):
    if i % SELLER_SCRAPE_EVERY != 0:
        continue

    try:
        driver.get(row["product_url"])
        time.sleep(4)

        try:
            row["seller_name"] = driver.find_element(
                By.CSS_SELECTOR, "a.pdp-e-seller-info-name"
            ).text.strip()
        except:
            row["seller_name"] = None

        try:
            txt = driver.find_element(
                By.CSS_SELECTOR, "div.pdp-e-seller-info-score"
            ).text
            row["seller_rating"] = float(re.findall(r"\d+\.?\d*", txt)[0])
        except:
            row["seller_rating"] = None

    except:
        continue

driver.quit()

# ======================
# SAVE RAW DATA
# ======================
raw_df = pd.DataFrame(rows)
raw_df.to_csv("raw_data.csv", index=False)

print("✅ RAW DATA SAVED")
print("Rows:", raw_df.shape[0])
print("Seller rows:", raw_df["seller_name"].notna().sum())
