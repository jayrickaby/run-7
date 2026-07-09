
from application import application, ORG_NAME, APP_NAME
from PySide6.QtCore import QObject, Property, Slot, QUrl, QSettings
from PySide6.QtQml import QmlElement

QML_IMPORT_NAME = "jayrickaby.run7.settings"
QML_IMPORT_MAJOR_VERSION = 1

@QmlElement
class Settings(QObject):
    def __init__(self, parent=None):
        super().__init__(parent)
        self._settings = QSettings(ORG_NAME, APP_NAME)

        # Appearance
        self.__prettyOsNames = bool(self._settings.value("Appearance/prettyOsNames", False))
        self.__icon = self._settings.value("Appearance/icon", application.defaultIcon)
        self.__osOverride = self._settings.value("Appearance/osOverride", None)
        self.__title = str(self._settings.value("Appearance/title", application.defaultTitle))

        # History
        self.__limitHistorySize = int( self._settings.value("History/limitHistorySize", 5))
        self.__urlHistory = self.__checkUrlHistoryValid( self._settings.value("History/urlHistory", []))

    def __checkUrlHistoryValid(self, history):
        if type(history) is list:
            pass
        elif history:
            history = [history]
        else:
            history = []

        return history

    @Property(int, constant=True)
    def limitHistorySize(self):
        return self.__limitHistorySize

    @Property(list, constant=True)
    def urlHistory(self):
        return self.__urlHistory

    @Property(bool, constant=True)
    def prettyOsNames(self):
        return self.__prettyOsNames

    @Property(str, constant=True)
    def title(self):
        return self.__title

    @Property(QUrl, constant=True)
    def icon(self):
        return QUrl.fromLocalFile(self.__icon)

    @Property(str, constant=True)
    def osOverride(self):
        return self.__osOverride

    @Slot(list)
    def setUrlHistory(self, urls):
        self.__urlHistory = urls
        self._settings.setValue("History/urlHistory", urls)

settings = Settings()