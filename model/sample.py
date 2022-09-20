import datetime

from sqlmodel import SQLModel, Field


class Sample(SQLModel, table=True):
    id_sample: int = Field(default=None, primary_key=True)
    id_project: int
    Date: datetime.date
    id_experimenter: int
    Target_Compo: str
    P_B: str
    P_LC: str
    Deposition_temp: int
    Anneal_Temp: int
    Anneal_Time: int
    Gas: str
    P_Gas: str
    Q_Gas: int
    Gun_Angle: str
    Substrate_Height: int
    Rotation_Speed: int
    Sputtering_Type: str
    Power: str
    Deposition_Time: int
    Target_Thick: int
    Sample_Shape: str
    Silicon_Thick: int
    Adh_Compo: str
    Adh_Pow: str
    Adh_time: int
    Adh_Rotation: int
    Substrate: str
    Substrate_Thick: int
    Comment: str

    class Config:
        arbitrary_types_allowed = True
        schema_extra = {
            "examples": {
                "id_sample": 32,
                "id_project": 1,
                "Date": "2020-10-06",
                "id_experimenter": 1,
                "Target_Compo": "",
                "P_B": "",
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

