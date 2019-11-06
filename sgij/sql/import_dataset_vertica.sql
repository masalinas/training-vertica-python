# create game schema
CREATE SCHEMA IF NOT EXISTS VMart.game

# create gamer table
DROP TABLE IF EXISTS game.player;

# create player player
CREATE TABLE gaming.player (
    operator_id INT,
    player_id INT,
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
    deposit_limit_day INT,
    deposit_limit_month INT,
    deposit_limit_year INT,
    vsvdi_status VARCHAR(10),
    vsvdi_date DATE,
    vdocumental_status VARCHAR(10),
    vdocumental_date DATE
);

ALTER TABLE gaming.player ADD CONSTRAINT C_PRIMARY_PLAYER PRIMARY KEY (operator_id, player_id) DISABLED;

# import player data 
COPY gaming.player FROM '/home/dbadmin/Sources/Vertica/Scripts/Dataset/player_register.csv' PARSER fcsvparser();

# create account table
DROP TABLE IF EXISTS gaming.account;
                                        
CREATE TABLE IF NOT EXISTS gaming.account (
    account_id INT, 
    operator_id INT, 
    player_id INT,
    checkin_time DATETIME,
    checkout_time DATETIME,
    last_visit DATETIME,
    init_token INT,
    deposit INT,
    profit INT,
    withdrawal INT,
    final_token INT,
    player_skill FLOAT,
    bettings INT
);

ALTER TABLE gaming.account ADD CONSTRAINT C_PRIMARY_ACCOUNT PRIMARY KEY (account_id) DISABLED;

# import account data 
COPY gaming.account FROM '/home/dbadmin/Sources/Vertica/Scripts/Dataset/account_register.csv' PARSER fcsvparser();

# create betting table
DROP TABLE IF EXISTS gaming.betting;
                        
CREATE TABLE IF NOT EXISTS gaming.betting (
    account_id INT, 
    game_id VARCHAR(10),
    checkin_time DATETIME,
    checkout_time DATETIME,
    bet INT,
    profit INT,
   device_type_id VARCHAR(10),    
    ip VARCHAR(125)
);

# import betting data 
COPY gaming.betting FROM '/home/dbadmin/Sources/Vertica/Scripts/Dataset/betting_register.csv' PARSER fcsvparser();