from bottle import route, run, static_file, error, request, get
import os
import paste

# My current working directory
my_dir = os.getcwd()


# Route this API GET request to return invitation templates and query of the language.
# NOTE: Change the route in parenthesis to match your GET  requests.
@route('/Brand/invitation_template')
def invite_static():
    language = request.query.get('language')
    filepath = 'invitation_template_' + language + '.txt'
    my_root = os.path.join(my_dir, 'static')
    return static_file(filepath, root=my_root)

# My webbridge3 webapp branding route this API GET request for the archive.zip file API Sends http://<bottle
# webserver ip>:8080/Brand/webapp/rebels.zip
@route('/Brand/webapp/rebels.zip')
def webapp_static():
    filepath = 'rebels.zip'
    my_root = os.path.join(my_dir, 'static')
    return static_file(filepath, root=my_root)

# This is the code which will route API GET request for the call customization files for CMS.  API Sends
# http://14.49.18.252:8080/Brand/CallBranding

@get("/Brand/CallBranding/<filepath:re:.*\.(jpg|wav)>")
def callbrand_static(filepath):
    my_root = os.path.join(my_dir, 'CallBranding')
    return static_file(filepath, root=my_root)


# This responds with an error 404 not found if the requests fails.  NOTE this is only seeen in bottle logging.  CMS
# will provide the default invitation template in callbridge if no file is returned by bottle webframework.
@error(404)
def error404(error):
    return 'Nothing here, sorry'


# run(server='paste') is added for multi-thread server
# run(host='0.0.0.0', port=8080, debug=True)
run(server='paste', host='0.0.0.0', port=8080, debug=True)
