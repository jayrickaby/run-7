import os
import platform
import webbrowser

from PySide6.QtCore import Property, Slot, QObject, QUrl

from settings import settings

class System(QObject):
    @Property(str, constant=True)
    def os_name(self):
        if settings.os_override:
            return settings.os_override

        if settings.pretty_os_names:
            return self.pretty_os_name

        return self.simple_os_name

    @Property(str, constant=True)
    def pretty_os_name(self):
        name = self.simple_os_name

        if name == "Windows":
            return f"{name} {platform.win32_ver()[0]}"

        elif name == "macOS":
            return name

        elif name == "Linux":
            return platform.freedesktop_os_release()['NAME']

        return ""

    @Property(str, constant=True)
    def simple_os_name(self):
        name = platform.system()

        if name == "Darwin":
            return "macOS"

        return name

    @Slot(str, result=bool)
    def open_url(self, url):
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

    @Slot(QUrl, result=str)
    def process_file_path(self, url):
        return os.path.abspath(url.toLocalFile())

system = System()
