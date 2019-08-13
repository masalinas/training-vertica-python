# -*- coding: utf-8 -*-
"""
Created on Sat Aug 10 15:23:18 2019

@description: Generate a virtual dataset for SGIJ Vertica Training in csv format
@author: Miguel Salinas Gancedo
@email: miguel@thingtrack.com
"""

import math
import random
from datetime import datetime
from datetime import timedelta
from faker import Faker
from faker.providers import internet
import pycountry
import csv

# faker localized providers ISO codes supported
faker_lang_iso_codes = ['ar_EG',
                        'ar_PS',
                        'ar_SA',
                        'bg_BG',
                        'bs_BA',
                        'cs_CZ',
                        'de_DE',
                        'dk_DK',
                        'el_GR',
                        'en_AU',
                        'en_CA',
                        'en_GB',
                        'en_NZ',
                        'en_US',
                        'es_ES',
                        'es_MX',
                        'et_EE',
                        'fa_IR',
                        'fi_FI',
                        'fr_FR',
                        'hi_IN',
                        'hr_HR',
                        'hu_HU',
                        'hy_AM',
                        'it_IT',
                        'ja_JP',
                        'ka_GE',
                        'ko_KR',
                        'lt_LT',
                        'lv_LV',
                        'ne_NP',
                        'nl_NL',
                        'no_NO',
                        'pl_PL',
                        'pt_BR',
                        'pt_PT',
                        'ro_RO',
                        'ru_RU',
                        'sl_SI',
                        'sv_SE',
                        'tr_TR',
                        'uk_UA',
                        'zh_CN',
                        'zh_TW']
                                      
# random gender function
def gender(): 
    return 'M' if random.randint(0,1) == 0 else 'F'

# random country function
def country_code(): 
    return random.choice(['AF',
                          'AX',
                          'AL',
                          'DZ',
                          'AS',
                          'AD',
                          'AO',
                          'AI',
                          'AQ',
                          'AG',
                          'AR',
                          'AM',
                          'AN',
                          'AW',
                          'AU',
                          'AT',
                          'AZ',
                          'BS',
                          'BH',
                          'BD',
                          'BB',
                          'BY',
                          'BE',
                          'BZ',
                          'BJ',
                          'BM',
                          'BT',
                          'BO',
                          'BQ',
                          'BA',
                          'BW',
                          'BV',
                          'BR',
                          'IO',
                          'BN',
                          'BG',
                          'BF',
                          'BI',
                          'KH',
                          'CM',
                          'CA',
                          'CV',
                          'KY',
                          'CF',
                          'TD',
                          'CL',
                          'CN',
                          'CX',
                          'CC',
                          'CO',
                          'KM',
                          'CG',
                          'CD',
                          'CK',
                          'CR',
                          'CI',
                          'HR',
                          'CU',
                          'CW',
                          'CY',
                          'CZ',
                          'DK',
                          'DJ',
                          'DM',
                          'DO',
                          'EC',
                          'EG',
                          'SV',
                          'GQ',
                          'ER',
                          'EE',
                          'ET',
                          'FK',
                          'FO',
                          'FJ',
                          'FI',
                          'FR',
                          'GF',
                          'PF',
                          'TF',
                          'GA',
                          'GM',
                          'GE',
                          'DE',
                          'GH',
                          'GI',
                          'GR',
                          'GL',
                          'GD',
                          'GP',
                          'GU',
                          'GT',
                          'GG',
                          'GN',
                          'GW',
                          'GY',
                          'HT',
                          'HM',
                          'VA',
                          'HN',
                          'HK',
                          'HU',
                          'IS',
                          'IN',
                          'ID',
                          'IR',
                          'IQ',
                          'IE',
                          'IM',
                          'IL',
                          'IT',
                          'JM',
                          'JP',
                          'JE',
                          'JO',
                          'KZ',
                          'KE',
                          'KI',
                          'KP',
                          'KR',
                          'KW',
                          'KG',
                          'LA',
                          'LV',
                          'LB',
                          'LS',
                          'LR',
                          'LY',
                          'LI',
                          'LT',
                          'LU',
                          'MO',
                          'MK',
                          'MG',
                          'MW',
                          'MY',
                          'MV',
                          'ML',
                          'MT',
                          'MH',
                          'MQ',
                          'MR',
                          'MU',
                          'YT',
                          'MX',
                          'FM',
                          'MD',
                          'MC',
                          'MN',
                          'ME',
                          'MS',
                          'MA',
                          'MZ',
                          'MM',
                          'NA',
                          'NR',
                          'NP',
                          'NL',
                          'NC',
                          'NZ',
                          'NI',
                          'NE',
                          'NG',
                          'NU',
                          'NF',
                          'MP',
                          'NO',
                          'OM',
                          'PK',
                          'PW',
                          'PS',
                          'PA',
                          'PG',
                          'PY',
                          'PE',
                          'PH',
                          'PN',
                          'PL',
                          'PT',
                          'PR',
                          'QA',
                          'RE',
                          'RO',
                          'RU',
                          'RW',
                          'BL',
                          'SH',
                          'KN',
                          'LC',
                          'MF',
                          'PM',
                          'VC',
                          'WS',
                          'SM',
                          'ST',
                          'SA',
                          'SN',
                          'RS',
                          'SC',
                          'SL',
                          'SG',
                          'SX',
                          'SK',
                          'SI',
                          'SB',
                          'SO',
                          'ZA',
                          'GS',
                          'SS',
                          'ES',
                          'LK',
                          'SD',
                          'SR',
                          'SJ',
                          'SZ',
                          'SE',
                          'CH',
                          'SY',
                          'TW',
                          'TJ',
                          'TZ',
                          'TH',
                          'TL',
                          'TG',
                          'TK',
                          'TO',
                          'TT',
                          'TN',
                          'TR',
                          'TM',
                          'TC',
                          'TV',
                          'UG',
                          'UA',
                          'AE',
                          'GB',
                          'US',
                          'UM',
                          'UY',
                          'UZ',
                          'VU',
                          'VE',
                          'VN',
                          'VG',
                          'VI',
                          'WF',
                          'EH',
                          'YE',
                          'ZM',
                          'ZW'])  
                                       
