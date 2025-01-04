DROP DATABASE IF EXISTS enspirket;

CREATE DATABASE IF NOT EXISTS enspirket;

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

CREATE TABLE IF NOT EXISTS drinks(
    drink_id varchar(10) NOT NULL,
    drink_name varchar(10) NOT NULL,
    temp varchar(10) NOT NULL,
    PRIMARY KEY(drink_id)
);

CREATE TABLE IF NOT EXISTS foods(
    food_id varchar(10) NOT NULL,
    food_name varchar(10) NOT NULL,
    hot_cold BOOLEAN NOT NULL,
    PRIMARY KEY(food_id)
);

CREATE TABLE IF NOT EXISTS purchases(
    purchase_id varchar(10) NOT NULL,
    customer_id varchar(10) NOT NULL,
    purchase_date DATE NOT NULL,
    PRIMARY KEY(purchase_id)
);
