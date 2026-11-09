#ifndef RUN7_APPLICATION_HISTORY_H_
#define RUN7_APPLICATION_HISTORY_H_

#include <qqml.h>
#include <QQueue>
#include <QString>

class History : public QObject {
    Q_OBJECT
    Q_PROPERTY(int maxSize READ getMaxSize CONSTANT)
    Q_PROPERTY(QQueue<QString> items READ getItems)
    QML_SINGLETON
    QML_ELEMENT

public:
    explicit History(QObject* parent = nullptr);

    int getMaxSize();
    QQueue<QString> getItems();

public slots:
    QString dequeue();

    void enqueue(const QString& path);

private:
    const int m_defaultMaxSize {5};

    QQueue<QString> m_items;
};

#endif
