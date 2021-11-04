from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
gauth = GoogleAuth()
gauth.LoadCredentialsFile("creds.json")    
drive = GoogleDrive(gauth) 

gfile = drive.CreateFile({'id': '1FbVyfkYS87m9ab8a961h_HXaYhe17Dj4'})
gfile.SetContentFile('census_log_dw.csv')
gfile.Upload() # Upload the file.
gfile = None

gfile = drive.CreateFile({'id': '1tGrkrWlPhhc1XjfCUDETU7HjW3lo3e8J'})
gfile.SetContentFile('tendays_dw.csv')
gfile.Upload() # Upload the file.
gfile = None
