import subprocess, sys, os, config
try:
    from googleapiclient.discovery import build
    from google_auth_oauthlib.flow import InstalledAppFlow
    from google.auth.transport.requests import Request
    modulesInstalled = True
except:
    modulesInstalled = False

def installGoogleDriveModules():
    try:
        # Automatic setup does not start on some device because pip tool is too old
        updatePip = subprocess.Popen("pip install --upgrade pip", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        *_, stderr = updatePip.communicate()
        if not stderr:
            print("pip tool updated!")
    except:
        pass
    try:
        updatePip = subprocess.Popen("pip install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        *_, stderr = updatePip.communicate()
        if not stderr:
            print("Python modules on Google Drive are installed!")
    except:
        pass

def uploadNotes():
    try:
        noteFileCloudId = os.path.join("plugins", "NotesUtility", "noteFileGoogleCloudId.txt")
        upload = subprocess.Popen("{0} {1} upload".format(sys.executable, os.path.join("plugins", "NotesUtility", "access_google_drive.py")), shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, stderr = upload.communicate()
        if not stderr:
            text = stdout.decode("utf-8")
            if text.startswith("Please visit this URL"):
                text = "{0}\n".format(text.split("\n")[1])
            with open(noteFileCloudId, "w") as f:
                f.write(text)
            config.mainWindow.displayMessage("Uploaded 'note.sqlite' to Google Drive!\nFile ID: {0}".format(text[:-1]))
        else:
            config.mainWindow.displayMessage("Failed to upload bible notes!")
    except:
        config.mainWindow.displayMessage("Failed to upload bible notes!")


credentials = os.path.join("credentials.json")
noteFile = os.path.join(os.getcwd(), "marvelData", "note.sqlite")
if not os.path.isfile(credentials):
    config.mainWindow.displayMessage("You have not yet enabled Goolge Drive API! \nBefore you can use this feature, you need to: \ndownload 'credentials.json' from \nhttps://developers.google.com/drive/api/v3/quickstart/python \nand place it in UniqueBible root directory.")
elif not os.path.isfile(noteFile):
    config.mainWindow.displayMessage("You have not created a bible note yet!")
else:
    if not modulesInstalled:
        print("Installing missing modules ...")
        installGoogleDriveModules()
        uploadNotes()
    else:
        uploadNotes()