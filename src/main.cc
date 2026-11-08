#include <QGuiApplication>
#include <QQmlApplicationEngine>
#include <QQuickStyle>

int main(int argc, char *argv[]) {
    QGuiApplication app(argc, argv);

    if (qEnvironmentVariableIsEmpty("QT_QUICK_CONTROLS_STYLE")) {
        QQuickStyle::setStyle(QStringLiteral("org.kde.desktop"));
    }

    QQmlApplicationEngine engine;
    QObject::connect(
    &engine, &QQmlApplicationEngine::objectCreationFailed,
    &app, []() {
        QCoreApplication::exit(-1);
    },
    Qt::QueuedConnection
    );

    engine.loadFromModule("jayrickaby.run_7", "Main");

    return 0;
}
