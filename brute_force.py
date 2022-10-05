import csv
from itertools import combinations
import sys
from tqdm import tqdm
import time



begin_time = time.time()

def main():
    actions_list = get_actions_from_csv("data/action.csv")
    print(f"\nComputing {len(actions_list)} shares for {MAX_INVEST}€ :")

    best_combi = get_all_combi(actions_list)
    show_cost_profit(best_combi)


try:
    MAX_INVEST = float(sys.argv[1])
except IndexError:
    MAX_INVEST = 500


def get_actions_from_csv(file_name: str):
    """Returns a list of Action object - actions - from a csv file"""
    
    with open(file_name, newline="") as csv_File: 
        actions = []
        reader = csv.reader(csv_File, delimiter=",")
        for row in reader:
            actions.append((row[0], float(row[1]), float(row[2])))

        return actions



def get_all_combi(actions):
    """Set all possible combinations of shares
    Make sure it's within possible max investment
    Iterate and get best profits
    list of all imported shares data - actions - as param 
    returns the list of most profitable combination - best_combi
    """
    actions.sort(key=lambda action: action[2], reverse=True)
    profit = 0
    best_combi = []

    for i in tqdm(range(len(actions))):
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
    """Sum of current share combination prices
    list of current shares combination - combi - as param
    returns total cost 
    """
    costs = []
    for el in combi:
        costs.append(el[1])

    return sum(costs)


def compute_profit(combi):
    """Retrieves the sum of the profit of current share combination
    list of current shares combi - combi - as param
    returns total profit 
    """
    profits = []
    for el in combi:
        profits.append(el[1] * el[2] / 100)
        
    return sum(profits)


def show_cost_profit(best_combi):
    """Shows the results of best combination 
    takes most profitable shares combination list - best_combi - as param
    """
    print(f"\nMost profitable investment ({len(best_combi)} shares) :\n")
  

    for item in best_combi:
        print(f"{item[0]} | {item[1]} € | +{item[2]} %")
        
    print("\nInvestment cost: ", compute_cost(best_combi), "€")
    print("Profit after 2 years: +",compute_profit(best_combi), "€")
    print("\nTime taken :", time.time()- begin_time, "seconds")
    print("")
   


if __name__ == "__main__":
    main()