CREATE TABLE inventory (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    item_name VARCHAR(255) NOT NULL,
    info VARCHAR(255) NOT NULL,
    price DECIMAL(10,2) NOT NULL,
    stock INTEGER NOT NULL,
    image_url VARCHAR(255) NOT NULL,
    category VARCHAR(255) NOT NULL
);

CREATE TABLE users (
    username VARCHAR(255) PRIMARY KEY NOT NULL,
    password_hash VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL,
    first_name VARCHAR(255) NOT NULL,
    last_name VARCHAR(255) NOT NULL
);

CREATE TABLE sales (
    sale_id INTEGER PRIMARY KEY AUTOINCREMENT,
    transaction_id VARCHAR(255) NOT NULL,
    username VARCHAR(255) NOT NULL,
    item_id INTEGER NOT NULL,
    quantity INTEGER NOT NULL,
    sale_date DATETIME NOT NULL,
    cost DECIMAL(10,2) NOT NULL,
    FOREIGN KEY (username) REFERENCES users(username),
    FOREIGN KEY (item_id) REFERENCES inventory(id)
);

CREATE TABLE customers (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_name VARCHAR(255) NULL,
    email VARCHAR(255) NULL,
    first_name VARCHAR(255) NULL,
    last_name VARCHAR(255) NULL
);

CREATE TABLE movies (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    item_code VARCHAR(255) NOT NULL,
    title VARCHAR(255) NULL,
    [description] VARCHAR(255) NULL,
    genre VARCHAR(255) NULL
);

CREATE TABLE theaters (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    location_code VARCHAR(255) NOT NULL,
    [name] VARCHAR(255) NULL,
    city VARCHAR(255) NULL,
    zip_code VARCHAR(255) NULL
);

CREATE TABLE shows (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    show_code VARCHAR(255) NOT NULL,
    movie_title VARCHAR(255) NULL,
    running_time INTEGER NULL,
    [date] DATETIME NULL
);
