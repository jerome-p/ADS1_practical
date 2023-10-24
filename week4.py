import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

BCS_share_price = pd.read_csv('./BCS_ann.csv')
BP_share_price = pd.read_csv('./BP_ann.csv')
TSCO_share_price = pd.read_csv('./TSCO_ann.csv')
VOD_share_price = pd.read_csv('./VOD_ann.csv')

plt.figure()

plt.subplot(2,2,1)
plt.hist(BCS_share_price['ann_return'], density=True, label='BCS')
plt.legend()

plt.subplot(2,2,2)
plt.hist(BP_share_price['ann_return'], density=True, label='BP')
plt.legend()

plt.subplot(2,2,3)
plt.hist(TSCO_share_price['ann_return'], density=True, label='TSCO')
plt.legend()

plt.subplot(2,2,4)
plt.hist(VOD_share_price['ann_return'], density=True, label='VOD')
plt.legend()

plt.savefig('Subplots_normalised_annual_returns.png')


plt.figure()

plt.hist(BP_share_price['ann_return'], density=True, alpha=0.8)
plt.hist(TSCO_share_price['ann_return'], density=True, alpha=0.7)
plt.savefig('Combined_histogram_BP_TSCO.png')


plt.figure()

plt.boxplot([BCS_share_price['ann_return'], BP_share_price['ann_return'],
             TSCO_share_price['ann_return'], VOD_share_price['ann_return']],
            labels = ['BCS','BP','TSCO','VOD'])

plt.savefig('Box_plots_all_4.png')




#3)

plt.figure()

mrk_capt = [33367,68765,20979,29741]
np_mrk_capt = np.array(mrk_capt)

plt.pie(mrk_capt, labels=['BCS','BP','TSCO','VOD'])

total_mrk_capt = 1814000

adjusted_mrk_capt = np_mrk_capt/total_mrk_capt

plt.figure()
plt.pie(adjusted_mrk_capt, labels=['BCS','BP','TSCO','VOD'], normalize=False)
plt.title("Market Capitalisations compared to total")

plt.figure()
plt.bar(['BCS','BP','TSCO','VOD'],mrk_capt)



