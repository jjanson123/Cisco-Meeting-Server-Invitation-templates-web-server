### Add this code to the invites.py project to host your call customization files from the bottle webframework web server.  
```python

#this is the code which will route API GET request for the call customization files for CMS.  API Sends http://14.49.18.252:8080/Brand/CallBranding

@get("/Brand/CallBranding/<filepath:re:.*\.(jpg|wav)>")
def brand(filepath):
    call=request.get('/Brand/CallBranding/<filepath:re:.*\.(jpg|wav)>')
    my_root = os.path.join(my_dir, 'CallBranding')
    return static_file(filepath, root=my_root)

#### When testing the call customization script you will not see any GET requests from CMS until someone initiates a call to a space that has a CallBrandingProfile applied to it or when you have the CallBrandingProfile on the SystemProfile.  As seen in the below examples there are 200OK responses to some of the files while there are 404 Not Found for others.  Please be sure all the currently required files are included in the python invites.py project.  In my project the call customization files are in the folder called CallBranding.

![alt text] (https://github.com/jjanson123/Cisco-Meeting-Server-Invitation-templates-web-server/blob/main/call%20custom.PNG)
```
