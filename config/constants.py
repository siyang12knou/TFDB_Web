from enum import Enum


yyyymmdd = '%Y%m%d'
yyyymmddHHMM = '%Y%m%d%H%M'
token_type = "Bearer"
tfdbmgr: str = "tfdbmgr"


class Level(Enum):
    INFO = 400
    WARNING = 300
    ERROR = 200


class Action(Enum):
    login = 0
    logout = 1
    create_user = 3
    update_user = 4
    delete_user = 5
    get_file_list = 6
    download_file = 7
    upload_file = 8


class TfdbCategory(Enum):
    EDS = 1
    Resistance = 2
    Thickness = 3
    XRD = 4
    Hardness = 5
    Image = 6


class Role(Enum):
    ADMIN = 0
    TFDB_MANAGER = 1
    TFDB_RESEARCHER = 2
    TFDB_WORKER = 3
    TFDB_VISITOR = 4
