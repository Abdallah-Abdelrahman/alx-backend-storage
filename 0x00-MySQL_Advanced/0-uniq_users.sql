-- creates a table users following these requirements
CREATE TABLE IF NOT EXISTS users (
    id INT PRIMARY KEY AUTOINCREMENT,
    email VARCHAR(255) NOT NULL UNIQUE,
    name VARCHAR(255),
);

