!include "MUI2.nsh"
!include "x64.nsh"

Name "Kapusta Installer"
OutFile "Kapusta_Installer_Windows.exe"
Icon "icon.ico"
Unicode True
InstallDir "$PROGRAMFILES64\Kapusta"
InstallDirRegKey HKCU "Software\Kapusta" ""
RequestExecutionLevel admin
!define INSTALLSIZE 243498
!define MUI_ABORTWARNING
!insertmacro MUI_PAGE_LICENSE "LICENSE"
!insertmacro MUI_PAGE_COMPONENTS
!insertmacro MUI_PAGE_DIRECTORY
!insertmacro MUI_PAGE_INSTFILES
!insertmacro MUI_UNPAGE_CONFIRM
!insertmacro MUI_UNPAGE_INSTFILES
!insertmacro MUI_LANGUAGE "English"

Section "Kapusta" MainInstall
    SectionIn RO
    SetOutPath "$INSTDIR"
    File /r "dist\Kapusta\*"
    WriteRegStr HKCU "Software\Kapusta" "" $INSTDIR
    WriteUninstaller "$INSTDIR\Uninstall.exe"
    WriteRegStr HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\Kapusta" "DisplayName" "Kapusta"
    WriteRegStr HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\Kapusta" "UninstallString" "$\"$INSTDIR\uninstall.exe$\""
	WriteRegStr HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\Kapusta" "QuietUninstallString" "$\"$INSTDIR\uninstall.exe$\" /S"
	WriteRegStr HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\Kapusta" "InstallLocation" "$\"$INSTDIR$\""
	WriteRegStr HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\Kapusta" "DisplayIcon" "$\"$INSTDIR\icon.ico$\""
	WriteRegStr HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\Kapusta" "Publisher" "Kapustniaci"
	WriteRegStr HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\Kapusta" "HelpLink" "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
	WriteRegStr HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\Kapusta" "URLUpdateInfo" "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
	WriteRegStr HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\Kapusta" "URLInfoAbout" "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
	WriteRegStr HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\Kapusta" "DisplayVersion" "1.0.0"
	WriteRegDWORD HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\Kapusta" "VersionMajor" 1
	WriteRegDWORD HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\Kapusta" "VersionMinor" 0
	WriteRegDWORD HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\Kapusta" "NoModify" 1
	WriteRegDWORD HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\Kapusta" "NoRepair" 1
	WriteRegDWORD HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\Kapusta" "EstimatedSize" ${INSTALLSIZE}
SectionEnd

Section "Uninstall"
    SetShellVarContext all
    Delete "$SMPROGRAMS\Kapusta.lnk"
    Delete "$DESKTOP\Kapusta.lnk"
    Delete "$INSTDIR\Uninstall.exe"
    RMDir /r "$INSTDIR"
    DeleteRegKey HKCU "Software\Kapusta"
    DeleteRegKey HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\Kapusta"
SectionEnd

Section "Desktop Shortcut" DesktopShortcut
    SetShellVarContext all
    CreateShortCut "$DESKTOP\Kapusta.lnk" "$INSTDIR\Kapusta.exe"
SectionEnd

Section "Start Menu" StartMen
    SetShellVarContext all
    CreateShortCut "$SMPROGRAMS\Kapusta.lnk" "$INSTDIR\Kapusta.exe"
SectionEnd
