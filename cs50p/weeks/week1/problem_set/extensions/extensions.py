def main():
    filename = input("File name: ").strip()
    filename = filename.lower()
    filetype(filename)

suffix = ['gif', 'pdf', 'zip', 'png', 'jpeg', 'jpg', 'txt']

def filetype(filename):
    filename = filename.split(".")
    if len(filename) >= 2:
        if filename[-1] == 'gif' or filename[-1] == 'png':
            print(f"image/{filename[-1]}")
        if filename[-1] == 'jpg' or filename[-1] == 'jpeg':
            print(f"image/jpeg")
        if filename[-1] == 'txt':
            print(f"text/{filename[0]}")
        if filename[-1] == 'zip' or filename[-1] == 'pdf':
            print(f"application/{filename[-1]}")
    if filename[-1] not in suffix or len(filename) == 1:
        return print("application/octet-stream")

main()