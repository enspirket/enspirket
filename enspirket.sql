DROP DATABASE IF EXISTS enspirket;

CREATE DATABASE IF NOT EXISTS enspirket;

-- just to test the push

use enspirket;

CREATE TABLE IF NOT EXISTS customers(
    customers_id varchar(10) NOT NULL,
    first_name varchar(10) NOT NULL,
    last_name varchar(10) NOT NULL,
    email varchar(50) NOT NULL,
    num_purchase INTEGER NOT NULL,
    PRIMARY KEY(customers_id)
);

CREATE TABLE IF NOT EXISTS employee(
    employee_id varchar(10) NOT NULL,
    first_name varchar(10) NOT NULL,
    last_name varchar(10) NOT NULL,
    email varchar(50) NOT NULL,
    PRIMARY KEY(employee_id)
);

CREATE TABLE IF NOT EXISTS purchases(
    purchase_id varchar(10) NOT NULL,
    customer_id varchar(10) NOT NULL,
    purchase_date DATE NOT NULL,
    PRIMARY KEY(purchase_id)
);

CREATE TABLE IF NOT EXISTS price(
    price_id INTEGER NOT NULL AUTO_INCREMENT,
    price DECIMAL(7,2) NOT NULL,
    category varchar(50) NOT NULL,
    PRIMARY KEY(price_id)
);

CREATE TABLE IF NOT EXISTS drinks(
    drink_id INTEGER NOT NULL AUTO_INCREMENT,
    drink_name varchar(50) NOT NULL,
    drink_price_id INTEGER NOT NULL,
    PRIMARY KEY(drink_id),
    FOREIGN KEY(drink_price_id) REFERENCES price(price_id)
);

CREATE TABLE IF NOT EXISTS snacks(
    snack_id INTEGER NOT NULL AUTO_INCREMENT,
    snack_name varchar(50) NOT NULL,
    snack_price_id INTEGER NOT NULL,
    PRIMARY KEY(snack_id),
    FOREIGN KEY(snack_price_id) REFERENCES price(price_id)
);

CREATE TABLE IF NOT EXISTS combos(
    combo_id INTEGER NOT NULL AUTO_INCREMENT,
    combo_name varchar(50) NOT NULL,
    combo_price_id INTEGER NOT NULL,
    PRIMARY KEY(combo_id),
    FOREIGN KEY(combo_price_id) REFERENCES price(price_id)
);

CREATE TABLE IF NOT EXISTS toppings(
    topping_id INTEGER NOT NULL AUTO_INCREMENT,
    topping_name varchar(50) NOT NULL,
    topping_price_id INTEGER NOT NULL,
    PRIMARY KEY(topping_id),
    FOREIGN KEY(topping_price_id) REFERENCES price(price_id)
);