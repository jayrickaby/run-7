import os
import sys

from PySide6.QtGui import QGuiApplication, QIcon
from PySide6.QtQml import qmlRegisterSingletonInstance, QQmlApplicationEngine
from PySide6.QtQuickControls2 import QQuickStyle

from application import application, APP_NAME, ORG_DOMAIN, ORG_NAME
from settings import settings
from system import system

if __name__ == "__main__": 
    kde_qt_path = "/usr/lib64/qt6/"
    
    # Load KDE Theme
    # FIXME: This is not guaranteed to work, and is very hacky
    if not os.environ.get("QT_QUICK_CONTROLS_STYLE") and os.path.isdir(kde_qt_path):
        if not os.environ.get("QML2_IMPORT_PATH"):
            os.environ["QML2_IMPORT_PATH"] = kde_qt_path + "/qml/"

        if not os.environ.get("QT_PLUGIN_PATH"):
            os.environ["QT_PLUGIN_PATH"] = kde_qt_path + "/plugins/"

        QQuickStyle.setStyle("org.kde.desktop")

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

    engine.loadFromModule("qml", "Main")
    if not engine.rootObjects():
        sys.exit(-1)
    sys.exit(app.exec())
