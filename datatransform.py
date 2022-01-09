import pandas as pd

def remove_spaces(df):
    """
    remove white spaces from console column to make the join
    """
    df["console"] = df["console"].str.strip()

def cleaner(df):
    """
    some clean and validation steps for the input dataframe
    """
    df.drop(columns="date", inplace = True)
    
    df = df.dropna(subset=['name'])
    df['userscore'] = pd.to_numeric(df['userscore'], errors='coerce')
    df['metascore'] = pd.to_numeric(df['metascore'], errors='coerce')
    df = df[(df.metascore >= 0) & (df.metascore <= 100) & (df.userscore >= 0) & (df.userscore <= 10)]
    
    return df

def rankgame(df, type, column):
    """
    add totalscore column to calculate rank by metascore and userscore, then return de 10 rows for the especified rank type (top or worst) and column (console or company)
    """
    df["totalscore"] = df["metascore"] + df["userscore"]
    if column == 'all':
        df_rankgame = df.sort_values(by=['totalscore'], ascending=(type == 'worst')).head(10)
        df_rankgame['rank'] = df_rankgame.totalscore.rank(method='first', ascending=type == 'worst')
    else:
        df_rankgame = df.sort_values(by=[column, 'totalscore'], ascending=(type == 'worst')).groupby(column).head(10)
        df_rankgame['rank'] = df_rankgame.groupby(column).cumcount()+1
    df_rankgame['rankcategory'] = type+"10"+column
    return df_rankgame