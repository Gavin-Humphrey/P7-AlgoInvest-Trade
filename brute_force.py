import csv
from dataclasses import dataclass 
from itertools import combinations
import sys
from prettytable import PrettyTable




def main():
    actions_list = get_actions_objects_from_csv("data/action.csv")
    print(f"\nComputing {len(actions_list)} shares for {MAX_INVEST}€ :")

    best_combi = get_all_combi(actions_list)
    show_cost_profit(best_combi)


try:
    MAX_INVEST = float(sys.argv[1])
except IndexError:
    MAX_INVEST = 500



def get_actions_objects_from_csv(file_name: str):
    """Return a list of Action object from a csv file"""
    actions = []
    with open(file_name, newline="") as csv_File:
        reader = csv.reader(csv_File, delimiter=",")
        for row in reader:
            actions.append((row[0], float(row[1]), float(row[2])))

    return actions



def get_all_combi(actions):
    """Set all possible combinations of shares
    Make sure it's within possible max investment
    Iterate and get best profits
    @param actions: list of all imported shares data
    @return: most profitable combination (list)
    """
    profit = 0
    best_combi = []

    for i in range(len(actions)):
        combis = combinations(actions, i+1)

        for combi in combis:
            total_cost = compute_cost(combi)

            if total_cost <= MAX_INVEST:
                total_profit = compute_profit(combi)

                if total_profit > profit:
                    profit = total_profit
                    best_combi = combi

    return best_combi


def compute_cost(combi):
    """Sum of current share combo prices
    @param combi: list of current shares combi
    @return: total cost (float)
    """
    costs = []
    for el in combi:
        costs.append(el[1])

    return sum(costs)


def compute_profit(combi):
    """Gets the sum of the profit of current share combi
    @param combo: list of current shares combi
    @return: total profit (float)
    """
    profits = []
    for el in combi:
        profits.append(el[1] * el[2] / 100)

    return sum(profits)


def show_cost_profit(best_combi):
    """Display best combination results
    @param best_combi: most profitable shares combination (list)
    """
    print(f"\nMost profitable investment ({len(best_combi)} shares) :\n")
    print("Action # | Cost €| Profit %")
    print("__________________________")

    for item in best_combi:
        print(f"{item[0]} | {item[1]} € | +{item[2]} %")
        # x = PrettyTable()

        # x.field_names = [f"{item[0]} |  {item[1]} € | +{item[2]} %"]
        # print(x)

    print("\nInvestment cost: ", compute_cost(best_combi), "€")
    print("Profit after 2 years: +",compute_profit(best_combi), "€")
    print("")
   


if __name__ == "__main__":
    main()