#!/opt/homebrew/bin/python3
import os
import subprocess
import sys
import inquirer

def find_files(extension):
    return [f for f in os.listdir('.') if f.endswith(extension)]

def open_with_xcode(file_path):
    subprocess.run(["open", "-a", "Xcode", file_path])

def interactive_select(files):
    questions = [
        inquirer.List('file',
                      message="Wähle eine Datei zum Öffnen",
                      choices=files,
        )
    ]
    answer = inquirer.prompt(questions)
    return answer['file']

def main(extension):
    files = find_files(extension)

    if len(files) == 0:
        print(f"Keine {extension} Dateien gefunden.")
        sys.exit(1)
    elif len(files) == 1:
        open_with_xcode(files[0])
    else:
        selected_file = interactive_select(files)
        if selected_file:
            open_with_xcode(selected_file)
        else:
            print("Keine Auswahl getroffen.")
            sys.exit(1)

if __name__ == "__main__":
    extension = ".xcodeproj" if len(sys.argv) < 2 or sys.argv[1] != "w" else ".xcworkspace"
    main(extension)