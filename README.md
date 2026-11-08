# Run–7

![Logo](docs/assets/logo/logo_trans.png)

A recreation of Window 7's Run Application

## About this project
This is an accurate-as-possible recreation of Window 7's Run Application in QtQuick and C++. It is based on inspecting the original application's components with Inspect.exe, along with comparing screenshots pixel-by-pixel in GIMP.

Originally made for the Hackclub Program [Macondo](https://macondo.hackclub.com/), where it was built in QtQuick and Python.

## Features
- Multi-theme support.
- Running applications, opening websites and viewing files.
- A browse dialog to precisely choose an application.
- Reactive text based on the OS you are using.
- Run History showing the last 'n' items.
- A config to customise parts of the application.

## Gallery
![Preview_Main](docs/assets/previews/preview_mainwindow.png)
![Preview_Dialog](docs/assets/previews/preview_unknowndialog.png)

Screenshots taken in KDE, using [AeroThemePlasma](https://gitgud.io/aeroshell/atp/aerothemeplasma).

## Running
- Download the binary from the [latest release](https://github.com/jayrickaby/run-7/releases/latest), or [build it from source](#building-from-source).
- You may need to give executable permissions via `chmod +x ./run-7` in terminal, or by adjusting the properties in the right-click context menu.
- Double click the executable, or use `./run-7` in the terminal, to run.

Requirements: [Qt 6.12](https://doc.qt.io/qt-6/).


## Building from Source
```
git clone https://github.com/jayrickaby/run-7.git && cd run-7

# Run the build script
chmod +x ./build.sh && ./build.sh 

# Run the application
chmod +x ./build/run-7 && ./build/run-7 
```
Requirements: [qt6-base](https://archlinux.org/packages/extra/x86_64/qt6-base/).

## Disclaimer
This project is not affiliated with Microsoft.
