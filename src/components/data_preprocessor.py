import pandas as pd
import numpy as np
import os

from src.exception import CustomException
from src.logger import logging
from dataclasses import dataclass

ath_df = pd.read_csv(
    r"C:\Users\Lenovo\Desktop\webapps\Olympics Da\data\athlete_events.csv"
)
region_df = pd.read_csv(r"data\noc_regions.csv")


@dataclass
class DataPath:
    data_pkl_path = os.path.join("artifact", "preprocessor.pkl")


class Preprocessor:
    def __init__(self) -> None:
        self.data_pkl_path = DataPath()

    def preprocessor(self):
        try:
            global ath_df, region_df
            ath_df = ath_df[ath_df["Season"] == "Summer"]

            ath_df = ath_df.merge(region_df, on="NOC", how="left",suffixes=('','_y'))
            ath_df.drop(ath_df.filter(regex='_y$').columns,axis=1,inplace=True)

            ath_df.drop_duplicates(inplace=True)

            medal_encoder = pd.get_dummies(ath_df["Medal"], dtype="int32")

            df = pd.concat([ath_df, medal_encoder], axis=1)

            return df
        except Exception as e:
            raise CustomException(e)
