#ifndef RUN7_APPLICATION_HISTORY_H_
#define RUN7_APPLICATION_HISTORY_H_

#include <qqml.h>

class History : public QObject {
    Q_OBJECT
    Q_PROPERTY(int maxSize READ getMaxSize CONSTANT)
    QML_SINGLETON
    QML_ELEMENT

public:
    explicit History(QObject* parent = nullptr);
    int getMaxSize();

private:
    const int m_defaultMaxSize {5};
};

#endif
