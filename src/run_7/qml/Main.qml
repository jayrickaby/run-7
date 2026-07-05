import QtCore
import QtQuick
import QtQuick.Controls
import QtQuick.Dialogs
import QtQuick.Layouts

import frutiger7
import jayrickaby.run7.app 1.0
import jayrickaby.run7.system 1.0

ApplicationWindow {
    id: root

    Application {
        id: pyApplication
    }

    System {
        id: pySystem
    }

    readonly property url dirHome: StandardPaths.writableLocation(StandardPaths.HomeLocation)
    readonly property url dirAssets: Qt.resolvedUrl( pyApplication.externalFolder + "/frutiger7/" + "/assets/items/window/")
    readonly property string imgBackground: "background.png"

    property alias comboBox : comboBox
    property alias browseDialog : browseDialog

    width: 397
    height: 174

    minimumWidth: width
    minimumHeight: height
    maximumWidth: width
    maximumHeight: height

    visible: true
    title: qsTr(pyApplication.currentTitle)

    flags: Qt.Window | Qt.WindowCloseButtonHint

    topPadding: 20
    bottomPadding: 20
    leftPadding: 12
    rightPadding: 12

    ColumnLayout {
        anchors.fill: parent
        spacing: 0

        RowLayout {
            Layout.alignment: Qt.AlignTop
            Layout.fillWidth: true
            Layout.bottomMargin: -15
            spacing: 19

            Image {
                Layout.preferredWidth: 32
                Layout.preferredHeight: 32
                Layout.topMargin: 2
                Layout.alignment: Qt.AlignTop

                source: pyApplication.icon
            }
            Text {
                Layout.preferredWidth: 319
                Layout.preferredHeight: 41
                Layout.alignment: Qt.AlignTop

                text: `Type the name of a program, folder, document, or Internet resource, and ${pySystem.simpleOsName} will open it for you.`

                font.letterSpacing: 0.10
                font.pointSize: 9

                lineHeight: 0.95
                renderType: Text.NativeRendering
                wrapMode: Text.WordWrap
            }
        }
        RowLayout {
            Layout.alignment: Qt.AlignTop
            Layout.fillWidth: true

            spacing:9

            Text {
                Layout.preferredWidth: 42
                Layout.preferredHeight: 19
                Layout.alignment: Qt.AlignTop
                Layout.topMargin: 3
                text: "Open:"

                font.pointSize: 9
                renderType: Text.NativeRendering
            }
            ComboBox {
                id: comboBox

                Layout.fillWidth: true
                Layout.preferredHeight: 23
                Layout.alignment: Qt.AlignTop
                Layout.rightMargin: 2

                editable: true
            }
        }
        RowLayout {
            Layout.alignment: Qt.AlignBottom | Qt.AlignRight
            Layout.bottomMargin: -2
            Layout.fillWidth: true

            spacing: 8
            Button {
                action: runAction
                Layout.preferredHeight: 24
                Layout.preferredWidth: 86

                enabled: comboBox.editText !== ""

                textVCenterOffset: -2
            }
            Button {
                action: closeAction
                Layout.rightMargin: 1
                Layout.preferredHeight: 24
                Layout.preferredWidth: 86

                textVCenterOffset: -2
            }
            Button {
                action: browseAction
                Layout.preferredHeight: 24
                Layout.preferredWidth: 86

                textVCenterOffset: -2
            }
        }
    }

    background: ColumnLayout{
        BorderImage {
            Layout.alignment: Qt.AlignTop
            Layout.fillWidth: true
            Layout.preferredHeight: 114

            border.left: 1
            border.right: 1
            border.top: 1
            border.bottom: 1

            horizontalTileMode: BorderImage.Repeat
            verticalTileMode: BorderImage.Repeat

            // Swap the image asset depending on whether the button is hovered or pressed
            source: dirAssets + imgBackground

        }
    }

    FileDialog {
        id: browseDialog
        currentFolder: dirHome
        onAccepted: {
            let resolved = Qt.resolvedUrl(currentFile)
            comboBox.contentItem.text = "\"" + new URL(resolved).pathname + "\""
        }
    }

    InstructionDialog {
        id: cantFindDialog
        // buttons: MessageDialog.Ok
        contentText: `${pySystem.simpleOsName} cannot find '${comboBox.editText}'. Make sure you typed the name correctly, and then try again.`
        // contentText: `Windows cannot find '${comboBox.editText}'. Make sure you typed the name correctly, and then try again.`
        title: comboBox.editText

        // icon: MessageDialog.Critical

        // onAccepted: root.visible = true
    }

    Action {
        id: runAction
        text: qsTr("OK")
        onTriggered: {
            let success = pySystem.openUrl(comboBox.editText)
            // TODO: Make this properly work. Should hide when cantFindDialog appears.
            // root.visible = false

            success ? root.close() : cantFindDialog.show()
        }
    }

    Action {
        id: browseAction
        text: qsTr("Browse...")
        shortcut: "ALT+B"
        onTriggered: browseDialog.open()
    }

    Action {
        id: closeAction
        text: qsTr("Cancel")
        shortcut: StandardKey.Cancel
        onTriggered: root.close()
    }
}
