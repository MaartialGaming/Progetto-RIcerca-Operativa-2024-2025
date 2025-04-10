import os
import pandas as pd

class Solution():
    def __init__(self, X, Y):
        self.X = X
        self.Y = Y
    
    def write(self, folder_name):
        folder_path = os.path.join('.', 'results', f'{folder_name}')
        os.makedirs(folder_path, exist_ok = True)
        # np.savetxt(os.path.join(folder_path, 'deposit_locations.csv'), self.X, delimiter = ',', newline = ',', fmt='%d')
        # f = open(os.path.join(folder_path, 'deposit_locations.csv'), 'w+')
        # f.write(str(self.X))
        # f.close()
        df = pd.DataFrame(self.X)
        df.T.to_csv(os.path.join(folder_path, 'deposit_locations.csv'), header = False, index = False)
        df = pd.DataFrame(self.Y)
        df.to_csv(os.path.join(folder_path, 'path.csv'), header = False, index = False)