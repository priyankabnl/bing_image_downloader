import os
import sys
import pandas as pd

from pathlib import Path
import shutil
path = os.path.join('C:'+os.sep,'Users','PBansal','OneDrive - Consolidated Electrical Distributors, Inc','Desktop','CED.xlsx')
data = pd.read_excel(path)
print(data.head())




