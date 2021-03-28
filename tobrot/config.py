from tobrot.sample_config import Config

class Config(Config):
    TG_BOT_TOKEN= "1301781981:AAGb2NngTvx_sd76flP9RDs4x1KnS9MfSj8" #imp
    APP_ID = 1711488 #imp
    API_HASH = "707667e743148abde192655aa64d21f6" #imp
    AUTH_CHANNEL = [-420813515, 999162609] #imp replace your_id with your id from telegram or delete
    GLEECH_COMMAND = "gleech@drivoidbot"
    YTDL_COMMAND = 'ytdl@drivoidbot'
    TELEGRAM_LEECH_COMMAND_G = "tleech@drivoidbot"
    CLONE_COMMAND_G = "gclone@drivoidbot"
    PYTDL_COMMAND_G = "pytdl@drivoidbot"
    DESTINATION_FOLDER = "my drive"
    DOWNLOAD_LOCATION = "./DOWNLOADS"
    INDEX_LINK = "https://www.emvsplex.ga/0:"
    LEECH_COMMAND = "leech@drivoidbot"
    CANCEL_COMMAND_G = "cancel@drivoidbot"
    LOG_COMMAND = "log@drivoidbot"
    STATUS_COMMAND = "status@drivoidbot"
    UPLOAD_COMMAND = "upload@drivoidbot"
    RENEWME_COMMAND = "renewme@drivoidbot"
    GET_SIZE_G = "getsize@drivoidbot"
    OWNER_ID = 999162609
    PROCESS_MAX_TIMEOUT = 3600
    MAX_MESSAGE_LENGTH = 4096
    MAX_FILE_SIZE = 50000000
    TG_MAX_FILE_SIZE = 2097152000
    FREE_USER_MAX_FILE_SIZE = 50000000
    RCLONE_CONFIG = """
    [DRIVE]
    type = drive
    client_id = 689614248022-f8jm4n8os876g0fe3k66hu4vn2hjnmm6.apps.googleusercontent.com
    client_secret = OCz4MamcnnHh70oanlxxMoeK
    scope = drive
    token = {"access_token":"ya29.a0AfH6SMCs-sXEWJS9isl61E_eYmpNxAR7l2w2JXb91HhHwjKdbXyG8ajmHEpDwjTrlopRySglAmyqJxgm6DBBom1KAphXFV0Z32b_Kt1K9dJJMWZa9Kn07ksbzT4PJqga2qMSBOIJli2kiCX_Gt2NUGlWl-fauqh15kOxbmNxmmk","token_type":"Bearer","refresh_token":"1//0g1wyhUv0ZH3CCgYIARAAGBASNwF-L9Irpe0OOfycW5ELFb2PO_Bp2ln9SE2voqWQHwDyTXBxRsj1m--tQS6KNMOgZXx-uAUSjyk","expiry":"2020-12-23T10:13:03.7093259+05:30"}
    team_drive = 0AL2f4TZ1lf0IUk9PVA
    """
    #put your config(replacing new lines with \n) in triple quote like above: """<your one liner config>"""
