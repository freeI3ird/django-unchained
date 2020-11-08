# Apache

#### Installing Apache
```   
      sudo apt-get update
      sudo apt-get install apache2
```

#### Common Instructions
1. Verify Installation
   - http://localhost/ : Open the url in web browser
2. Stop, start, restart, reload apache server
   ```
   sudo systemctl stop apache2.service
   sudo systemctl start apache2.service
   sudo systemctl restart apache2.service
   sudo systemctl reload apache2.service
   ```
3. Check the status of Server
    - http://localhost/server-status: open url in web browser
    - Command: `sudo systemctl status apache2`

#### mod_wsgi
- It is an apache module which can host Python wsgi applications

#### WSGI
- Web Server Gateway Interface
- It is a specification of generic API(i.e guidelines about how to write this generic API). Then this API will act as interface between the web server and Python Application.
- Purpose: To provide a common mechanism for hosting the Python applicaton on different type of web servers.
- WSGI Application should not be placed within Root directory of Apache main installation or particular site. Because that local is mainly to serve static things and if our script is kept there, it can be downloaded.
- `WSGI Application will act as mapping between python application and web server.`
- mod_wsgi requires that the WSGI application entry point have a fixed name called ‘application’.
- `Mounting: Attaching/connecting/relating a specific path(mount point) to a application or device is k/a mounting of device/application`
- Mounting WSGI application to specific url
  - Using WSGIScriptAlias directive
  - **WSGIScriptAlias  [URL-mount-point]  [reference-to-wsgi-script]**
  - E.g: WSGIScriptAlias /myapp /home/mr/wsgi-applicatons/script-name.wsgi
  - Write this directive in Apache main configuration file(apache2.conf)
- 
