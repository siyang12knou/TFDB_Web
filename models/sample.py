import datetime
from typing import Optional

from sqlmodel import JSON, SQLModel, Field, Column


class Sample(SQLModel, table=True):
    id_sample: Field(default=None, primary_key=True)
    id_project: int
    Date: datetime.date
    id_experimenter: Optional[int]
    Target_Compo: str
    P_B: Optional[str]
    P_LC: Optional[str]
    Deposition_temp: Optional[int]
    Anneal_Temp: Optional[int]
    Anneal_Time: Optional[int]
    Gas: Optional[str]
    P_Gas: Optional[str]
    Q_Gas: Optional[int]
    Gun_Angle: Optional[str]
    Substrate_Height: Optional[int]
    Rotation_Speed: Optional[int]
    Sputtering_Type: Optional[str]
    Power: Optional[str]
    Deposition_Time: Optional[int]
    Target_Thick: Optional[int]
    Sample_Shape: Optional[str]
    Silicon_Thick: Optional[int]
    Adh_Compo: Optional[str]
    Adh_Pow: Optional[str]
    Adh_time: Optional[int]
    Adh_Rotation: Optional[int]
    Substrate: Optional[str]
    Substrate_Thick: Optional[int]
    Comment: Optional[str]

    class Config:
        schema_extra = {
            "examples": {
                "id_sample": 32,
                "id_project": 1,
                "Date": "2020-10-06",
                "id_experimenter": 1,
                "Target_Compo": "",
                "P_B": "rl;f'efkef",
                "P_LC": "",
                "Deposition_temp": 0,
                "Anneal_Temp": 0,
                "Anneal_Time": 0,
                "Gas": " ",
                "P_Gas": "",
                "Q_Gas": 0,
                "Gun_Angle": "",
                "Substrate_Height": 0,
                "Rotation_Speed": 0,
                "Sputtering_Type": "Sequential",
                "Power": "",
                "Deposition_Time": 0,
                "Target_Thick": 0,
                "Sample_Shape": "",
                "Silicon_Thick": 0,
                "Adh_Compo": "",
                "Adh_Pow": "",
                "Adh_time": 0,
                "Adh_Rotation": 0,
                "Substrate": "None",
                "Substrate_Thick": 0,
                "Comment": "Dummy data"
            }
        }


