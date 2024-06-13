-- creates a TABLE users following these requirements:
-- 
-- With these attributes:
-- id, integer, never NULL, auto increment AND PRIMARY KEY
-- email, string (255 characters), never NULL AND UNIQUE
-- name, string (255 characters)
-- country, enumeration of countries: US, CO AND TN, never NULL (= DEFAULT will be the first element of the enumeration, here US)
-- If the TABLE already EXISTS, your script should NOT fail
CREATE TABLE IF NOT EXISTS users (
	id INT AUTO_INCREMENT,
	email VARCHAR(255) NOT NULL,
	name VARCHAR(255),
	country ENUM('US', 'CO', 'TN') NOT NULL DEFAULT 'US',
	PRIMARY KEY(id),
	UNIQUE(email)
);
