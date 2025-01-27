DROP DATABASE IF EXISTS test;

CREATE DATABASE IF NOT EXISTS test;

USE test;

CREATE TABLE IF NOT EXISTS price(
    price_id VARCHAR(10) NOT NULL,
    price DECIMAL(4,2) NOT NULL,
    product_type VARCHAR(50) NOT NULL,
    product_category VARCHAR(50) NOT NULL,
    price_large DECIMAL(4,2),
    price_small DECIMAL(4,2),
    PRIMARY KEY(price_id)
);

CREATE TABLE IF NOT EXISTS product(
    product_id VARCHAR(10) NOT NULL,
    product_name_eng VARCHAR(50) NOT NULL,
	product_name_chinese VARCHAR(50) NOT NULL,
    product_type VARCHAR(50) NOT NULL,
    product_category VARCHAR(50) NOT NULL,
    price_id VARCHAR(10) NOT NULL,
    PRIMARY KEY (product_id),
    FOREIGN KEY (price_id) REFERENCES price(price_id)
);

CREATE TABLE IF NOT EXISTS promotion(
    promotion_id VARCHAR(10) NOT NULL,
    promotion_price DECIMAL(4,2) NOT NULL,
	promotion_percent DECIMAL(4,2) NOT NULL,
    start_date DATETIME NOT NULL,
    end_date DATETIME,
    product_id VARCHAR(10) NOT NULL,
    PRIMARY KEY (promotion_id),
    FOREIGN KEY (product_id) REFERENCES product(product_id)
);