# random game type function
def game_type(): 
    return random.choice(['ADC', 
                          'AHC', 
                          'ADX', 
                          'ADM',
                          'AHM',
                          'AHX',
                          'AOC',
                          'AOX',
                          'POC',
                          'POT',
                          'AZA',
                          'BLJ',
                          'BNG',
                          'PUN',
                          'RLT',
                          'COC',
                          'COM',
                          'PDM',
                          'PHM',
                          'PLN',
                          'PLP',
                          'PEU',
                          'PBL',
                          'PGP',
                          'PLT',
                          'OLN',
                          'OLP',
                          'OEU',
                          'OBL',
                          'OGP',
                          'OLT'])
                                   
# random payment method function
def payment_method_type(): 
    return random.choice(['1',
                          '2',
                          '3',
                          '4',
                          '5',
                          '6',
                          '7',
                          '8',
                          '9',
                          '10',
                          '11',
                          '12',
                          '13',
                          '14',
                          '15',
                          '16',
                          '17',
                          '18',
                          '19',
                          '20',
                          '99'])    
                                             
# random CNJ status function
def CNJ_status(): 
    return random.choice(['A',
                         'PV',
                         'S',
                         'C',
                         'SC',
                         'AC',
                         'PR',
                         'AE',
                         'O',])  

# random document type function
def document_type(): 
    return random.choice(['ID',
                          'SS',
                          'PA',
                          'DL',
                          'OT'])

# random device type function
def device_type(): 
    return random.choice(['MO',
                          'PC',
                          'TB',
                          'TF',
                          'OT'])
                                       
# random region fiscal function
def fiscal_region(): 
    return random.choice(['01',
                          '02',
                          '03',
                          '04',
                          '05',
                          '06',
                          '07',
                          '08',
                          '09',
                          '10',
                          '11',
                          '12',
                          '13',
                          '14',
                          '15',
                          '16',
                          '17',
                          '18',
                          '19',
                          '20',
                          '21',
                          '22'])                                                

