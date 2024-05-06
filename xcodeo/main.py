#!/usr/bin/env python3
import os
import subprocess
import sys
import inquirer
import argparse

def find_files(extension, path):
    return [f for f in os.listdir(path) if f.endswith(extension)]

def open_with_xcode(file_path):
    subprocess.run(["open", "-a", "Xcode", file_path])

def interactive_select(files):
    questions = [
        inquirer.List('file',
                      message="Wähle eine Datei zum Öffnen",
                      choices=files,
        )
    ]
    answer = inquirer.prompt(questions)
    return answer['file']

def main():
    parser = argparse.ArgumentParser(description="Tool zur Interaktion mit Xcode-Projekten. Dieses Tool ermöglicht es, .xcodeproj oder .xcworkspace Dateien auszuwählen und in Xcode zu öffnen.",
                                     epilog="Beispielgebrauch: xcodeo --project oder xcodeo -w für workspaces.")
    
    parser.add_argument('path', type=str, 
                        help="Pfad zu den .xcodeproj/.xcworkspace Dateien.")
    parser.add_argument('-p', '--project', action='store_true',
                        help="Verarbeite .xcodeproj Dateien (standardmäßig).")
    parser.add_argument('-w', '--workspace', action='store_true', 
                        help="Verarbeite .xcworkspace Dateien.")
    parser.add_argument('-v', '--version', action='version', version='xcodeo version 0.0.4',
                        help="Display the version of the tool")
    
    args = parser.parse_args()

    # Default to .xcodeproj unless --workspace is specified
    if args.workspace:
        extension = ".xcworkspace"
    else:
        extension = ".xcodeproj"  # Default behavior

    print(f"Verarbeite Dateien mit der Endung: {extension}")
    files = find_files(extension, args.path)

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
    main()
