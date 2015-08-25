; Script generated by the HM NIS Edit Script Wizard.

SetCompressor /FINAL /SOLID lzma
SetCompressorDictSize 64

!define MULTIUSER_EXECUTIONLEVEL "Admin"
!include MultiUser.nsh

; HM NIS Edit Wizard helper defines
!define PRODUCT_NAME "OdemisViewer"
; Product version is defined through the command line!
!ifndef PRODUCT_VERSION
    !define PRODUCT_VERSION "2.1"
!endif
!define PRODUCT_PUBLISHER "Elit"
!define PRODUCT_WEB_SITE "http://www.delmic.com"
!define PRODUCT_DIR_REGKEY "Software\Microsoft\Windows\CurrentVersion\App Paths\${PRODUCT_NAME}.exe"
!define PRODUCT_UNINST_KEY "Software\Microsoft\Windows\CurrentVersion\Uninstall\${PRODUCT_NAME}"
!define PRODUCT_UNINST_ROOT_KEY "HKLM"
!define PRODUCT_EXECUTABLE "${PRODUCT_NAME}.exe"

; MUI 1.8 compatible ------
!include "MUI.nsh"

; MUI Settings
!define MUI_ABORTWARNING
;;;;;!define MUI_ICON "fabrixkassa\gui\img\fabrixinstall.ico"
!define MUI_UNICON "${NSISDIR}\Contrib\Graphics\Icons\modern-uninstall.ico"
!define MUI_WELCOMEFINISHPAGE_BITMAP "..\image\install.bmp"

; Welcome page
!insertmacro MUI_PAGE_WELCOME
!define MUI_TEXT_WELCOME_INFO_TITLE "$(^NameDA) installation"
; Directory page
!insertmacro MUI_PAGE_DIRECTORY
; Instfiles page
!define MUI_FINISHPAGE_NOAUTOCLOSE
!insertmacro MUI_PAGE_INSTFILES
; Finish page
!define MUI_FINISHPAGE_RUN "$INSTDIR\fabrixkassa.exe"
!insertmacro MUI_PAGE_FINISH

; Uninstaller pages
!insertmacro MUI_UNPAGE_INSTFILES

; Language files
!insertmacro MUI_LANGUAGE "English"

; MUI end ------

Name "${PRODUCT_NAME} ${PRODUCT_VERSION}"
OutFile "dist/OdemisViewer-${PRODUCT_VERSION}.exe"
InstallDir "$PROGRAMFILES\OdemisViewer"
InstallDirRegKey HKLM "${PRODUCT_DIR_REGKEY}" ""
ShowInstDetails show
ShowUnInstDetails show

Section "MainSection" SEC01
  SetOutPath "$APPDATA\OdemisViewer"
  SetOutPath "$INSTDIR"
  File /r .\dist\OdemisViewer\*.*
  CreateDirectory "$SMPROGRAMS\Odemis Viewer"
  CreateShortCut "$SMPROGRAMS\Odemis Viewer\Odemis Viewer.lnk" "$INSTDIR\OdemisViewer.exe"
  CreateShortCut "$DESKTOP\Odemis Viewer.lnk" "$INSTDIR\OdemisViewer.exe"
SectionEnd

Section -AdditionalIcons
  WriteIniStr "$INSTDIR\${PRODUCT_NAME}.url" "InternetShortcut" "URL" "${PRODUCT_WEB_SITE}"
  CreateShortCut "$SMPROGRAMS\Odemis Viewer\Website.lnk" "$INSTDIR\${PRODUCT_NAME}.url"
  CreateShortCut "$SMPROGRAMS\Odemis Viewer\Uninstall.lnk" "$INSTDIR\uninst.exe"
SectionEnd

Section -Post
  WriteUninstaller "$INSTDIR\uninst.exe"
  WriteRegStr HKLM "${PRODUCT_DIR_REGKEY}" "" "$INSTDIR\w9xpopen.exe"
  WriteRegStr ${PRODUCT_UNINST_ROOT_KEY} "${PRODUCT_UNINST_KEY}" "DisplayName" "$(^Name)"
  WriteRegStr ${PRODUCT_UNINST_ROOT_KEY} "${PRODUCT_UNINST_KEY}" "UninstallString" "$INSTDIR\uninst.exe"
  WriteRegStr ${PRODUCT_UNINST_ROOT_KEY} "${PRODUCT_UNINST_KEY}" "DisplayIcon" "$INSTDIR\fabrixkassa.exe"
  WriteRegStr ${PRODUCT_UNINST_ROOT_KEY} "${PRODUCT_UNINST_KEY}" "DisplayVersion" "${PRODUCT_VERSION}"
  WriteRegStr ${PRODUCT_UNINST_ROOT_KEY} "${PRODUCT_UNINST_KEY}" "URLInfoAbout" "${PRODUCT_WEB_SITE}"
  WriteRegStr ${PRODUCT_UNINST_ROOT_KEY} "${PRODUCT_UNINST_KEY}" "Publisher" "${PRODUCT_PUBLISHER}"
SectionEnd


Function un.onUninstSuccess
  HideWindow
  MessageBox MB_ICONINFORMATION|MB_OK "$(^Name) successfully removed."
FunctionEnd

Function .onInit
  !insertmacro MULTIUSER_INIT

  ; http://nsis.sourceforge.net/KillProc_plug-in
  StrCpy $0 ${PRODUCT_EXECUTABLE}
  KillProc::FindProcesses

  StrCmp $1 "-1" wooops     ; Error occured
  StrCmp $0 "0" completed   ; None found, so done
  Sleep 1500

  StrCpy $0 ${PRODUCT_EXECUTABLE}
  KillProc::KillProcesses

  StrCmp $1 "-1" wooops     ; Error during kill
  Goto completed            ; Kill done

  wooops:
  MessageBox MB_OK|MB_ICONEXCLAMATION "Error while stopping Odemis Viewer" /SD IDOK
  Abort

  completed:
  DetailPrint "Done."
FunctionEnd

Function un.onInit
  !insertmacro MULTIUSER_UNINIT
  MessageBox MB_ICONQUESTION|MB_YESNO|MB_DEFBUTTON2 "Weet u zeker dat u $(^Name) wilt verwijderen?" IDYES +2
  Abort
FunctionEnd

Section Uninstall
  Delete "$SMPROGRAMS\Odemis Viewer\Uninstall.lnk"
  Delete "$SMPROGRAMS\Odemis Viewer\Website.lnk"
  Delete "$DESKTOP\Odemis Viewer.lnk"
  Delete "$SMPROGRAMS\Odemis Viewer\\Odemis Viewer.lnk"

  RMDir /r "$SMPROGRAMS\Odemis Viewer"
  RMDir /r "$INSTDIR"

  DeleteRegKey ${PRODUCT_UNINST_ROOT_KEY} "${PRODUCT_UNINST_KEY}"
  DeleteRegKey HKLM "${PRODUCT_DIR_REGKEY}"
  SetAutoClose true
SectionEnd
