import os
import pandas as pd
from sqlalchemy import column, false, true
import csv

csv_name = 'define your fine name here'

class DownStreamAutomateCheck:
    def __init__(self):
        curr_path = os.path.abspath(__file__)
        folder_path = os.path.dirname(curr_path)
        sub_folders = [
            name
            for name in os.listdir(folder_path)
            if os.path.isdir(os.path.join(folder_path, name))
        ]

        for folderNo in range(len(sub_folders)):
            module_file = os.path.join(folder_path, sub_folders[folderNo], csv_name)
            try:
                Readin_csv = pd.read_csv(
                    module_file,
                    skipinitialspace=false,
                    engine="python",
                    header=0,
                    error_bad_lines=False,
                    warn_bad_lines=True,
                )
                Readin_csv.insert(0, column="count", value=1)
                savefilename = sub_folders[folderNo]
                Readin_csv.to_csv(
                    os.path.join(
                        folder_path,
                        sub_folders[folderNo],
                        sub_folders[folderNo] + ".csv",
                    ),
                    sep=";",
                    quoting=csv.QUOTE_NONE,
                    escapechar=";",
                    index=false,
                )
            except FileNotFoundError:
                continue
