def print_most_profitable_item2():
    y = sales.groupby(['Trade Name'],as_index=True).sum()
    x = y.sort_values(['Profit'], ascending = False)
    w = x.iloc[0].to_frame()
    print(w)
