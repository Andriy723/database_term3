-- --------------------------------------------------------------------------------------------

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

-- --------------------------------------------------------------------------------------------

USE iot_db;
DROP TRIGGER IF EXISTS no_delete;

DELIMITER //
CREATE TRIGGER no_delete BEFORE DELETE ON person_profile FOR EACH ROW
BEGIN
	SIGNAL SQLSTATE '45000'
    SET MESSAGE_TEXT = 'Deletion is not allowed';
END //
DELIMITER ;

-- --------------------------------------------------------------------------------------------

USE iot_db;
DROP TRIGGER IF EXISTS regex_str_create;
DROP TRIGGER IF EXISTS regex_str_update;

DELIMITER //
CREATE TRIGGER regex_str_create BEFORE INSERT ON janre FOR EACH ROW
BEGIN
        IF(NOT NEW.name RLIKE '[^{A|M|Z}[0-9]{5}[A-Za-z]{2}$]') THEN
            SIGNAL SQLSTATE '45000'
            SET MESSAGE_TEXT = 'name does not match regex';
        END IF;
END //

DELIMITER //
CREATE TRIGGER regex_str_update BEFORE UPDATE ON janre FOR EACH ROW
BEGIN
        IF(NOT NEW.name RLIKE '[^{A|M|Z}[0-9]{5}[A-Za-z]{2}$]') THEN
            SIGNAL SQLSTATE '45000'
            SET MESSAGE_TEXT = 'name does not match regex';
        END IF;
END //
DELIMITER ;

-- --------------------------------------------------------------------------------------------

USE iot_db;
DROP TRIGGER IF EXISTS regex_str_create_0;
DROP TRIGGER IF EXISTS regex_str_update_0;

DELIMITER //
CREATE TRIGGER regex_str_create_0 BEFORE INSERT ON albom FOR EACH ROW
BEGIN
        IF(NOT NEW.name RLIKE '[^[A-LO-QS-Z]{2}-[0-9]{3}-[0-9]{2}$]') THEN
            SIGNAL SQLSTATE '45000'
            SET MESSAGE_TEXT = 'name does not match regex';
        END IF;
END //

DELIMITER //
CREATE TRIGGER regex_str_update_0 BEFORE UPDATE ON albom FOR EACH ROW
BEGIN
        IF(NOT NEW.name RLIKE '[^[A-LO-QS-Z]{2}-[0-9]{3}-[0-9]{2}$]') THEN
            SIGNAL SQLSTATE '45000'
            SET MESSAGE_TEXT = 'name does not match regex';
        END IF;
END //
DELIMITER ;

-- --------------------------------------------------------------------------------------------