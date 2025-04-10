import os
import json
import pandas as pd

class Instance():
    def __init__(self, folder_name):
        folder_path = os.path.join('.', 'data', f'{folder_name}')
        f = open(os.path.join(folder_path, 'weights.json'), 'r')
        self.weights = json.load(f)
        f.close()
        df = pd.read_csv(os.path.join(folder_path, 'service.csv'), sep = ',', header = None)
        self.service = df.values
        df = pd.read_csv(os.path.join(folder_path, 'distances.csv'), sep = ',', header = None)
        self.distances = df.values
        print(self.weights)
        print(self.service)
        print(self.distances)

if __name__ == '__main__':
    inst = Instance('dummy_problem')