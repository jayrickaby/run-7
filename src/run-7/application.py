from pathlib import Path

from PySide6.QtCore import Property, QObject, QUrl

ORG_NAME = "JayRickaby"
ORG_DOMAIN = "jayrickaby.com"
APP_NAME = "Run-7"

class Application(QObject):
    def __init__(self, parent=None):
        super().__init__(parent)

        base = Path(__file__).parent

        if (base / "external").exists():
            self._external_path = base / "external"
            self._parent_path = base
        else:
            self._external_path = base.parent.parent / "external"
            self._parent_path = base
        self._default_title = "Run–7"

    def get_default_icon(self):
        return str(self._parent_path / "qml" / "assets" / "icons" / "icon.png")

    def get_default_title(self):
        return self._default_title

    @Property(str, constant=True)
    def default_icon(self):
        return str(self._parent_path / "qml" / "assets" / "icons" / "icon.png")

    @Property(str, constant=True)
    def default_title(self):
        return self._default_title

    @Property(QUrl, constant=True)
    def external_folder(self):
        return QUrl.fromLocalFile(str(self._external_path))

    @Property(QUrl, constant=True)
    def parent_path(self):
        return QUrl.fromLocalFile(self._parent_path)

    @Property(QUrl, constant=True)
    def project_root_folder(self):
        return QUrl.fromLocalFile((self._parent_path.parent.parent.absolute()))

application = Application()
