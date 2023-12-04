-- ----------------------------------------------------------------------------
Процедура для параметризованої вставки
-- ----------------------------------------------------------------------------

Use iot_db;
DROP PROCEDURE IF EXISTS InsertIntoCountry;

DELIMITER //
CREATE PROCEDURE InsertIntoCountry(IN city_ VARCHAR(20), IN current_place_ VARCHAR(25))
BEGIN
    INSERT INTO country (city, current_place) VALUES (city_, current_place_);
END //
DELIMITER ;

-- ----------------------------------------------------------------------------
Процедура для генерування стрічок(Усі стрічки будуть city_1 та current_1_place)
* Вибрав ту саму таблицю, щоб не заплутатися і аби було простіше
-- ----------------------------------------------------------------------------

USE iot_db;
DROP PROCEDURE IF EXISTS InsertStringsIntoCountry;

DELIMITER //
CREATE PROCEDURE InsertStringsIntoCountry()
BEGIN
    DECLARE i INT DEFAULT 1;
    DECLARE city_ VARCHAR(20);
    DECLARE current_place_ VARCHAR(25);

    WHILE i <= 10 DO
        SET city_ = CONCAT('city_', i);
        SET current_place_ = CONCAT('current_', i, '_place');
        INSERT INTO country (city, current_place) VALUES (city_, current_place_);
        SET i = i + 1;
    END WHILE;
END //

-- ----------------------------------------------------------------------------
Функція для визначення всіх операцій(макс, мін, сума та середнє)
та виклик її у процедурі
-- ----------------------------------------------------------------------------

Use iot_db;
DROP FUNCTION IF EXISTS FunctionForOperations;

DELIMITER //
CREATE FUNCTION FunctionForOperations(duration VARCHAR(50), music VARCHAR(50), operation VARCHAR(3))
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
    END IF;
    RETURN result;
END //
DELIMITER ;


DROP PROCEDURE IF EXISTS CallFunctionForOperations;

DELIMITER //
CREATE PROCEDURE CallFunctionForOperations(IN duration VARCHAR(50), IN music VARCHAR(50), IN operation VARCHAR(3))
READS SQL DATA
BEGIN
    DECLARE result INT;
    SET result = FunctionForOperations(duration, music, operation);

    SELECT result AS Result;
END //
DELIMITER;

-- ----------------------------------------------------------------------------
Процедура для створення таблиці з даним часом і рандом полями
від 1 до 10
Тут використовується курсор
-- ----------------------------------------------------------------------------

USE iot_db;
DROP PROCEDURE IF EXISTS CreateDynamicTables;

DELIMITER //

CREATE PROCEDURE CreateDynamicTables()
BEGIN
    DECLARE table_name VARCHAR(50);
    DECLARE column_count INT;
    DECLARE column_query VARCHAR(1000);
    DECLARE i INT DEFAULT 0;
    DECLARE max_i INT DEFAULT 1;
    DECLARE column_definitions VARCHAR(1000) DEFAULT '';

    SET max_i = FLOOR(RAND() * 9) + 1;
    SET table_name = CONCAT('table_', UNIX_TIMESTAMP());
    SET column_count = FLOOR(RAND() * 9) + 1;

    WHILE i < column_count DO
        SET column_definitions = CONCAT(column_definitions, 'column_', i, ' VARCHAR(50),');
        SET i = i + 1;
    END WHILE;

    SET column_definitions = SUBSTRING(column_definitions, 1, LENGTH(column_definitions) - 1);

    SET @column_query = CONCAT('CREATE TABLE ', table_name, ' (', column_definitions, ');');

    PREPARE stmt FROM @column_query;

    EXECUTE stmt;
    DEALLOCATE PREPARE stmt;
END //

DELIMITER ;

CALL CreateDynamicTables();
-- ----------------------------------------------------------------------------
Процедура для створення двох таблиць із штампом часу і копіюванням
всіх полів і таблиці жанр(там найменше полів, тому було найзручніше взяти)
-- ----------------------------------------------------------------------------

USE iot_db;
DROP PROCEDURE IF EXISTS CopyRows;

DELIMITER //

CREATE PROCEDURE CopyRows()
BEGIN
    DECLARE done INT DEFAULT FALSE;
    DECLARE a INT;
    DECLARE cur CURSOR FOR SELECT janre_id FROM janre;
    DECLARE CONTINUE HANDLER FOR NOT FOUND SET done = TRUE;

    SET @table1 = CONCAT('table_', UNIX_TIMESTAMP());
    SET @table2 = CONCAT('table_', UNIX_TIMESTAMP() + 1);

    SET @createTable = CONCAT('CREATE TABLE ', @table1, ' LIKE janre;');
    PREPARE stmt FROM @createTable;
    EXECUTE stmt;
    DEALLOCATE PREPARE stmt;

    SET @createTable = CONCAT('CREATE TABLE ', @table2, ' LIKE janre;');
    PREPARE stmt FROM @createTable;
    EXECUTE stmt;
    DEALLOCATE PREPARE stmt;

    OPEN cur;

    read_loop: LOOP
        FETCH cur INTO a;

        IF done THEN
            LEAVE read_loop;
        END IF;

        IF RAND() < 0.5 THEN
            SET @insert = CONCAT('INSERT INTO ', @table1, ' SELECT * FROM janre WHERE janre_id = ', a, ';');
        ELSE
            SET @insert = CONCAT('INSERT INTO ', @table2, ' SELECT * FROM janre WHERE janre_id = ', a, ';');
        END IF;

        PREPARE stmt FROM @insert;
        EXECUTE stmt;
        DEALLOCATE PREPARE stmt;
    END LOOP;

    CLOSE cur;
END //

DELIMITER ;

-- ----------------------------------------------------------------------------