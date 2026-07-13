# Run–7

![Logo](docs/assets/logo/logo_trans.png)

A recreation of Window 7's Run Application

## About this project
This is an accurate-as-possible recreation of Window 7's Run Application in Qt Quick and Python. It is based on Inspecting the original application's components with Inspect.exe, extracting assets via msstyleeditor and Resource Hacker, along with comparing screenshots pixel-by-pixel in GIMP.

I made this in order to familiarise myself with creating a simple Qt Quick application. It taught me how to create windows and style them with a theme in QML, how to write a backend for more important function calls in Python, and bridging them together via slots and signals. It also helped me learn the standard structure of Python projects which are distributed, like specifying package managers, a pyproject.toml and a versioning system.

## Features
- Running applications, opening websites and viewing files
- A browse dialog to precisely choose an application
- A recreation of Window 7's Aero theme for increased accuracy
- Reactive text based on the OS you are using
- Run History showing the last 'n' items
- A config to customise parts of the application

## Gallery
![Preview_Main](docs/assets/previews/preview_mainwindow.png)
![Preview_Dialog](docs/assets/previews/preview_unknowndialog.png)

## Setup
```
git clone https://github.com/jayrickaby/run-7.git && cd run-7
git submodule update --init --recursive
uv run src/run-7/main.py
```
Requirements: [uv](https://docs.astral.sh/uv/)

## Disclaimer
Microsoft® Windows™ is a registered trademark of Microsoft® Corporation. This name is used for referential use only, and does not aim to usurp copyrights from Microsoft. Microsoft Ⓒ 2026 All rights reserved. All resources belong to Microsoft Corporation.
