from office365.runtime.auth.authentication_context import AuthenticationContext
from office365.sharepoint.client_context import ClientContext
from office365.runtime.auth.user_credential import UserCredential
from office365.sharepoint.files.file import File
import os

url = 'https://<tenent>.sharepoint.com/sites/<site-name>'
sharepoint_user = 'useremail'
sharepoint_password = 'password'
    
context_auth = AuthenticationContext(url)
context_auth.acquire_token_for_user(sharepoint_user, sharepoint_password)
ctx = ClientContext(url, context_auth)

tempfile = 'C:\\Users\\Profile\\Desktop' #Local System Path
file_url = "/sites/<site-name>/Shared Documents/<filename>.xlsx"
download_path = os.path.join(tempfile, os.path.basename(file_url))
with open(download_path, "wb") as local_file:
    #file = ctx.web.get_file_by_server_relative_path(file_url).download(local_file).execute_query()
    file = ctx.web.get_file_by_server_relative_url(file_url).download(local_file).execute_query()
print("[Ok] file has been downloaded into: {0}".format(download_path))
