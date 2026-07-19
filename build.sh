#!/usr/bin/env bash
set -euo pipefail

python -m nuitka src/run-7/main.py \
  --follow-imports \
  --enable-plugin=pyside6 \
  --output-dir=dist \
  --output-filename=run-7 \
  --onefile \
  --include-data-dir=src/run-7/qml=qml \
  --include-data-dir=external=external \
  --noinclude-dlls=libQt6Charts* \
  --noinclude-dlls=libQt6Quick3D* \
  --noinclude-dlls=libQt6Sensors* \
  --noinclude-dlls=libQt6Test* \
  --noinclude-dlls=libQt6WebEngine* \
  --noinclude-dlls=*assetdownloader* \
  --linux-icon=src/run-7/qml/assets/icons/icon.png \
  --include-qt-plugins=networkinformation,platforminputcontexts,qml,qmllint,qmltooling,vectorimageformats \
  --noinclude-qt-translations
