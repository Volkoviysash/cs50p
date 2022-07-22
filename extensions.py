filename = input("Filename: ")

imageformats = [".gif", ".png" ,".jpg", ".jpeg"]
applicationformats = {".pdf", ".rtf", ".zip"}
textformats = {".txt"}


format = filename[filename.rindex('.'):]

if format in imageformats:
    print(f"image/{format[1:]}")
elif format in applicationformats:
    print(f"application/{format[1:]}")
elif format in textformats:
    print("text/plain")
else:
    print("application/octet-stream")