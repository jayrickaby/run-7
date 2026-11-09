#include "History.h"

History::History(QObject* parent)
  : QObject(parent)
{}

int History::getMaxSize() {
    return m_defaultMaxSize;
}
