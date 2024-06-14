-- script that creates a TRIGGER that decreases the quantity of an item AFTER adding a NEW order.
--
-- Quantity IN the TABLE items can be negative.
DROP TRIGGER IF EXISTS `decrease_quantity`;

DELIMITER $$
CREATE TRIGGER `decrease_quantity`
AFTER INSERT ON orders
FOR EACH ROW
    BEGIN
        UPDATE items
        SET quantity = quantity - NEW.number
        WHERE name = NEW.item_name;
    END$$
DELIMITER ;
