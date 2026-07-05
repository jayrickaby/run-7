import platform
import webbrowser
import os

from PySide6.QtCore import QObject, Property, Slot
from PySide6.QtQml import QmlElement

QML_IMPORT_NAME = "jayrickaby.run7.system"
QML_IMPORT_MAJOR_VERSION = 1

@QmlElement
class System(QObject):

    @Property(str, constant=True)
    def simpleOsName(self):
        name = platform.system()

        if name == "Darwin":
            return "macOS"

        return name

    @Slot(str, result=bool)
    def openUrl(self, url):
        cleanUrl = url.replace('"', "").strip()

        if cleanUrl.startswith(("http://", "https://", "file://")):
            target = cleanUrl

        elif cleanUrl.startswith("www."):
            target = f"https://{cleanUrl}"

        else:
            absolutePath = os.path.abspath(cleanUrl)
            if not os.path.exists(absolutePath): return False

            target = f"file://{absolutePath}"

        return webbrowser.open(target)