# random Deposit limit function
def deposit_limit(): 
    return random.choice(['600',
                          '1500',
                          '3000',
                          '-1']) 

# random VSVDI Status function
def vsvdi_status():  
    return random.choice(['S',
                          'N']) 

# random VDocumental Status function
def vdocumental_status():  
    return random.choice(['S',
                          'N'])                      


def get_skillup_coef(x):
    return round(1000000000 / ((9-x) ** 4))

def roundup(x):
    return int(math.ceil(x / 10.0)) * 10

# generate a date intervals for a betting account holder in a period of time
def betting_date_intervals(checkin_time, checkout_time, rounds): 
    interval = [] 

    t_in = datetime.strptime(checkin_time, '%Y-%m-%d %H:%M')    
    t_out = datetime.strptime(checkout_time, '%Y-%m-%d %H:%M') 
    
    # calculate total betting time spent in minutes
    total_round_time = (t_out - t_in).total_seconds() / 60
    
    # calculate a random sorted checkout datetime collection from total rounds
    for j in range(2*rounds - 2): 
        time_round = random.randint(0, total_round_time)
        checkout_round_time = t_in + timedelta(minutes=time_round)
        
        interval.append(checkout_round_time) 
  
    interval.sort()
        
    # convert datetime to string
    for j in range(len(interval)): 
        interval[j] = interval[j].strftime('%Y-%m-%d %H:%M')
    
    interval.insert(0, checkin_time)
    interval.append(checkout_time)
    
    interval = [tuple(interval[i:i+2]) for i in range(0, len(interval), 2)]
    
    return interval
    
# generate the player personal information register
def player_register():
    register = {}
    
    # generate random ISO country code
    cc = country_code()
    
    # if lang ISO country code is not supported get Spain code
    country_codes_supported = [s for s in faker_lang_iso_codes if cc in s]
    
    if len(country_codes_supported) == 0 :
        register['resident'] = 'S'
        cc = 'ES'
        lang_iso_code = 'es_ES'
    else:
        register['resident'] = 'N'
        lang_iso_code = country_codes_supported[0]
    
    # get country from ISO country code
    country = pycountry.countries.get(alpha_2=cc)

    fake = Faker(lang_iso_code)
    fake.add_provider(internet)

    # generate random gender
    sex = gender()

    # configure fake gender profile and generate random name, surname
    fake.profile(sex=sex)
     
    # create register
    register['first_name'] = fake.first_name()
    register['last_name_01'] = fake.last_name()
    register['last_name_02'] = fake.last_name()
    register['sex'] = sex
    register['birthdate'] = fake.date_between_dates(date_start=datetime(1970, 1, 1), date_end=datetime(2000, 1, 1)).strftime("%Y-%m-%d")
    register['document_type_id'] = document_type()
    register['identification_document'] = fake.credit_card_number(card_type=None)  
    register['email'] = fake.email()
    register['login'] = register['email'] 
    register['pseudonym'] = register['email'].split("@")[0] 
    register['resident'] = register['resident']
    register['address'] = fake.address()
    register['country'] = country.name
    register['telephone'] = fake.phone_number().replace(' ', '')
    fa = fake.date_between_dates(date_start=datetime(2010, 1, 1), date_end=datetime.now())
    register['activation_date'] = fa.strftime("%Y-%m-%d")
    register['fiscal_region'] = fiscal_region()
    register['game_id'] = game_type()
    register['payment_method_id'] = payment_method_type()
    register['device_type_id'] = device_type()
    register['ip'] = fake.ipv4_private()
    register['cnj_status'] = CNJ_status()
    register['deposit_limit_day'] = deposit_limit()
    register['deposit_limit_month'] = deposit_limit()
    register['deposit_limit_year'] = deposit_limit()
    
    register['vsvdi_status'] = vsvdi_status()
    register['vsvdi_date'] = (fa + timedelta(days=random.randint(1, 30))).strftime("%Y-%m-%d")
    
    register['vdocumental_status'] = vdocumental_status()
    register['vdocumental_date'] = (fa + timedelta(days=random.randint(1, 30))).strftime("%Y-%m-%d")
        
    return register

