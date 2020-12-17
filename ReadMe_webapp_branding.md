## Cisco Meeting Server WebApp Branding Code:<br /><p ?>
You can add this snipett of code to the invites.py project and add your brand.zip file for webapp to the static folder and 
start hosting webapp branding from same bottle webserver.<br /><p />




#my webbridge3 webapp branding GET request for the archive.zip file API Sends http://<bottle webserver ip>:8080/Brand/webapp/rebels.zip
@route('/Brand/webapp/rebels.zip')
def webapp_static():
    rebels=request.get('/Brand/webapp/rebels.zip')
    filepath='rebels.zip'
    #print(filepath)
    #print(my_dir)
    my_root = os.path.join(my_dir, 'static')
    return static_file(filepath, root=my_root)
