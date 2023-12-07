# Copyright (C) 2015-2018 Jurriaan Bremer.
# This file is part of VMCloak - http://www.vmcloak.org/.
# See the file 'docs/LICENSE.txt' for copying permission.

from vmcloak.abstract import Dependency

class Python(Dependency):
    name = "python"
    default = "3.7.3"
    exes = [{
        "version": "2.7.6",
        "urls": [
            "https://www.python.org/ftp/python/2.7.6/python-2.7.6.msi",
            "https://cuckoo.sh/vmcloak/python-2.7.6.msi",
        ],
        "sha1": "c5d71f339f7edd70ecd54b50e97356191347d355",
        "filename": "python-2.7.6.msi",
        "window_name": "Python 2.7.6 Setup",
        "install_path": "C:\\Python27",
    }, {
        "version": "2.7.13",
        "urls": [
            "https://www.python.org/ftp/python/2.7.13/python-2.7.13.msi",
            "https://cuckoo.sh/vmcloak/python-2.7.13.msi",
        ],
        "sha1": "7e3b54236dbdbea8fe2458db501176578a4d59c0",
        "filename": "python-2.7.13.msi",
        "window_name": "Python 2.7.13 Setup",
        "install_path": "C:\\Python27",
    }, {
        "version": "3.7.3",
        "urls": [
            "https://www.python.org/ftp/python/3.7.3/python-3.7.3-amd64.exe",
        ],
        "sha1": "bd95399506f362e7618d4f6b5a429ebf44714585",
        "filename": "python-3.7.3-amd64.exe",
        "window_name": "Python 3.7.3 (64-bit) Setup",
        "install_path": "C:\\Python3"
    }, {
        "version": "3.10.0",
        "urls": [
            "https://www.python.org/ftp/python/3.10.0/python-3.10.0-amd64.exe",
        ],
        "sha1": "3ee4e92a8ef94c70fb56859503fdc805d217d689",
        "filename": "python-3.10.0-amd64.exe",
        "window_name": "Python 3.10.0 (64-bit) Setup",
        "install_path": "C:\\Python3"
    }]

    def run(self):
        self.upload_dependency("C:\\python.exe")

        self.a.execute("C:\\python.exe PrependPath=1 TargetDir=%s /passive" % self.install_path)
        self.a.remove("C:\\python.exe")

class Python27(Python, Dependency):
    """Backwards compatibility."""
    name = "python27"
    recommended = False
