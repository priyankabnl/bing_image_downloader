import os
import sys
import pandas as pd
from downloader import download
from bing import Bing
from pathlib import Path
import shutil
path = os.path.join('C:'+os.sep,'Users','PBansal','OneDrive - Consolidated Electrical Distributors, Inc','Desktop','CED Clients','X-Items','images.xlsx')
data = pd.read_excel(path)
print(data.head())

if __name__ == '__main__':
    for index, row in data.iterrows():
        download(str(row['UPC']), limit=5, output_dir=str(row['UPC']), adult_filter_off=True,
                 force_replace=False, timeout=120, verbose=True)

