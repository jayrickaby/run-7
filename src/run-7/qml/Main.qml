import QtCore
import QtQuick
import QtQuick.Controls
import QtQuick.Dialogs
import QtQuick.Layouts

import frutiger7
import jayrickaby.run7.application 1.0
import jayrickaby.run7.settings 1.0
import jayrickaby.run7.system 1.0

ApplicationWindow {
    id: root

    readonly property url dirHome: StandardPaths.writableLocation(StandardPaths.HomeLocation)
    readonly property url dirAssets: Qt.resolvedUrl( Application.external_folder + "/frutiger7/" + "/assets/items/window/")
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
    title: qsTr(Settings.title)

    flags: Qt.Window | Qt.WindowTitleHint | Qt.WindowSystemMenuHint | Qt.WindowCloseButtonHint

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

                mipmap: true

                source: Settings.icon
            }
            Text {
                Layout.preferredWidth: 319
                Layout.preferredHeight: 41
                Layout.alignment: Qt.AlignTop

                text: `Type the name of a program, folder, document, or Internet resource, and ${System.os_name} will open it for you.`

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
                editable: true

                popup.closePolicy: Popup.NoAutoClose

                Layout.fillWidth: true
                Layout.preferredHeight: 23
                Layout.alignment: Qt.AlignTop
                Layout.rightMargin: 2

                Component.onCompleted: {
                    // Make sure current list is limited
                    let currentQueue = Array.from(Settings.url_history);

                    if (Settings.limit_history_size > -1) {
                        while (currentQueue.length > Settings.limit_history_size) {
                            currentQueue.pop();
                        }

                        Settings.set_url_history(currentQueue);
                    }

                    // Set model only after adjusting it
                    model = currentQueue;

                    if (model.length > 0) {
                        contentItem.text = model[0];
                    }
                }
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

                highlighted: true
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

            source: dirAssets + imgBackground
        }
    }

    FileDialog {
        id: browseDialog
        currentFolder: dirHome

        onAccepted: {
            let resolved = System.process_file_path(currentFile);
            comboBox.contentItem.text = "\"" + resolved + "\"";
        }
    }

    InstructionDialog {
        id: cantFindDialog
        title: comboBox.editText
        contentText: `${System.os_name} cannot find '${comboBox.editText}'. Make sure you typed the name correctly, and then try again.`
        instructionType: InstructionDialog.Critical

        buttons: DialogButtonBox.Ok

        onButtonClicked: (role) => {
            if (role === DialogButtonBox.AcceptRole) {
                cantFindDialog.close();
            }
        }
    }

    Action {
        id: runAction
        text: qsTr("OK")
        onTriggered: {
            let success = System.open_url(comboBox.editText)
            // TODO: Make this properly work. Should hide when cantFindDialog appears.
            // root.visible = false

            if (success) {
                let newUrl = comboBox.editText.trim();

                let currentQueue = Array.from(Settings.url_history);

                let existingIndex = currentQueue.indexOf(newUrl);

                if (existingIndex !== -1) {
                    currentQueue.splice(existingIndex, 1);
                }

                currentQueue.unshift(newUrl);

                if (Settings.limit_history_size > -1 && currentQueue.length > Settings.limit_history_size) {
                    currentQueue.pop();
                }

                Settings.set_url_history(currentQueue);

                root.close();
                return;
            }

            cantFindDialog.show();
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
        // TODO: Is there a better way to do this?
        shortcut: (browseDialog.visible || cantFindDialog.visible) ? "" : StandardKey.Cancel
        onTriggered: root.close()
    }

    onActiveChanged: { if (active) comboBox.selectAll(); }
}
