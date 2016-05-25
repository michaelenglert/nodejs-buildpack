import os
import sys
import json
import os.path
import logging
import subprocess
import commands

class Appdynamics_ext:
    def set_environ_variables(self):
        setEnv = "cf set-env %s http_proxy %s"%(self.applicationName, self.httpProxy)
        subprocess.call(setEnv)

    def generate_appdy_statement(self):
        self.VCAP_SERVICES=json.loads(os.environ['VCAP_SERVICES'])
        self.VCAP_APPLICATION=json.loads(os.environ['VCAP_APPLICATION'])

        if "appdynamics" in str(self.VCAP_SERVICES):
            self.extension_name = "appdynamics"
        else:
            self.extension_name = "user-provided"

        self.controllerHostName = self.VCAP_SERVICES["user-provided"][0]["credentials"]["host-name"]
        self.controllerPort = self.VCAP_SERVICES["user-provided"][0]["credentials"]["port"]
        self.accountAccessKey = self.VCAP_SERVICES["user-provided"][0]["credentials"]["account-access-key"]

        if "ssl-enabled" in str(self.VCAP_SERVICES):
            self.controllerSslEnabled = self.VCAP_SERVICES["user-provided"][0]["credentials"]["ssl-enabled"]
        else:
            self.controllerSslEnabled = "false"
        if "account-name" in str(self.VCAP_SERVICES):
            self.accountName = self.VCAP_SERVICES["user-provided"][0]["credentials"]["account-name"]
        else:
            self.accountName = "customer1"
        if "application-name" in str(self.VCAP_SERVICES):
            self.applicationName = self.VCAP_SERVICES["user-provided"][0]["credentials"]["application-name"]
        else:
            self.applicationName = self.VCAP_APPLICATION["application_name"]
        if "tier-name" in str(self.VCAP_SERVICES):
            self.tierName = self.VCAP_SERVICES["user-provided"][0]["credentials"]["tier-name"]
        else:
            self.tierName = self.VCAP_APPLICATION["application_name"]

        self.nodeName = "%s:%s"%(self.tierName, str(os.system("echo $VCAP_APPLICATION | sed -e \'s/.*instance_index.://g;s/\".*host.*//g\' | sed \'s/,//\'")))
        self.httpProxy= os.environ.get('HTTP_PROXY') or os.environ.get('HTTPS_PROXY')

        if self.httpProxy:
            self.set_environ_variables()

        vcap_application_filename = os.path.join("/tmp", '_appd_module.txt')
        f = open(vcap_application_filename, 'w')
        f.write('require("appdynamics").profile({\n')
        f.write('  controllerHostName: \'' + self.controllerHostName + '\',\n')
        f.write('  controllerPort: ' + self.controllerPort + ',\n')
        f.write('  controllerSslEnabled: \'' + self.controllerSslEnabled + '\',\n')
        f.write('  accountName: \'' + self.accountName + '\',\n')
        f.write('  accountAccessKey: \'' + self.accountAccessKey + '\',\n')
        f.write('  applicationName: \'' + self.applicationName + '\',\n')
        f.write('  tierName: \'' + self.tierName + '\',\n')
        f.write('  nodeName: \'' + self.nodeName + '\', \n')
        f.write('});')
        f.close()

Appdynamics_ext_obj = Appdynamics_ext()
Appdynamics_ext_obj.generate_appdy_statement()