# generate the account-holder status register in a period of time   
def account_register(operator_id, player_id):
    register = {}
     
    host_skill = 10
    wins = 0
    loss = 0
    rounds = 0
    checkin_time = None
    checkout_time = None
    start_time = None
    
    if not any(register['operator_id'] == operator_id and 
               register['player_id'] == player_id for register in account_registers):
        start_time = datetime.now() + timedelta(minutes = random.randint(1, 400))
        checkin_time = start_time.strftime('%Y-%m-%d %H:%M')
        init_token = round(random.uniform(1, 10)) * 100
        player_skill = random.uniform(6 ,9)
        
        register['player_skill'] = player_skill
        register['init_token'] = init_token
        register['last_visit'] = start_time
    else:
        init_token = roundup(next(register['init_token'] for register in account_registers if register['operator_id'] == operator_id and register.get("player_id") == player_id) * random.uniform(0.7, 1.3)) 
        player_skill = next(register['player_skill'] for register in account_registers if register['operator_id'] == operator_id and register.get("player_id") == player_id)
        start_time = next(register['last_visit'] for register in account_registers if register['operator_id'] == operator_id and register.get("player_id") == player_id) + timedelta(days=random.randint(3,7))
        checkin_time = start_time.strftime('%Y-%m-%d %H:%M')
        register['last_visit'] = start_time
        
    token = init_token
     
    while token > 0 and rounds <= random.uniform(5, 10): # (min, max) total rounds
        host_luck = random.uniform(10, 20)
        player_luck = random.randint(8, 28)
        if host_skill * host_luck > player_skill * player_luck:
            bet = round(init_token * random.uniform(0.05, 0.1))
            if token >= bet:
                token -= bet   
            else: 
                token = 0
                checkout_time = (datetime.now()+ timedelta(hours=rounds/5)).strftime('%Y-%m-%d %H:%M')
            loss += 1 
            
        elif host_skill * host_luck < player_skill * player_luck:
            token += round(init_token * random.uniform(0.05, 0.1)) #win x% token in 1 round
            wins += 1

        skillup_coef = get_skillup_coef(player_skill)
        player_skill += math.sqrt(rounds/skillup_coef)
        rounds += 1
        
    checkout_time = (start_time + timedelta(hours=rounds/5)).strftime('%Y-%m-%d %H:%M')

    register['checkin_time'] = checkin_time
    register['checkout_time'] = checkout_time
    register['rounds'] = rounds
    register['init_token'] = init_token
    register['withdraw'] = token
    register['profit'] = token - init_token
    register['player_skill'] = player_skill
    register['wins'] = wins
    register['loss'] = loss

    return register

# generate the bettings events registers executed in a account-holder in a period of time
def betting_register(account_id):
    registers = []
    register = {}
    
    checkin_time = next(account_register['checkin_time'] for account_register in account_registers if account_register['account_id'] == account_id)
    checkout_time = next(account_register['checkout_time'] for account_register in account_registers if account_register['account_id'] == account_id)
    rounds = next(account_register['rounds'] for account_register in account_registers if account_register['account_id'] == account_id)        
    init_token = next(account_register['init_token'] for account_register in account_registers if account_register['account_id'] == account_id)    
    profit = next(account_register['profit'] for account_register in account_registers if account_register['account_id'] == account_id)    
    wins = next(account_register['wins'] for account_register in account_registers if account_register['account_id'] == account_id)
    loss = next(account_register['loss'] for account_register in account_registers if account_register['account_id'] == account_id)  
    
    intervals = betting_date_intervals(checkin_time, checkout_time, rounds)
    
    # intervals loop
    i = 0
    while i < len(intervals):
        #for i in range(len(intervals)):
        register['account_id'] = account_id
        register['game_id'] = game_type()
        register['checkin_time'] = intervals[i][0]
        register['checkout_time'] = intervals[i][1]
        register['ip'] = Faker().ipv4_private()
        
        # random win
        win = random.randint(0, 1)
        bet = 0;
        profit = 0;
        
        if win == 1 and wins > 0:
            bet = random.randint(1, init_token)
            profit = random.randint(1, init_token)
            
            #init_token = init_token + profit
            wins = wins - 1
            i = i + 1
            
            register['bet'] = bet
            register['profit'] = profit
        
            registers.append(register.copy())
        elif win == 0 and loss > 0:
            bet = random.randint(1, init_token)
            profit = random.randint(1, init_token) * -1
            
            #init_token = init_token + profit
            loss = loss - 1
            i = i + 1
            
            register['bet'] = bet
            register['profit'] = profit
        
            registers.append(register.copy())
        
    return registers
        
