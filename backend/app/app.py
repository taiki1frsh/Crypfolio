from pycoingecko import CoinGeckoAPI
import matplotlib.pyplot as plt
import numpy as np
import time
from datetime import datetime
import sys
sys.path.append() # enter the path of draw_func folder on your own
from circle import circle
from line_time import line_time

cg = CoinGeckoAPI()
#since the rule of coingecko's API, have to name project name instead of symbol.

class Crypto_folio():
    def __init__(self, portfolio, labels):
        self.portfolio = portfolio
        self.labels = labels

    def arange_total_asset(self, principal, portfolio):
        start = time.time()
        total_asset = 0
       
        my_cryptos = {}
        num_for_pie = []
        # arrange form of total assset
        for i in portfolio:
            each_price = cg.get_price(ids=i, vs_currencies='jpy')
            each_money = int(each_price[i]['jpy']*portfolio[i])
            that_money = "¥{:,d}".format(each_money)
            total_asset += each_money
            my_cryptos[f'{portfolio[i]}{i}'] = that_money
            num_for_pie.append(each_money)
        print(my_cryptos)

        num_for_pie = sorted(num_for_pie, reverse=True)
        
        # growth rate
        growth_rate = (int(total_asset)/principal)*100 - 100
        growth_rate = round(growth_rate, 1)
        total_asset = "¥{:,d}".format(int(total_asset))
        print(f'\nMy total asset : {total_asset}\nGrowth rate : {growth_rate}%')
        end = time.time()
        print(end - start)

        return growth_rate, num_for_pie, total_asset

def main():
    # define your portfolio + labels (from high to low about your proportion)
    """ examples
    my_portfolio = {'bitcoin': 1, 'ethereum' : 1}
    labels = ['BTC', 'ETH']
    """

    mine = Crypto_folio() # portfolio, labels
    my_growth_rate, num_for_pie, total_outcome = mine.arange_total_asset() # principal, portfolio
    fig1 = circle(my_growth_rate, num_for_pie, mine.labels, total_outcome)

    fig_line = line_time() # portfolio, 
    plt.show()

    
if __name__ == '__main__':
    main()
