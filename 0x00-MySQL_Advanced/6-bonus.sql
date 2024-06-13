-- script that creates a stored procedure AddBonus that adds a new correction for a student.
-- 
-- Requirements:
-- 
-- Procedure AddBonus is taking 3 inputs (in this order):
-- user_id, a users.id value (you can assume user_id is linked to an existing users)
-- project_name, a new or already exists projects - if no projects.name found in the table, you should create it
-- score, the score value for the correction
-- Context: Write code in SQL is a nice level up!
DELIMITER $$;
CREATE PROCEDURE AddBonus(IN user_id INT, IN project_name VARCHAR(255), IN score INT)
BEGIN
        DECLARE id INT;

        -- check if the project already exists
        SELECT id FROM projects WHERE name = project_name;

        -- if the project does not exist, create it
        IF id IS NULL THEN
                INSERT INTO projects (name) VALUES (project_name);
                SET id = LAST_INSERT_ID();
        END IF;

        -- Add the new correction
        INSERT INTO corrections (user_id, project_id, score) VALUES (user_id, id, score);
END;$$
DELIMITER ;$$
