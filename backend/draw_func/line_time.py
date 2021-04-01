import matplotlib.pyplot as plt
from datetime import datetime
from pycoingecko import CoinGeckoAPI
cg = CoinGeckoAPI()

def line_time(portfolio, year, month, date):
    # prepare the time related variables
    now = datetime.now()
    now_ts = now.timestamp()
    start = datetime(year, month, date)
    start_ts = start.timestamp()
    each_pri_time = []
    each_datetimes = []
    total_pri = []
    total_prices = []
    amount = []

    for j in portfolio:
        history = cg.get_coin_market_chart_range_by_id(id=j, vs_currency='jpy',
          from_timestamp=str(start_ts), to_timestamp=str(now_ts))
        each_pri_time = history['prices']
        total_pri.append(each_pri_time)
        num_time = len(history['prices'])
        amount.append(portfolio[j])

    for k in range(num_time-1):
        total_price = 0
        for s in range(len(portfolio)):
            if k == 781 & s== 3:
                continue
            total_price += (total_pri[s][k][1]*amount[s])
        total_prices.append(total_price)
        each_datetimes.append(datetime.fromtimestamp((each_pri_time[k][0]/1000)))

    fig_line, ax = plt.subplots(nrows=1, ncols=1)
    ax.plot(each_datetimes[:num_time], total_prices)
    ax.set_xlabel('Total worth', fontsize=15)
    ax.set_ylabel('Date', fontsize=15)
    ax.set_title("Transition of the worth")
    
    return fig_line

if __name__=='__main__':
    print("fine line")