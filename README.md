# Cisco-Meeting-Server

This GitHub Example is how to host your invitation/email template files, from a webserver, that Cisco Meeting Server will send to the web app for multiple languages.<br /> 

## Prerequisite:<br />
1)Pre-configured Python environment on the IIS server.<br />
2)Knowledge of Python Scripting.<br />
3)The following modules in your Python Project:  bottle and os.<br />
4)Microsoft Server 2016 IIS 10.0<br />
5) Cisco Meeting Server 3.1.x 

## High View on Deploment of Invitation/Email Templates hosted on a webserver files<br />

**Deployment of Python3:**<br />
<br />
* 1) Install Python3 on the web server in our case it is IIS [Download Python3 Here](https://www.python.org/downloads/).  Configure Python3 with a virtual environment in which your modules bottle and os will run and activate the venv for the project [Documentation on Python virtual environments](https://docs.python.org/3/library/venv.html).<br />/

* 2) Copy the Invites Python Project into the venv or create your own project and use the Invites script: [Invites Script Pthon 3.9](https://github.com/jjanson123/Cisco-Meeting-Server-Invitation-templates-web-server/blob/main/Invites%20Script%20Pthon%203.9) in the GitHub.  If you use the script then please install bottle module.  Here is a url on how to use bottle [Bottle Documentation](https://bottlepy.org/docs/dev/).<br />
