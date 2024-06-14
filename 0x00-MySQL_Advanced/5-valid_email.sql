-- script that creates a TRIGGER that resets the attribute valid_email only when the email has been changed.
-- 
-- Context: Nothing related TO MySQL, but perfect FOR USER email validation - distribute the logic TO the DATABASE itself!
DROP TRIGGER IF EXISTS `validate_email`;
DELIMITER $$

CREATE TRIGGER `validate_email` AFTER UPDATE ON users
FOR EACH ROW
BEGIN
    IF OLD.email != NEW.email
    THEN
        SET valid_email = 0;
    END IF;
END$$

DELIMITER ;
