#!/usr/bin/env python3
import os
import subprocess
import sys
import inquirer
import argparse
from .version import __version__

def find_files(extension, path):
    return [f for f in os.listdir(path) if f.endswith(extension)]

def open_with_xcode(file_path):
    subprocess.run(["open", "-a", "Xcode", file_path])

def interactive_select(files):
    try:
        questions = [
            inquirer.List('file',
                          message="Choose a file to open in Xcode 💾",
                          choices=files,
        )
        ]
        answer = inquirer.prompt(questions)
        if answer and 'file' in answer:
            return answer['file']
        else:
            return None
    except KeyboardInterrupt:
        print("\nExecution interrupted by user. Exiting. 👋")
        sys.exit(1)

def main():
    parser = argparse.ArgumentParser(description="Tool for interacting with Xcode projects. This tool makes it possible to select .xcodeproj or .xcworkspace files and open them in Xcode.",
                                     epilog="Example usage: xcodeo --project or xcodeo -w for workspaces.")
    
    parser.add_argument('path', type=str, 
                        help="Path to .xcodeproj/.xcworkspace files.")
    parser.add_argument('-p', '--project', action='store_true',
                        help="Open .xcodeproj files (default).")
    parser.add_argument('-w', '--workspace', action='store_true', 
                        help="Open .xcworkspace files.")
    parser.add_argument('-s', '--swiftpackage', action='store_true', 
                        help="Open .swiftpm files.")
    parser.add_argument('-v', '--version', action='version', version=f'xcodeo version {__version__}',
                        help="Show current version")
    
    args = parser.parse_args()

    # Default to .xcodeproj unless --workspace is specified
    if args.workspace:
        extension = ".xcworkspace"
    elif args.swiftpackage:
        extension = ".swiftpm"
    else:
        extension = ".xcodeproj"  # Default behavior

    print(f"\nOpening \033[1m\033[3m\033[38;2;245;131;146m{extension}\033[0m file(s) in Xcode. 🐛\n")
    files = find_files(extension, args.path)

    if len(files) == 0:
        print(f"\n\033[1m\033[3m\033[38;2;245;131;146m{extension}\033[0m file(s) not found. 🤕\n")
        sys.exit(1)
    elif len(files) == 1:
        open_with_xcode(files[0])
    else:
        selected_file = interactive_select(files)
        if selected_file:
            open_with_xcode(selected_file)
        else:
            print("No selection made.")
            sys.exit(1)

if __name__ == "__main__":
    main()