# INPUT01: players per operator input
OPERATORS = [200, 500, 300]          
#OPERATORS = [2]          

# INPUT02: number of rounds per player
ROUNDS = 3

# SGIJ register collections                   
player_registers = []
account_registers = []
betting_registers = []

# initialize account identifier
account_id = 1

# generate SGIJ registers from OPERATORS
for operator_id in range(0, len(OPERATORS)):                       
    for player_id in range(0, OPERATORS[operator_id]):
        register = player_register()
        register['operator_id'] = operator_id + 1
        register['player_id'] = player_id + 1
        
        player_registers.append(register)
        
        # generate account player registers from ROUNDS 
        for r in range(ROUNDS):
            register = account_register(operator_id + 1, player_id + 1)
            register['account_id'] = account_id
            register['operator_id'] = operator_id + 1
            register['player_id'] = player_id + 1
         
            account_registers.append(register)
            
            # generate gampling player registers from each round
            betting_registers.extend(betting_register(account_id))
            
            account_id = account_id + 1
            
# export DGIJ registers collection to csv file
csv_columns_player_register = ['operator_id',
                               'player_id',
                               'first_name', 
                               'last_name_01', 
                               'last_name_02', 
                               'sex', 
                               'birthdate', 
                               'document_type_id', 
                               'identification_document', 
                               'email', 
                               'login', 
                               'pseudonym', 
                               'resident', 
                               'address',
                               'country',
                               'telephone',
                               'activation_date',
                               'fiscal_region',
                               'game_id',
                               'payment_method_id',
                               'device_type_id',
                               'ip',
                               'cnj_status',
                               'deposit_limit_day',
                               'deposit_limit_month',
                               'deposit_limit_year',
                               'vsvdi_status',
                               'vsvdi_date',
                               'vdocumental_status',
                               'vdocumental_date']
try:
    with open('./csv/player_register.csv', 'w') as csvFile:
        writer = csv.DictWriter(csvFile, fieldnames=csv_columns_player_register)
        writer.writeheader()
        
        for player_register in player_registers:
            writer.writerow(player_register)
        
    csvFile.close()
except IOError:
    print("I/O Player Dataset CSV file error.")

print('STEP01: Player Dataset CSV file generated correctly ...')

csv_columns_account_register = ['account_id',
                                'operator_id',
                                'player_id',
                                'checkin_time',
                                'checkout_time', 
                                'last_visit',                                                                                              
                                'init_token',  
                                'profit',                                 
                                'withdraw', 
                                'player_skill',
                                'rounds',                                  
                                'wins', 
                                'loss']
try:    
    with open('./csv/account_register.csv', 'w') as csvFile:
        writer = csv.DictWriter(csvFile, fieldnames=csv_columns_account_register)
        writer.writeheader()
        
        for account_register in account_registers:
            writer.writerow(account_register)
        
    csvFile.close()
except IOError:
    print("I/O Account Dataset CSV file error")

print('STEP02: Account Dataset CSV file generated correctly ...')

csv_columns_betting_register = ['account_id',
                                'game_id',
                                'checkin_time',
                                'checkout_time', 
                                'bet',
                                'profit',
                                'ip']
try:    
    with open('./csv/betting_register.csv', 'w') as csvFile:
        writer = csv.DictWriter(csvFile, fieldnames=csv_columns_betting_register)
        writer.writeheader()
        
        for betting_register in betting_registers:
            writer.writerow(betting_register)
        
    csvFile.close()
except IOError:
    print("I/O Betting Dataset CSV file error")

print('STEP03: Betting Dataset CSV file generated correctly ...')

print()    
print('Virtual Dataset CSV files generated correctly ...')