import pandas as pd
import datatransform as dt
import os

df_result = pd.read_csv(os.path.join(os.getcwd(),"data/result.csv"))
df_console = pd.read_csv(os.path.join(os.getcwd(),"data/consoles.csv"))

dt.remove_spaces(df_console)
dt.remove_spaces(df_result)

df_result = dt.cleaner(df_result)

df_final = df_result.set_index('console').join(df_console.set_index('console'))

df_ranked = pd.concat([dt.rankgame(df_final, 'top', 'console'),
dt.rankgame(df_final, 'worst', 'console' ),
dt.rankgame(df_final, 'top', 'company'),
dt.rankgame(df_final, 'worst', 'company'),
dt.rankgame(df_final, 'top', 'all'),
dt.rankgame(df_final, 'worst', 'all')
])

df_ranked = df_ranked[['name', 'company', 'metascore', 'userscore', 'totalscore', 'rankcategory', 'rank' ]]

df_ranked.to_csv(os.path.join(os.getcwd(),"OutputFiles/rankings.csv"))