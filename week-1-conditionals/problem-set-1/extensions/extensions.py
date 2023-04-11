extension = input("File name: ")
if extension.endswith(".gif"):
    print("image/gif")
elif extension.endswith(".jpg") or extension.endswith(".jpeg"):
    print("image/jpeg")
elif extension.endswith(".png"):
    print("image/png")
elif extension.endswith(".pdf"):
    print("application/pdf")
elif extension.endswith(".txt"):
    print("text/plain")
elif extension.endswith(".zip"):
    print("application/zip")
else:
    print("application/octet-stream")


# Method 2: more concise and easier to maintain than the original code.
# Define a dictionary that maps file extensions to MIME types
# mime_types = {
#     ".gif": "image/gif",
#     ".jpg": "image/jpeg",
#     ".jpeg": "image/jpeg",
#     ".png": "image/png",
#     ".pdf": "application/pdf",
#     ".txt": "text/plain",
#     ".zip": "application/zip",
#     ".doc": "application/msword",
#     ".docx": "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
#     ".xls": "application/vnd.ms-excel",
#     ".xlsx": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
#     ".ppt": "application/vnd.ms-powerpoint",
#     ".pptx": "application/vnd.openxmlformats-officedocument.presentationml.presentation",
#     ".mp4": "video/mp4",
#     ".mp3": "audio/mp3"
# }

# # Get the file extension from the user
# filename = input("File name: ")
# extension = "." + filename.split(".")[-1]

# # Look up the MIME type based on the file extension
# if extension in mime_types:
#     print(mime_types[extension])
# else:
#     print("application/octet-stream")
