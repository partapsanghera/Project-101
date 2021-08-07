import os
import dropbox

class TransferData():
    def __init__(self, access_token):
        self.access_token = access_token

    def upload_file(self, file_from, file_to):
        dbx = dropbox.Dropbox(self.access_token)

        for root, dirs, files in os.walk(file_from):
            for name in files:
                path = os.path.join(root, name)
                print(path)

                relative_path = os.path.relpath(path, file_from)
                dropbox_path = os.path.join(file_to, relative_path)

                with open(path, "rb") as f:
                    dbx.files_upload(f.read(), dropbox_path, mode=dropbox.files.WriteMode.overwrite)

def main():
    access_token = "pDrWNGKY8yMAAAAAAAAAARzthKKGRcy0-NsG98dAyDX87O9_OFhbcS_6LS_Ye6r7"
    transfer__data = TransferData(access_token)

    file_from = input("Enter The Path Of File To Be Taken:- ")
    file_to = input("Enter The Path Where The File Is To Be Dropped:- ")

    transfer__data.upload_file(file_from, file_to)

    print("Your File Has Been Uploaded Successfully!")
    
main()