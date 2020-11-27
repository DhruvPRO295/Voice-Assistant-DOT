import json

spotify_credentials = {
    "spotify_email": "<YOUR EMAIL>",
    "spotify_pass": "<YOUR PASSWORD>"
}
with open('Sources\\credentials.json', 'w') as outfile:
    json.dump(spotify_credentials, outfile)

print("Task Successfully Done \n Exported JSON Data to %s  " % outfile.name)
