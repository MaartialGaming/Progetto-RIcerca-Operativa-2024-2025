import os
import json
import numpy as np
import pandas as pd

instance_name = 'dummy_problem'

folder_path = os.path.join('.', 'data', f'{instance_name}')

f = open(os.path.join(folder_path, 'weights.json'), 'r')
weights = json.load(f)
f.close()

df = pd.read_csv(os.path.join(folder_path, 'service.csv'), sep = ',', header = None)
service = df.values

df = pd.read_csv(os.path.join(folder_path, 'distances.csv'), sep = ',', header = None)
distances = df.values

folder_path = os.path.join('.', 'results', f'{instance_name}')

df = pd.read_csv(os.path.join(folder_path, 'deposit_locations.csv'), sep = ',', header = None)
deposit_locations = df.values

df = pd.read_csv(os.path.join(folder_path, 'path.csv'), sep = ',', header = None)
path = df.values

(N_deposits, N_supermarkets) = service.shape

N_constructions = np.sum(deposit_locations)

N_missed_supermarkets = N_supermarkets - len(np.nonzero(np.matmul(deposit_locations, service))[0])

travel_length = np.sum(distances * path)

total_cost = N_constructions * weights['construction'] + N_missed_supermarkets * weights['missed_supermarket'] + travel_length * weights['travel']

print('\n-----------------------COSTS-----------------------')
print('\t\t\t\tQ.TY\t\tCOST')
print(f"DEPOSIT CONSTRUCTIONS\t\t{N_constructions}\tx\t{weights['construction']}")
print(f"MISSED SUPERMARKETS\t\t{N_missed_supermarkets}\tx\t{weights['missed_supermarket']}")
print(f"TRAVEL LENGTH\t\t\t{travel_length}\tx\t{weights['travel']}")
print('')
print(f'TOTAL\t\t\t\t{total_cost}')
print('---------------------------------------------------\n')