### Add this code to the invites.py project to host your call customization files from the bottle webframework web server.  
```python

#this is the code which will route API GET request for the call customization files for CMS.  API Sends http://14.49.18.252:8080/Brand/CallBranding

@get("/Brand/CallBranding/<filepath:re:.*\.(jpg|wav)>")
def brand(filepath):
    call=request.get('/Brand/CallBranding/<filepath:re:.*\.(jpg|wav)>')
    my_root = os.path.join(my_dir, 'CallBranding')
    return static_file(filepath, root=my_root)
```
