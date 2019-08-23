# query import csv default mysql folder
#SHOW VARIABLES LIKE "secure_file_priv";
#SET SQL_SAFE_UPDATES = 0;

# create player table
DROP TABLE IF EXISTS player;

CREATE TABLE IF NOT EXISTS player (
    operator_id INT(11), 
    player_id INT(11),
    first_name VARCHAR(65),
    last_name_01 VARCHAR(65),
    last_name_02 VARCHAR(65),
    sex CHAR(1),
    birthdate DATE,
    document_type_id VARCHAR(10),
	identification_document VARCHAR(65),
    email VARCHAR(65),
    login VARCHAR(65),
    pseudonym VARCHAR(65),
    resident CHAR(1),
    address VARCHAR(255),
    country VARCHAR(65),
    telephone VARCHAR(65),
    activation_date DATE,
    fiscal_region VARCHAR(65),
    payment_method_id VARCHAR(10),
    cnj_status VARCHAR(10),
    deposit_limit_day INT(11),
    deposit_limit_month INT(11),
    deposit_limit_year INT(11),
    vsvdi_status VARCHAR(10),
    vsvdi_date DATE,
    vdocumental_status VARCHAR(10),
    vdocumental_date DATE,
    PRIMARY KEY (operator_id, player_id)
)  ENGINE=INNODB;

# import player data
LOAD DATA INFILE '/var/lib/mysql-files/player_register.csv' 
INTO TABLE player
FIELDS TERMINATED BY ',' 
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;

# remove \r in player table
SET SQL_SAFE_UPDATES=0;
update player SET first_name = TRIM(TRAILING '\r' FROM first_name);
update player SET last_name_01 = TRIM(TRAILING '\r' FROM last_name_01);
update player SET last_name_02 = TRIM(TRAILING '\r' FROM last_name_02);    
update player SET telephone = TRIM(TRAILING '\r' FROM telephone);
update player SET sex = TRIM(TRAILING '\r' FROM sex);
update player SET identification_document = TRIM(TRAILING '\r' FROM identification_document);
update player SET document_type_id = TRIM(TRAILING '\r' FROM document_type_id);
update player SET email = TRIM(TRAILING '\r' FROM email);
update player SET login = TRIM(TRAILING '\r' FROM login);
update player SET pseudonym = TRIM(TRAILING '\r' FROM pseudonym);
update player SET resident = TRIM(TRAILING '\r' FROM resident);
update player SET address = TRIM(TRAILING '\r' FROM address);
update player SET country = TRIM(TRAILING '\r' FROM country);
update player SET fiscal_region = TRIM(TRAILING '\r' FROM fiscal_region);
update player SET payment_method_id = TRIM(TRAILING '\r' FROM payment_method_id);
update player SET cnj_status = TRIM(TRAILING '\r' FROM cnj_status);
update player SET vdocumental_status = TRIM(TRAILING '\r' FROM vdocumental_status);
update player SET vsvdi_status = TRIM(TRAILING '\r' FROM vsvdi_status);

# create account table
DROP TABLE IF EXISTS account;
                                        
CREATE TABLE IF NOT EXISTS account (
    account_id INT(11), 
    operator_id INT(11), 
    player_id INT(11),
    checkin_time DATETIME,
    checkout_time DATETIME,
    last_visit DATETIME,
    init_token INT(11),
    deposit INT(11),
    profit INT(11),
    withdrawal INT(11),
    final_token INT(11),
    player_skill FLOAT,
    bettings INT(11),
    PRIMARY KEY (account_id)
)  ENGINE=INNODB;

# import account data
LOAD DATA INFILE '/var/lib/mysql-files/account_register.csv' 
INTO TABLE account
FIELDS TERMINATED BY ',' 
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;

# create betting table
DROP TABLE IF EXISTS betting;
                        
CREATE TABLE IF NOT EXISTS betting (
    account_id INT(11), 
    game_id VARCHAR(10),
    checkin_time DATETIME,
    checkout_time DATETIME,
    bet INT(11),
    profit INT(11),
	device_type_id VARCHAR(10),    
    ip VARCHAR(125)
)  ENGINE=INNODB;

# import betting data
LOAD DATA INFILE '/var/lib/mysql-files/betting_register.csv' 
INTO TABLE betting
FIELDS TERMINATED BY ',' 
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;

# remove \r in betting table you
update betting SET ip = TRIM(TRAILING '\r' FROM ip);