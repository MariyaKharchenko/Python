# Возьмите задачу о банкомате из семинара 2.
# Разбейте её на отдельные операции — функции.
# Дополнительно сохраняйте все операции поступления и снятия средств в список.

import decimal

CMD_DEPOSIT = 'd'
CMD_WITHDRAW = 'w'
CMD_EXIT = 'e'
CMD_HISTORY = 'h'
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
operations = []


def operation(command: str, amount: decimal) -> list[str, decimal]:
    """
    Эта функция возвращает список, состоящий из команды(действия) и суммы.
    """
    lst = []
    if command == CMD_DEPOSIT:
        command = 'пополнение'
    elif command == CMD_WITHDRAW:
        command = 'снятие'
        amount *= -1
    lst.append(command)
    lst.append(amount)
    return lst


def withdraw(amount, withdraw_tax, account, count):
    """
   Эта функция уменьшает баланс электронного кошелька
   на amount и комиссию, а также двигает count вперед.
    """
    count += 1
    account -= (amount + withdraw_tax)
    return (account, count)


def tax(amount, wp=WITHDRAW_PERCENT, min_r=MIN_REMOVAL, max_r=MAX_REMOVAL):
    """
     Эта функция рассчитывает сумму комиссии за снятие.
    """
    withdraw_tax = amount * wp
    withdraw_tax = (min_r if withdraw_tax < min_r else
                    max_r if withdraw_tax > max_r else withdraw_tax)
    return withdraw_tax


def depozit(account: decimal, amount: int, count: int):
    """
   Эта функция увеличивает баланс электронного кошелька
   на amount, а также двигает count вперед.
    """
    account += amount
    count += 1
    return (account, count)


while True:
    command = input(f'Пополнить - "{CMD_DEPOSIT}", '
                    f'Снять - "{CMD_WITHDRAW}"'
                    f', Выйти - "{CMD_EXIT}", История операций - "{CMD_HISTORY}": ')
    if command == CMD_EXIT:
        print(f'Возьмите карту на которой {account:.2f} у.е.')
        break
    if account > RICHNESS_SUM:
        percent = account * RICHNESS_TAX
        account -= percent
        print(f'Удержан нолог на богатство {RICHNESS_TAX} '
              f'в размере {percent:.2f} у.е. \n'
              f'Остаток на карте {account:.2f} у.е.')
    if command in (CMD_DEPOSIT, CMD_WITHDRAW):
        amount = 1
        while amount % 50 != 0:
            amount = int(input(f'Введите сумму, кратную {MULTiPLICITY} '))
    if command == CMD_DEPOSIT:
        account, count = depozit(account, amount, count)
        operations.append(operation(command, amount))
        print(f'Пополнение карты на сумму {amount:.2f} у.е. \n '
              f'Итого на карте {account:.2f} у.е.')
    elif command == CMD_WITHDRAW:
        withdraw_tax = tax(amount)
        if amount + withdraw_tax <= account:
            account, count = withdraw(amount, withdraw_tax, account, count)
            operations.append(operation(command, amount))
            print(f'Снятие с карты {amount:.2f} у.е. \n'
                  f'Комиссия за снятие {withdraw_tax:.2f} у.е.\n'
                  f'На карте осталось {account:.2f} у.е.')
        else:
            print(f'Недостаточно средств.\n'
                  f' На карте {account:.2f} у.е.')
    elif command == CMD_HISTORY:
        if len(operations) > 0:
            print(f'Были совершены следующие операции: {operations}')
        else:
            print('Операций еще не было.')
    if count % COUNT_OPER == 0 and count != 0:
        bonus = account * ADD_PERCENT
        account += bonus
        print(f'На счет начислено {ADD_PERCENT*100}%, '
              f'составляющие {bonus:.2f} у.е. \n'
              f'Итого на карте {account:.2f} у.е.')





