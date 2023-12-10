-- --------------------------------------------------------------------------------------------

Use iot_db;
DROP PROCEDURE IF EXISTS InsertIntoCountry;

DELIMITER //
CREATE PROCEDURE InsertIntoCountry(IN city_ VARCHAR(20), IN current_place_ VARCHAR(25))
BEGIN
    INSERT INTO country (city, current_place) VALUES (city_, current_place_);
END //
DELIMITER ;

-- --------------------------------------------------------------------------------------------

USE iot_db;
DROP PROCEDURE IF EXISTS InsertIntoCountryHasMusic;

DELIMITER //
CREATE PROCEDURE InsertIntoCountryHasMusic(IN id_country INT, IN id_music INT)
BEGIN

	DECLARE country_city VARCHAR(20);
    DECLARE music_name VARCHAR(20);

    IF EXISTS (SELECT * FROM country WHERE country_id = id_country) AND
	   EXISTS (SELECT * FROM music WHERE id = id_music) AND id_country = id_music
       AND NOT EXISTS (SELECT * FROM country_has_music WHERE country_country_id = id_country
       AND music_id = id_music)THEN

        SELECT city INTO country_city FROM country WHERE country_id = id_country;
        SELECT name INTO music_name FROM music WHERE id = id_music;

        INSERT INTO country_has_music(country_country_id, music_id, price, price_curency)
        VALUES (id_country, id_music, country_city, music_name);
    ELSE
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'Something is wrong';
    END IF;
END //
DELIMITER ;

-- --------------------------------------------------------------------------------------------

USE iot_db;
DROP PROCEDURE IF EXISTS InsertStringsIntoCountry;

DELIMITER //
CREATE PROCEDURE InsertStringsIntoCountry(IN city_ VARCHAR(25), IN current_place_ VARCHAR(25))
BEGIN
    DECLARE i INT DEFAULT 1;
    WHILE i <= 10 DO
        SET city_ = CONCAT('city_', i);
        SET current_place_ = CONCAT('current_place_', i);
        INSERT INTO country (city, current_place) VALUES (city_, current_place_);
        SET i = i + 1;
    END WHILE;
END //
DELIMITER ;

-- --------------------------------------------------------------------------------------------

Use iot_db;
DROP FUNCTION IF EXISTS FunctionForOperations;

DELIMITER //
CREATE FUNCTION FunctionForOperations(operation VARCHAR(3))
RETURNS INT
READS SQL DATA
BEGIN
    DECLARE result INT;

    IF operation = 'MAX' THEN
        SELECT MAX(duration) INTO result FROM music;
    ELSEIF operation = 'MIN' THEN
        SELECT MIN(duration) INTO result FROM music;
    ELSEIF operation = 'SUM' THEN
        SELECT SUM(duration) INTO result FROM music;
    ELSEIF operation = 'AVG' THEN
        SELECT AVG(duration) INTO result FROM music;
	ELSE
       SIGNAL SQLSTATE '45000'
       SET MESSAGE_TEXT = 'Something is wrong';
    END IF;

    RETURN result;
END //
DELIMITER ;

DROP PROCEDURE IF EXISTS CallFunctionForOperations;

DELIMITER //
CREATE PROCEDURE CallFunctionForOperations(IN operation VARCHAR(3))
READS SQL DATA
BEGIN
    DECLARE result INT;
    SET result = FunctionForOperations(operation);

    SELECT result AS ResultTable;
END //
DELIMITER ;

-- --------------------------------------------------------------------------------------------

USE iot_db;
DROP PROCEDURE IF EXISTS ProcCursor;

DELIMITER //
CREATE PROCEDURE ProcCursor()
BEGIN
    DECLARE done INT DEFAULT FALSE;
    DECLARE nameT VARCHAR(25);
	DECLARE tables_num INT;
    DECLARE i INT;
    DECLARE St_Cursor10 CURSOR FOR SELECT name FROM Janre;
    DECLARE CONTINUE HANDLER FOR NOT FOUND SET done = TRUE;

    OPEN St_Cursor10;
    myLoop: LOOP
        FETCH St_Cursor10 INTO nameT;
			IF done THEN LEAVE myLoop;
        END IF;
        SET @temp_query = CONCAT('CREATE DATABASE ', nameT);
        PREPARE myquery FROM @temp_query;
        EXECUTE myquery;
        DEALLOCATE PREPARE myquery;

        SET tables_num = FLOOR(1 + RAND() * 9);
        SET i = 1;
        loop__: LOOP
            IF i > tables_num THEN
				LEAVE loop__;
            END IF;
            SET @temp_query = CONCAT('CREATE TABLE ', nameT, '.table', i, ' (id INT)');
            PREPARE myquery FROM @temp_query;
            EXECUTE myquery;
            DEALLOCATE PREPARE myquery;
            SET i = i + 1;
        END LOOP;
    END LOOP;
    CLOSE St_Cursor10;
END //
DELIMITER ;

CALL ProcCursor();

-- --------------------------------------------------------------------------------------------