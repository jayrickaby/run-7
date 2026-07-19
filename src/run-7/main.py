import sys

from PySide6.QtGui import QGuiApplication, QIcon
from PySide6.QtQml import qmlRegisterSingletonInstance, QQmlApplicationEngine

from application import application, APP_NAME, ORG_DOMAIN, ORG_NAME
from settings import settings
from system import system

if __name__ == "__main__":
    app = QGuiApplication(sys.argv)
    app.setApplicationName(APP_NAME)
    app.setOrganizationDomain(ORG_DOMAIN)
    app.setOrganizationName(ORG_NAME)

    app.setDesktopFileName("run-7")
    app.setWindowIcon(QIcon(settings.get_icon().toLocalFile()))

    qmlRegisterSingletonInstance(
        type(application), "jayrickaby.run7.application",
        1, 0,
        "Application", application
    )
    qmlRegisterSingletonInstance(
        type(settings), "jayrickaby.run7.settings",
        1, 0,
        "Settings", settings
    )
    qmlRegisterSingletonInstance(
        type(system), "jayrickaby.run7.system",
        1, 0,
        "System", system
    )

    engine = QQmlApplicationEngine()
    engine.addImportPath(application.parent_path.toLocalFile())
    engine.addImportPath(application.external_folder.toLocalFile())
    engine.loadFromModule("qml", "Main")
    if not engine.rootObjects():
        sys.exit(-1)
    sys.exit(app.exec())
