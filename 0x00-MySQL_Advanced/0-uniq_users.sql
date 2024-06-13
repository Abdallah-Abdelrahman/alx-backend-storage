-- creates a table users following these requirements
CREATE TABLE IF NOT EXISTS users (
    -- `id` is an integer that auto increments and serves as the primary key
    id INT AUTO_INCREMENT,

    -- `email` is a string of up to 255 characters that must be unique and not null
    email VARCHAR(255) NOT NULL,

    -- `name` is a string of up to 255 characters
    name VARCHAR(255),

    -- Define `id` as the primary key
    PRIMARY KEY (id),

    -- Ensure that `email` is unique across all records
    UNIQUE (email)
);

