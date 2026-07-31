

def exchange_money(budget, exchange_rate):

    exchanged_rate = budget/exchange_rate
    return exchanged_rate


print(exchange_money(127.5,1.2))

from math import ceil, floor


def get_value_of_bills(denomination, number_of_bills):
    money_returned = ceil(number_of_bills)*denomination
    return money_returned

print(get_value_of_bills(10000,128))

def get_number_of_bills(amount, denomination):
    """

    :param amount: float - the total starting value.
    :param denomination: int - the value of a single bill.
    :return: int - number of bills that can be obtained from the amount.
    """

    return floor(amount/denomination)

print(get_number_of_bills(127.5,5))

def get_leftover_of_bills(amount, denomination):
    """

    :param amount: float - the total starting value.
    :param denomination: int - the value of a single bill.
    :return: float - the amount that is "leftover", given the current denomination.
    """

    return (amount%denomination)
print (get_leftover_of_bills(127.5,20))


def exchangeable_value(budget, exchange_rate, spread, denomination):
    """
    Calculates the maximum exchangeable value in a given denomination.

    1. Calculate the actual rate by adding the spread percentage to the exchange_rate.
    2. Divide the budget by this actual rate to get the total raw value.
    3. Use floor division with denomination to find the maximum exchangeable whole amount.
    """

    # Calculate the actual exchange rate including the fee
    # Example: 1.20 + (10 / 100 * 1.20) = 1.32
    actual_rate = exchange_rate + (spread / 100 * exchange_rate)

    # Calculate the maximum possible amount of the new currency
    #127.25/1.32 = 96.40
    total_new_currency = budget / actual_rate

    # Calculate how many full denominations (bills) fit into that total
    #96.40 // 5 = 19 96.40//20 = 4
    number_of_bills = total_new_currency // denomination

    # Return the total value of those bills
    #5*19 = 95 4*20 = 80
    return int(number_of_bills * denomination)


# Example usage based on your parameters:
# budget = 127.25, rate = 1.20, spread = 10, denomination = 5
print(exchangeable_value(127.25, 1.20, 10, 20))
print(127.25//5)

# or -- after applying actual rate we get 96.40 from this exchange booth will give us the amount divisible by singlge bill unit (5 or 20)
# so one more solution is

def exchangeable_value(budget, exchange_rate, spread, denomination):

    actual_rate = exchange_rate + (spread / 100 * exchange_rate)
    total_new_currency = budget / actual_rate
    exchanged_amount = total_new_currency - (total_new_currency%denomination)
    return int(exchanged_amount)

print(exchangeable_value(127.25, 1.20, 10, 20))





