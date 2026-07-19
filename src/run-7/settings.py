from application import application, APP_NAME, ORG_NAME
from PySide6.QtCore import Property, Slot, QObject, QSettings, QUrl

class Settings(QObject):
    def __init__(self, parent=None):
        super().__init__(parent)
        self._settings = QSettings(ORG_NAME, APP_NAME)

        self._settings.beginGroup("Appearance")
        self._pretty_os_names = bool(
            self._settings.value(
                "prettyOsNames", False
            )
        )
        self._icon = self._settings.value(
            "icon", application.get_default_icon()
        )
        self.__osOverride = self._settings.value(
            "osOverride",
            None
        )

        self._title = str(
            self._settings.value(
                "title", application.get_default_title()
             )
        )
        self._settings.endGroup()

        self._settings.beginGroup("History")
        self._limit_history_size = int(
            self._settings.value(
                "limitHistorySize", 5
            )
        )

        self._url_history = self._check_url_history_valid(
            self._settings.value(
                "urlHistory", []
            )
        )
        self._settings.endGroup()

    def _check_url_history_valid(self, history):
        if type(history) is list:
            pass
        elif history:
            history = [history]
        else:
            history = []

        return history

    @Property(int, constant=True)
    def limit_history_size(self):
        return self._limit_history_size

    @Property(list, constant=True)
    def url_history(self):
        return self._url_history

    @Property(bool, constant=True)
    def pretty_os_names(self):
        return self._pretty_os_names

    @Property(str, constant=True)
    def title(self):
        return self._title

    @Property(QUrl, constant=True)
    def icon(self):
        return QUrl.fromLocalFile(self._icon)

    def get_icon(self):
        return QUrl.fromLocalFile(self._icon)

    @Property(str, constant=True)
    def os_override(self):
        return self.__osOverride

    @Slot(list)
    def set_url_history(self, urls):
        self._url_history = urls
        self._settings.setValue("History/urlHistory", urls)

settings = Settings()