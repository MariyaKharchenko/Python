import  decimal

CMD_DEPOSIT = 'd'
CMD_WITHDRAW = 'w'
CMD_EXIT = 'e'
RICHNESS_SUM = decimal.Decimal(5_000_000)
RICHNESS_TAX = decimal.Decimal(10) / decimal.Decimal(100)
WITHDRAW_PERCENT = decimal.Decimal(15) / decimal.Decimal(1000)
ADD_PERCENT = decimal.Decimal(3) / decimal.Decimal(100)
MULTiPLICITY = 50
MIN_REMOVAL = 30
MAX_REMOVAL = 600
COUNT_OPER = 3

account = decimal.Decimal(0)
count = 0

while True:
    command = input(f'Пополнить - "{CMD_DEPOSIT}", Снять - "{CMD_WITHDRAW}", Выйти - "{CMD_EXIT}": ')
    if command == CMD_EXIT:
        print(f'Возьмите карту на которой {account:.2f} у.е.')
        break
    if account > RICHNESS_SUM:
        percent = account * RICHNESS_TAX
        account -= percent
        print(f'Удержан нолог на богатство {RICHNESS_TAX} в размере {percent:.2f} у.е. \n'
              f'Остаток на карте {account:.2f} у.е.')
    if command in (CMD_DEPOSIT, CMD_WITHDRAW):
        amount = 1
        while amount % 50 != 0:
            amount = int(input(f'Введите сумму, кратную {MULTiPLICITY} '))
    if command == CMD_DEPOSIT:
        account += amount
        count += 1
        print(f'Пополнение карты на сумму {amount:.2f} у.е. \n'
              f'Итого на карте {account:.2f} у.е.')
    elif command == CMD_WITHDRAW:
        withdraw_tax = amount * WITHDRAW_PERCENT
        withdraw_tax = (MIN_REMOVAL if withdraw_tax < MIN_REMOVAL else
                        MAX_REMOVAL if withdraw_tax > MAX_REMOVAL else withdraw_tax)
        if amount + withdraw_tax <= account:
            count += 1
            account -= (amount + withdraw_tax)
            print(f'Снятие с карты {amount:.2f} у.е. \n'
                  f'Комиссия за снятие {withdraw_tax:.2f} у.е.\n'
                  f'На карте осталось {account:.2f} у.е.')
        else:
            print(f'Недостаточно средств.\n'
                  f' На карте {account:.2f} у.е.')
    if count % COUNT_OPER == 0 and count != 0:
        bonus = account * ADD_PERCENT
        account += bonus
        print(f'На счет начислено {ADD_PERCENT*100}%, составляющие {bonus:.2f} у.е. \n'
              f'Итого на карте {account:.2f} у.е.')




