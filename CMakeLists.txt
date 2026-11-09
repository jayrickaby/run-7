cmake_minimum_required(VERSION 3.16)

project(run-7 VERSION 0.8.0 LANGUAGES CXX)

set(CMAKE_CXX_STANDARD 20)

find_package(Qt6 REQUIRED COMPONENTS
        Qml
        Quick
        QuickControls2
        Widgets
)

qt_standard_project_setup(REQUIRES 6.12.0)

add_executable(run-7 
    src/main.cc
    src/application/AppInfo.cc
    src/application/AppInfo.h
    src/application/History.cc
    src/application/History.h
)

qt_add_qml_module(run-7
        URI jayrickaby.run_7
        RESOURCE_PREFIX /
        QML_FILES
            qml/Main.qml
        RESOURCES
            assets/icons/icon.png
)

target_include_directories(run-7 PRIVATE
        ${CMAKE_CURRENT_SOURCE_DIR}/src
        ${CMAKE_CURRENT_SOURCE_DIR}/src/application
)

# Qt for iOS sets MACOSX_BUNDLE_GUI_IDENTIFIER automatically since Qt 6.1.
# If you are developing for iOS or macOS you should consider setting an
# explicit, fixed bundle identifier manually though.
set_target_properties(run-7 PROPERTIES
        #    MACOSX_BUNDLE_GUI_IDENTIFIER jayrickaby.run-7
        MACOSX_BUNDLE_BUNDLE_VERSION ${PROJECT_VERSION}
        MACOSX_BUNDLE_SHORT_VERSION_STRING ${PROJECT_VERSION_MAJOR}.${PROJECT_VERSION_MINOR}
        MACOSX_BUNDLE TRUE
        WIN32_EXECUTABLE TRUE
)

target_link_libraries(run-7
        PRIVATE Qt6::Qml
        PRIVATE Qt6::Quick
        PRIVATE Qt6::QuickControls2
)

install(TARGETS run-7
        BUNDLE DESTINATION .
        LIBRARY DESTINATION ${CMAKE_INSTALL_LIBDIR}
        RUNTIME DESTINATION ${CMAKE_INSTALL_BINDIR}
)
