## Cisco Meeting Server WebApp Branding Code:<br /><p />
You can add this snipett of code to the invites.py project and add your brand.zip file for webapp to the static folder and 
start hosting webapp branding from same bottle webserver.<br /><p />


`code()`
#my webbridge3 webapp branding GET request for the archive.zip file API Sends http://<bottle webserver ip>:8080/Brand/webapp/rebels.zip<br />
@route('/Brand/webapp/rebels.zip')<br />
def webapp_static():<br />
    rebels=request.get('/Brand/webapp/rebels.zip')<br />
    filepath='rebels.zip'<br />
    #print(filepath)<br />
    #print(my_dir)<br />
    my_root = os.path.join(my_dir, 'static')<br />
    return static_file(filepath, root=my_root)<br />
