import json

with open('Lesson5_7_data.txt', 'r') as fr:
    firm_list = {}
    profit_list = {}
    total_profit = 0
    count_of_profit_firms = 0

    while True:
        line = fr.readline().strip().split()
        if not line:
            break
        profit = float(line[2]) - float(line[3])
        if profit > 0:
            total_profit += profit
            count_of_profit_firms += 1

        firm_list[line[0]] = profit

    profit_list['average_profit'] = total_profit/count_of_profit_firms

    with open('Lesson5_7_data.json', 'w') as jw:
        json.dump(firm_list, jw, indent=4)
        json.dump(profit_list, jw, indent=4)