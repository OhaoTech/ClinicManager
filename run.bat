pyside2-uic PatientInfoWindow.ui -o ui_PatientInfoWindow.py
pyside2-uic addNewPatientWindow.ui -o ui_addNewPatientWindow.py
pyside2-uic searchWindow.ui -o ui_searchWindow.py
pyside2-uic form.ui -o ui_form.py
lrelease-qt6 language.ts
python mainwindow.py
