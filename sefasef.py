import pandas as pd

my_fruits_pieces = pd.DataFrame({
    'fruit': ['apple', 'banana', 'orange'],
    'pieces': [3, 2]
})
my_fruits_prices = pd.DataFrame({
    'fruit': ['apple', 'banana', 'orange'],
    'price': [20, 10, 50],})

#my_fruits_merged = pd.merge(my_fruits_pieces, my_fruits_prices, on='fruit', na_values=0)
my_fruits_concat= pd.concat([my_fruits_pieces, my_fruits_prices], axis=1,sort=False).reset_index()

#print(my_fruits_merged)
print(my_fruits_concat)