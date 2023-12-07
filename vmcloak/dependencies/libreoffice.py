# Copyright (C) 2015-2018 Jurriaan Bremer.
# This file is part of VMCloak - http://www.vmcloak.org/.
# See the file 'docs/LICENSE.txt' for copying permission.

from vmcloak.abstract import Dependency

config = """
<?xml version="1.0"?>
 <oor:data xmlns:xs="http://www.w3.org/2001/XMLSchema"
 xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
 xmlns:oor="http://openoffice.org/2001/registry">
   <dependency file="main" />
   <oor:component-data xmlns:install="http://openoffice.org/2004/installation"
   oor:name="Common" oor:package="org.openoffice.Office">
     <node oor:name="Security">
       <node oor:name="Scripting">
         <prop oor:name="MacroSecurityLevel" oor:op="fuse">
           <value>0</value>
         </prop>
       </node>
     </node>
   </oor:component-data>
 </oor:data>
"""

class LibreOffice(Dependency):
    name = "libreoffice"
    default = "7.6.4"
    exes = [{
        "version": "7.6.4",
        "url": "https://download.documentfoundation.org/libreoffice/stable/7.6.4/win/x86_64/LibreOffice_7.6.4_Win_x86-64.msi",
        "sha1": "ee8112b9eea7c8b4e6ef9e38604ad92d7976196b",
    }]

    def run(self):
        self.upload_dependency("C:\\%s" % self.filename)
        self.a.execute("msiexec /i C:\\%s RebootYesNo=No /qn" % self.filename)
        self.a.upload(
            "C:\\Program Files\\LibreOffice\\share\\registry\\macrosConfig.xcd",
            config
        )
        self.a.remove("C:\\%s" % self.filename)
