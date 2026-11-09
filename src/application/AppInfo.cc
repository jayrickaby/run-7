#include "AppInfo.h"

AppInfo::AppInfo(QObject* parent)
  : QObject(parent)
{}

QString AppInfo::getIcon() {
    return m_defaultIcon;
}
QString AppInfo::getTitle() {
    return m_defaultTitle;
}
