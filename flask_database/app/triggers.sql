-- ---------------------------------------------------------
Тригер для плейлисту та музики(для 1 to many зв^зку)
-- ---------------------------------------------------------

USE iot_db;
DROP TRIGGER IF EXISTS before_insert_update_playlist;

DELIMITER //
CREATE TRIGGER before_insert_update_playlist BEFORE INSERT ON playlist FOR EACH ROW
    BEGIN
        DECLARE music_count INT;

        SELECT COUNT(*) INTO music_count FROM music WHERE id = NEW.music_id;

        IF music_count = 0 THEN
            SIGNAL SQLSTATE '45000'
            SET MESSAGE_TEXT = 'Music with this id doesn`t exist';
        END IF;
    END //
DELIMITER ;

-- ---------------------------------------------------------
Тригер без закінчення на 2 нулі
-- ---------------------------------------------------------

USE iot_db;
DROP TRIGGER IF EXISTS no_double_zeros;

DELIMITER //
CREATE TRIGGER no_double_zeros BEFORE INSERT ON janre FOR EACH ROW
BEGIN
    IF NEW.janre_id LIKE '%00' THEN
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'Can`t end with double zeros';
    END IF;
END //
DELIMITER ;

-- ---------------------------------------------------------
Тригер без змін(модифікування)
-- ---------------------------------------------------------

USE iot_db;
DROP TRIGGER IF EXISTS no_modification;

DELIMITER //
CREATE TRIGGER no_modification BEFORE UPDATE ON person_profile FOR EACH ROW
BEGIN
    SIGNAL SQLSTATE '45000'
    SET MESSAGE_TEXT = 'Modification is not allowed';
END //
DELIMITER ;

-- ---------------------------------------------------------
Тригер тільки певні імена у полі таблиці(їх 4)
-- ---------------------------------------------------------

USE iot_db;
DROP TRIGGER IF EXISTS only_particular_names;

DELIMITER //
CREATE TRIGGER only_particular_names BEFORE INSERT ON music_labels FOR EACH ROW
BEGIN
    IF NEW.label_name NOT IN ('Svitlana', 'Petro', 'Olha', 'Taras') THEN
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'Invalid name. Name must be only Svitlana, Petro, Olha, or Taras';
    END IF;
END //
DELIMITER ;
