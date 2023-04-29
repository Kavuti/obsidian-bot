from pydrive2.auth import GoogleAuth
from pydrive2.drive import GoogleDrive
from pprint import pprint
from datetime import datetime


def get_authentication():
    settings = {
        "client_config_backend": "service",
        "service_config": {
            "client_json_file_path": "service-secrets.json",
        },
    }
    gauth = GoogleAuth(settings=settings)
    gauth.ServiceAuth()
    return gauth


auth = get_authentication()
drive = GoogleDrive(auth)


def create_note(content):
    files = drive.ListFile().GetList()
    inbox_folder = None
    for file in files:
        if "Inbox" in file["title"]:
            inbox_folder = file["id"]
            break

    now = datetime.now().strftime("%d-%m-%Y-%H-%M-%S")
    note = drive.CreateFile(
        {
            "title": f"{now}.md",
            "parents": [{"id": inbox_folder}],
        }
    )
    note.SetContentString(content)
    note.Upload()
    return note
