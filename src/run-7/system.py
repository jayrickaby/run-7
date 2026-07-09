import platform
import webbrowser
import os
from settings import settings

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

    @Property(str, constant=True)
    def prettyOsName(self):
        name = self.simpleOsName

        if name == "Windows":
            return f"{name} {platform.win32_ver()[0]}"

        elif name == "macOS":
            return name

        elif name == "Linux":
            return platform.freedesktop_os_release()['NAME']

        return ""

    @Property(str, constant=True)
    def osName(self):
        if settings.osOverride:
            return settings.osOverride

        if settings.prettyOsNames:
            return self.prettyOsName

        return self.simpleOsName

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

system = System()
