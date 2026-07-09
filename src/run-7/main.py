# This Python file uses the following encoding: utf-8
import sys
from pathlib import Path

from PySide6.QtGui import QGuiApplication, QIcon
from PySide6.QtQml import QQmlApplicationEngine
from PySide6.QtQml import qmlRegisterSingletonInstance

# This is NOT unused
from application import application, ORG_NAME, ORG_DOMAIN, APP_NAME
from settings import settings
from system import system

if __name__ == "__main__":
    app = QGuiApplication(sys.argv)
    app.setOrganizationName(ORG_NAME)
    app.setOrganizationDomain(ORG_DOMAIN)
    app.setApplicationName(APP_NAME)

    app.setWindowIcon(QIcon(settings.icon.toLocalFile()))
    app.setDesktopFileName("run-7")

    qmlRegisterSingletonInstance(type(application), "jayrickaby.run7.application", 1, 0, "Application", application)
    qmlRegisterSingletonInstance(type(settings), "jayrickaby.run7.settings", 1, 0, "Settings", settings)
    qmlRegisterSingletonInstance(type(system), "jayrickaby.run7.system", 1, 0, "System", system)

    engine = QQmlApplicationEngine()
    engine.addImportPath(application.parentPath.toLocalFile())
    engine.addImportPath(application.externalFolder.toLocalFile())
    engine.loadFromModule("qml", "Main")
    if not engine.rootObjects():
        sys.exit(-1)
    sys.exit(app.exec())
