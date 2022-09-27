from brute_force import compute_cost, compute_profit, get_actions_objects_from_csv
import sys
import csv
from tqdm import tqdm
import time



start_time = time.time()
MAX_INVEST = 500


def main():

    #actions_list = get_actions_objects_from_csv("data/dataset1.csv")
    filename = "data/dataset1.csv"#
    actions_list = read_csv(filename)
    
  

def read_csv(filename):
   
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
    actions_list.sort(key=lambda action: action[2], reverse=False)
    max_inv = MAX_INVEST * 100   
    shares_total = len(actions_list)
    cost = []      
    profit = []    

    for action in actions_list:
        cost.append(action[1])
        profit.append(action[2])

    dp = [[0 for i in range(max_inv +1)] for i in range(shares_total + 1)] # Making the dp array

    for i in range(1, shares_total+1):  # taking first i elements
        for w in range(max_inv, 0, -1):  # starting from back,so that we also have data of
                                # previous computation when taking i-1 items
            if cost[i-1] <= w:
                # finding the maximum value
                dp[i][w] = max(profit[i-1] + dp[i-1][w-cost[i-1]], dp[i-1][w])
            else:
                dp[i][w] = dp[i-1][w]

      # returning the maximum value of knaps

    

if __name__ == "__main__":
    main()