DROP TRIGGER IF EXISTS enforce_workplace_type ON workplace CASCADE;
DROP TRIGGER IF EXISTS enforce_order_in_contains ON orders CASCADE;

--IC1

ALTER TABLE employee
DROP CONSTRAINT check_employee_age,
ADD CONSTRAINT check_employee_age
CHECK (DATE_PART('Year', AGE(CURRENT_DATE,bdate)) >= 18);

--IC2

CREATE OR REPLACE FUNCTION check_workplace_type()
    RETURNS TRIGGER AS $$
    BEGIN
        IF (NEW.address IN (SELECT address FROM office) AND NEW.address IN (SELECT address FROM warehouse)) THEN
            RAISE EXCEPTION 'The Workplace in % cannot be both an Office and a Warehouse', NEW.address;
        END IF;
        IF (NEW.address NOT IN (SELECT address FROM office) AND NEW.address NOT IN (SELECT address FROM warehouse)) THEN
            RAISE EXCEPTION 'The Workplace in % is mandatorily an Office or an Warehouse', NEW.address;
        END IF;
        RETURN NEW;
    END;
$$ LANGUAGE plpgsql;

CREATE CONSTRAINT TRIGGER enforce_workplace_type
    AFTER INSERT ON workplace DEFERRABLE
    FOR EACH ROW
    EXECUTE FUNCTION check_workplace_type();


--IC3

CREATE OR REPLACE FUNCTION check_order_in_contains()
    RETURNS TRIGGER AS $$
    BEGIN
        IF NEW.order_no NOT IN (SELECT order_no FROM contains) THEN
            RAISE EXCEPTION 'The Order % must appear in Contains', NEW.order_no;
        END IF;
        RETURN NEW;
    END;
$$ LANGUAGE plpgsql;

CREATE CONSTRAINT TRIGGER enforce_order_in_contains
    AFTER INSERT ON orders DEFERRABLE
    FOR EACH ROW
    EXECUTE FUNCTION check_order_in_contains();

-- Drop the existing foreign key constraints
ALTER TABLE orders DROP CONSTRAINT orders_cust_no_fkey;
ALTER TABLE pay DROP CONSTRAINT pay_order_no_fkey;
ALTER TABLE contains DROP CONSTRAINT contains_order_no_fkey;
ALTER TABLE contains DROP CONSTRAINT contains_SKU_fkey;
ALTER TABLE supplier DROP CONSTRAINT supplier_SKU_fkey;
ALTER TABLE delivery DROP CONSTRAINT delivery_TIN_fkey;

ALTER TABLE orders
    ADD CONSTRAINT orders_cust_no_fkey
    FOREIGN KEY (cust_no)
    REFERENCES customer (cust_no)
    ON DELETE CASCADE;

ALTER TABLE pay
    ADD CONSTRAINT pay_order_no_fkey
    FOREIGN KEY (order_no)
    REFERENCES orders (order_no)
    ON DELETE CASCADE;

ALTER TABLE contains
    ADD CONSTRAINT contains_order_no_fkey
    FOREIGN KEY (order_no)
    REFERENCES orders (order_no)
    ON DELETE CASCADE;

ALTER TABLE contains
    ADD CONSTRAINT contains_SKU_fkey
    FOREIGN KEY (SKU)
    REFERENCES product (SKU)
    ON DELETE CASCADE;

ALTER TABLE supplier
    ADD CONSTRAINT supplier_SKU_fkey
    FOREIGN KEY (SKU)
    REFERENCES product (SKU)
    ON DELETE CASCADE;

ALTER TABLE delivery
    ADD CONSTRAINT delivery_TIN_fkey
    FOREIGN KEY (TIN)
    REFERENCES supplier (TIN)
    ON DELETE CASCADE;

AlTER TABLE customer DROP CONSTRAINT check_address_format;
AlTER TABLE workplace DROP CONSTRAINT check_address_format;
AlTER TABLE supplier DROP CONSTRAINT check_address_format;

ALTER TABLE customer
ADD CONSTRAINT check_address_format
CHECK (address ~ '^[A-Za-z ,.-]+\s[0-9]{4}-[0-9]{3}\s[A-Za-z ]+$');

ALTER TABLE workplace
ADD CONSTRAINT check_address_format
CHECK (address ~ '^[A-Za-z ,.-]+\s[0-9]{4}-[0-9]{3}\s[A-Za-z ]+$');

ALTER TABLE supplier
ADD CONSTRAINT check_address_format
CHECK (address ~ '^[A-Za-z ,.-]+\s[0-9]{4}-[0-9]{3}\s[A-Za-z ]+$');