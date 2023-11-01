# Clinic Manager(PyQt5 + Sqlite)

Intro: this app is for super tiny scale single doctor's clinic PC.

### on Linux

```bash
chmod +x install.sh  lang_pack_gen.sh  run.sh
./install.sh
./lang_pack_gen.sh
./run.sh
```

### on Windows

double click `configure.bat` and `install.bat lang_pack_gen.sh`


### UI XML File ->Python Script

```bash
pyside6-uic PatientInfoWindow.ui -o ui_PatientInfoWindow.py
pyside6-uic addNewPatientWindow.ui -o ui_addNewPatientWindow.py
pyside6-uic searchWindow.ui -o ui_searchWindow.py
pyside6-uic form.ui -o ui_form.py
```
