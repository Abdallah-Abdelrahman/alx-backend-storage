-- script that creates a trigger that decreases the quantity of an item after adding a new order.
-- 
-- Quantity IN the TABLE items can be negative.
CREATE TRIGGER decrease_quantity AFTER INSERT ON orders
    FOR EACH ROW
	UPDATE items
	    SET items.quantity = items.quantity - NEW.number
	    WHERE NEW.item_name = items.name;
