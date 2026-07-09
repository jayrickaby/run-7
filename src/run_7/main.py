# This Python file uses the following encoding: utf-8
import sys
from pathlib import Path

from PySide6.QtGui import QGuiApplication, QIcon
from PySide6.QtQml import QQmlApplicationEngine

# This is NOT unused
import application
import system

if __name__ == "__main__":
    application = application.Application()

    app = QGuiApplication(sys.argv)
    app.setWindowIcon(QIcon(application.icon.toLocalFile()))
    app.setDesktopFileName("run_7")

    app.setOrganizationName("JayRickaby")
    app.setOrganizationDomain("jayrickaby.com")
    app.setApplicationName("Run-7")

    engine = QQmlApplicationEngine()
    engine.addImportPath(application.parentPath.toLocalFile())
    engine.addImportPath(application.externalFolder.toLocalFile())
    engine.loadFromModule("qml", "Main")
    if not engine.rootObjects():
        sys.exit(-1)
    sys.exit(app.exec())
