from PySide6.QtCore import QObject, Property
from PySide6.QtQml import QmlElement
from pathlib import Path

QML_IMPORT_NAME = "jayrickaby.run7.app"
QML_IMPORT_MAJOR_VERSION = 1

@QmlElement
class Application(QObject):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.__parentPath = Path(__file__).parent
        self.__defaultTitle = "Run–7"
        self.__title = None

    @Property(str, constant=True)
    def icon(self):
        return str(self.__parentPath / "qml" / "assets" / "icons" / "win7.ico")

    @Property(str, constant=True)
    def parentPath(self):
        return self.__parentPath

    @Property(str, constant=True)
    def projectRootFolder(self):
        return str(self.__parentPath.parent.parent.absolute())

    @Property(str, constant=True)
    def externalFolder(self):
        return str(self.__parentPath.parent.parent.absolute() / "external")

    @Property(str, constant=True)
    def currentTitle(self):
        return self.__defaultTitle if self.__title is None else self.__title
