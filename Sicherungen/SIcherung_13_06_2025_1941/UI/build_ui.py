import subprocess
import os

# --- Konfiguration ---
ui_file = "UI/frm_main_window.ui"
py_file = "UI/frm_main_window.py"
correct_import = "import UI.icons_rc"
wrong_import = "import icons_rc"

# --- Schritt 1: .ui in .py konvertieren ---
print(f"🔧 Konvertiere {ui_file} -> {py_file}")
subprocess.run(["pyside6-uic", ui_file, "-o", py_file], check=True)

# --- Schritt 2: Import anpassen ---
with open(py_file, "r", encoding="utf-8") as f:
    content = f.read()

if wrong_import in content:
    print(f"🔄 Ersetze '{wrong_import}' mit '{correct_import}'")
    content = content.replace(wrong_import, correct_import)

    with open(py_file, "w", encoding="utf-8") as f:
        f.write(content)
    print("✅ Import angepasst.")
else:
    print("ℹ️ Kein falscher Import gefunden – nichts geändert.")

print("🎉 Fertig.")
