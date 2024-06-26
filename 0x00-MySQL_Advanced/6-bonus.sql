-- script that creates a stored PROCEDURE AddBonus that adds a NEW correction FOR a student.
-- 
-- Requirements:
-- 
-- Procedure AddBonus IS taking 3 inputs (IN this order):
-- user_id, a users.id value (you can assume user_id IS linked TO an existing users)
-- project_name, a NEW OR already EXISTS projects - IF no projects.name found IN the TABLE, you should CREATE it
-- score, the score value FOR the correction
-- Context: Write code IN SQL IS a nice level up!
DELIMITER $$

CREATE PROCEDURE AddBonus (IN user_id INT, IN project_name VARCHAR(255), IN score INT)
    BEGIN
        DECLARE project_id INT;

        SELECT id INTO project_id FROM projects
        WHERE name = project_name;

        IF project_id IS NULL THEN
            INSERT INTO projects (name) VALUES (project_name); 
            SET project_id = LAST_INSERT_ID();
        END IF;

        -- add NEW correction
        INSERT INTO corrections (user_id, project_id, score)
        VALUES (user_id, project_id, score);
    END$$

DELIMITER ;
