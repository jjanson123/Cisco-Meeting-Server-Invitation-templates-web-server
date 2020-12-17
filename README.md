# Cisco Meeting Server-Invitation/Email Templates

This GitHub Example is how to host your invitation/email template files, from a simple python webserver, that Cisco Meeting Server will send to the web app for multiple languages.
This is especially helpful when you host multiple images for Call Customization / Web App backgrounds and with multiple tenants.<br /> 

## Prerequisite:<br />
1) Pre-configured Python environment on Microsoft Server 2016.<br />
2) Knowledge of Python Scripting.<br />
3) The following modules in your Python Project:  bottle and os.<br />
4) Cisco Meeting Server 3.1.x 

### High View on Deploment of Invitation/Email Templates hosted on a webserver files<br />

**Deployment of Python3:**<br />
<br />
*1) Install Python3 on the Microsoft Server 2016 [Download Python3 Here](https://www.python.org/downloads/).  Configure Python3 with a virtual environment in which your modules bottle.py and os.py will run and activate the venv for the project [Documentation on Python virtual environments](https://docs.python.org/3/library/venv.html).<br /><p />*

*2) Copy the Invites Python Project into the venv [My Invites Python Project files](https://github.com/jjanson123/Cisco-Meeting-Server-Invitation-templates-web-server/blob/main/Invites.zip) **(NOTE:  I hosted all my invitation templates in the static folder of the project)**. You can also, create your own project, from scratch, and use the Invites script: [Invites Script Pthon 3.9](https://github.com/jjanson123/Cisco-Meeting-Server-Invitation-templates-web-server/blob/main/Invites%20Script%20Pthon%203.9) in the GitHub.  If you use the script then please install bottle module.  Here is a url on how to use bottle [Bottle Documentation](https://bottlepy.org/docs/dev/).<br /><p />*

*3) If you have not already created the web server web pages for the CMS Branding per the CMS Customization Guide 3.1 current release as of this GitHub [CMS Customization Guide 3.1](https://www.cisco.com/c/dam/en/us/td/docs/conferencing/ciscoMeetingServer/Customisation/Version-3-1/Cisco-Meeting-Server-3-1-Customization-Guidelines.pdf) do this now then come back to this project. The IIS 10 web server will be serving your Call Customization files and the web app for Branding.  **(NOTE AGAIN ALL OUR INVITATION TEMPLATES ARE IN THE STATIC FOLDER OF THE PROJECT)** <br /><p />*

*4) Launch your Python IDE and run the invites.py program.  This will start the bottle web server which will start to listen for traffic on port 8080.<br /><p />*

###### Image 1-- Below image shows IDE on Left, running bottle web server, and on the right side a console showing http requests for language files with response codes.  We can see 404 not found for files not in the static folder where I am hosting invitation templates.  While we see 200 response codes for the invitation template files found in the static.  
#### (NOTE THAT CMS WILL LOAD THE _DEFAULT INVITATION TEMPLATE_ FROM CMS WHEN THERE IS NO RETURN FROM BOTTLE WEBSERVER.) <b /><p />

![alt text](https://github.com/jjanson123/Cisco-Meeting-Server-Invitation-templates-web-server/blob/main/6_bottle%20server.PNG)

## Cisco Meeting Server API and How This Works<br /><p />
When the web app user chooses a language from the drop down then CMS sends the url, preconfigured in the CallBrandingProfile for invitation templates, and appends the ?language query then forwards that GET to the web server.  Once the python webframe work receives the GET url it performs a lookup for the language file in the current working directory, in this project, the static folder and returns the invitation template back to CMS so that the interpreter can output the correct information to web app.<br /><p />

###### Image 2-- Sample of CallBridgeProfile url used in CMS for this project<br /><p />

![alt text](https://github.com/jjanson123/Cisco-Meeting-Server-Invitation-templates-web-server/blob/main/cms%20callbrandingprofile_api.JPG)


## Disclaimer<br /><p />
This project is only meant as an example of how to parse CMS requests about invitation templates and it will most likely won’t fit your deployment needs in terms or security, scalability and performance.

We don’t recommend its use in production systems and we don't provide support for it.

The software is provided "as is", without warranty of any kind, express or implied, including but not limited to the warranties of merchantability, fitness for a particular purpose and noninfringement. In no event shall the authors or copyright holders be liable for any claim, damages or other liability, whether in an action of contract, tort or otherwise, arising from, out of or in connection with the software or the use or other dealings in the software.


