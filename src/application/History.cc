#include "History.h"

History::History(QObject* parent)
  : QObject(parent)
{
    m_items.reserve(getMaxSize());
}


int History::getMaxSize() {
    return m_defaultMaxSize;
}

QQueue<QString> History::getItems() {
    return m_items;
}

QString History::dequeue() {
    if (m_items.isEmpty()) {
        return {};
    }

    return m_items.dequeue();
}

void History::enqueue(const QString& path) {
    if (m_items.size() == getMaxSize()) {
        return;
    }

    m_items.enqueue(path);
}
