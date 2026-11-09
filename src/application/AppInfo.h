#ifndef RUN7_APPLICATION_APPINFO_H_
#define RUN7_APPLICATION_APPINFO_H_

#include <qqml.h>

class AppInfo : public QObject {
    Q_OBJECT
    Q_PROPERTY(QString icon READ getIcon CONSTANT)
    Q_PROPERTY(QString title READ getTitle CONSTANT)
    QML_SINGLETON
    QML_ELEMENT

public:
    explicit AppInfo(QObject* parent = nullptr);

    QString getIcon();
    QString getTitle();

private:
    const QString m_defaultIcon {"qrc:/jayrickaby/run_7/assets/icons/icon.png"};
    const QString m_defaultTitle {"Run–7"};
};

#endif
