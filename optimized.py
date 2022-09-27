import sys
import csv
from tqdm import tqdm
import time



start_time = time.time()
MAX_INVEST = 500


def main():

    filename = "data/dataset1.csv"#
    actions_list = read_csv(filename)
    print(f"\nComputing {len(actions_list)} shares for {MAX_INVEST}€ :")
    show_cost_profit(knapSack(actions_list))
  

def read_csv(filename):
    """Import shares data from csv file
    check rows and filter out corrupted data 
    Then return list of shares data 
    """
    with open(filename) as csvfile:
        actions_file = csv.reader(csvfile, delimiter=',')

        actions_list = []

        for row in actions_file:
            if float(row[1]) <= 0 or float(row[2]) <= 0:
                pass
            else:
                action = (
                    row[0],
                    int(float(row[1])*100),
                    float(float(row[1]) * float(row[2]) / 100)
                )
                actions_list.append(action)

        return actions_list

    
def knapSack(actions_list):
    """Sort the actions_list
    Knapsack - Initialize the matrix  - k
    Retrieve the best combination of shares
    actions_list - list of shares - as parameter
    Returns the best possible combinations list
    """
    actions_list.sort(key=lambda action: action[2], reverse=False)
    max_inv = MAX_INVEST * 100   
    total_action = len(actions_list)
    cost = []      
    profit = []    

    for action in actions_list:
        cost.append(action[1])
        profit.append(action[2])

    # Finding the best value (profit)
    k = [[0 for x in range(max_inv +1)] for x in range(total_action + 1)] # Making the k array

    for i in tqdm(range(1, total_action+1)):  # taking first i elements
        for w in range(1, max_inv + 1):  
                                   # previous computation when taking i-1 items
            if cost[i-1] <= w:
                # finding the maximum value(profit)
                k[i][w] = max(profit[i-1] + k[i-1][w-cost[i-1]], k[i-1][w])
            else:
                k[i][w] = k[i-1][w]
     

    #  Getting actions combination from best value (profits)
    best_combi = []

    while max_inv >= 0 and total_action >= 0:

        if k[total_action][max_inv] == \
                k[total_action-1][max_inv - cost[total_action-1]] + profit[total_action-1]:

            best_combi.append(actions_list[total_action-1])
            max_inv -= cost[total_action-1]

        total_action -= 1

    return best_combi  # returning the maximum value (profit) combination of knaps


def show_cost_profit(best_combi):
    """Show best cost and prifit combinations result
    The list of most profitable shares combination - best_combi - as param
    """
    print(f"\nMost profitable investments ({len(best_combi)}  shares) :\n")

    cost = []
    profit = []

    for item in best_combi:
        print(f"{item[0]} | {item[1] / 100} € | +{item[2]} €")
        cost.append(item[1] / 100)
        profit.append(item[2])

    print("\nTotal cost : ", sum(cost), "€")
    print("Profit after 2 years : +", sum(profit), "€")
    print("\nTime taken : ", time.time() - start_time, "seconds\n")

if __name__ == "__main__":
    main()