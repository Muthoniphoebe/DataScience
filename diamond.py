import seaborn as sns
diamonds = sns.load_dataset('diamonds')

print(diamonds.to_string())
print('This is what we have:')
print(diamonds.info()) 
print(diamonds.size) 
print(diamonds.shape) 
print('This is the decription of the dataset:')
print(diamonds.describe()) 
print(diamonds.isnull().sum())
import matplotlib as plt
