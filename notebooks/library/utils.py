#function to get the unique values for each featur

import matplotlib.pyplot as plt
import seaborn as sns

def get_summary(df,features):
  for entry in features:
      print('Summary for: "' + entry + '"')
      output = pd.DataFrame({'count':df[entry].value_counts()})
      output['%'] = round(100* (output['count']/len(df[entry])),2)
      print(output)
      print('\n')
      sns.catplot(x=entry,data=df,kind="count")
      #plt.xticks(rotation=90)
      plt.show();
      print('________________________________________________________________________________________________________')


# function to calculate VIF
def calculate_vif(data):
    vif_df = pd.DataFrame(columns = ['Var', 'Vif'])
    x_var_names = data.columns
    for i in range(0, x_var_names.shape[0]):
        y = data[x_var_names[i]]
        x = data[x_var_names.drop([x_var_names[i]])]
        r_squared = sm.OLS(y,x).fit().rsquared
        vif = round(1/(1-r_squared),2)
        vif_df.loc[i] = [x_var_names[i], vif]
    return vif_df.sort_values(by = 'Vif', axis = 0, ascending=False, inplace=False)