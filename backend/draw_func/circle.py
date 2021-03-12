import matplotlib.pyplot as plt
import numpy as np

def circle(growth_rate, num_list, labels, total_outcome):
    fig_circle, ax = plt.subplots(figsize=(6, 3), subplot_kw=dict(aspect="equal"))

    def func(pct, allvals):
        absolute = int(pct/100.*np.sum(allvals))
        return "{:.1f}%\n(¥{:,d}jpy)".format(pct, absolute)

    wedges, texts, autotexts = ax.pie(num_list, wedgeprops=dict(width=0.7),            
        autopct=lambda pct: func(pct, num_list),
        textprops=dict(color="w"))

    bbox_props = dict(boxstyle="square,pad=0.3", fc="w", ec="k", lw=0.72)
    kw = dict(arrowprops=dict(arrowstyle="-"),
      bbox=bbox_props, zorder=0, va="center")

    for i, p in enumerate(wedges):
        ang = (p.theta2 - p.theta1)/2 + p.theta1
        y = np.sin(np.deg2rad(ang))
        x = np.cos(np.deg2rad(ang))
        horizontalalignment = {-1: "right", 1: "left"}[int(np.sign(x))]
        connectionstyle = "angle,angleA=0,angleB={}".format(ang)
        kw["arrowprops"].update({"connectionstyle": connectionstyle})      
        ax.annotate(labels[i], xy=(x, y), xytext=(1.4*np.sign(x), 1.4*y),
           horizontalalignment=horizontalalignment, **kw)

    plt.setp(autotexts, size=8, weight="bold")
    ax.set_title(f"Proportion of assets\n Growth rate so far : {growth_rate}% from total outcome: {total_outcome}")

    return fig_circle

""" if __name__=='__main__':
    circle() """
