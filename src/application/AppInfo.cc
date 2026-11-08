#include "AppInfo.h"

AppInfo::AppInfo(QObject* parent)
  : QObject(parent)
{}

QString AppInfo::getTitle() {
    return m_defaultTitle;
}
