# Run–7

<img src="https://github.com/jayrickaby/run_7/blob/master/src/run_7/assets/logo/logo_trans.png" />
A recreation of Window 7's Run Application


## About this project
This is an accurate-as-possible recreation of Window 7's Run Application in Qt Quick and Python. It is based on Inspecting the original application's components with Inspect.exe, extracting assets via msstyleeditor and Resource Hacker, along with comparing screenshots pixel-by-pixel in GIMP.

I made this in order to familiarise myself with creating a simple Qt Quick application. It taught me how to create windows and style them with a theme in QML, how to write a backend for more important function calls in Python, and bridging them together via slots and signals. It also helped me learn the standard structure of Python projects which are distributed, like specifying package managers, a pyproject.toml and a versioning system.

## Features
- Running applications, opening websites and viewing files.
- A browse dialog to precisely choose an application
- A recreation of Window 7's Aero theme for increased accuracy
- Reactive text based on the Operating System you are using
- ~~Run History~~ (TODO)
- ~~A config to customise parts of the application~~ (TODO)

## Gallery
<img width="447" height="246" alt="image" src="https://github.com/user-attachments/assets/a64b1950-b816-4066-808f-5331c6f4d7ec" />
<img width="555" height="165" alt="image" src="https://github.com/user-attachments/assets/cf5aff27-e8e7-4724-8236-3cd8c301f2e2" />

## Setup
```
git clone https://github.com/jayrickaby/run_7.git && cd run_7
git submodule update --init --recursive
uv run src/run_7/main.py
```
Requirements: [uv](https://docs.astral.sh/uv/)

On KDE Plasma, you can make the Window more accurate by appling a Window Rule, such as:

<img width="332" height="179" alt="image" src="https://github.com/user-attachments/assets/631e606b-6563-40aa-90a1-e9b829ed9739" />


## Disclaimer
Microsoft® Windows™ is a registered trademark of Microsoft® Corporation. This name is used for referential use only, and does not aim to usurp copyrights from Microsoft. Microsoft Ⓒ 2026 All rights reserved. All resources belong to Microsoft Corporation.
