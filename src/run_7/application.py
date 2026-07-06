from PySide6.QtCore import QObject, Property, QUrl
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

    @Property(QUrl, constant=True)
    def icon(self):
        return QUrl.fromLocalFile(str(self.__parentPath / "assets" / "logo" / "icon.png"))

    @Property(QUrl, constant=True)
    def parentPath(self):
        return QUrl.fromLocalFile(self.__parentPath)

    @Property(QUrl, constant=True)
    def projectRootFolder(self):
        return QUrl.fromLocalFile((self.__parentPath.parent.parent.absolute()))

    @Property(QUrl, constant=True)
    def externalFolder(self):
        return QUrl.fromLocalFile(str(self.__parentPath.parent.parent.absolute() / "external"))

    @Property(str, constant=True)
    def currentTitle(self):
        return self.__defaultTitle if self.__title is None else self.__title
