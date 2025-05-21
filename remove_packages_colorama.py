#!/usr/bin/env python3
from typing import List, Set

def remove_package_names(file_path: str) -> None:
    """
    Reads class names from a file, removes package names, and checks for duplicates.
    Prints duplicates in red color to stdout using colorama for cross-platform support.
    """
    # Define variables for color output
    RED = '\033[91m'
    RESET = '\033[0m'
    
    try:
        # Try to import colorama for cross-platform colored output
        from colorama import init, Fore, Style
        init()  # Initialize colorama
        has_colorama = True
    except ImportError:
        print("Note: For colored output, install colorama: pip install colorama")
        has_colorama = False
    
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        return
    
    # Extract class names and remove package names
    class_names: List[str] = []
    for line in lines:
        # Skip empty lines
        if not line.strip():
            continue
            
        # Extract the class name part (after line number and whitespace)
        parts = line.strip().split('|')
        if len(parts) > 1:
            full_class_name = parts[1].strip()
        else:
            full_class_name = line.strip()
        
        # Remove package name (everything before the last dot)
        if '.' in full_class_name:
            class_name = full_class_name.split('.')[-1]
        else:
            class_name = full_class_name
            
        class_names.append(class_name)
    
    # Find duplicates
    seen: Set[str] = set()
    duplicates: Set[str] = set()
    
    for name in class_names:
        if name in seen:
            duplicates.add(name)
        else:
            seen.add(name)
    
    # Print results
    print(f"Total classes after removing package names: {len(class_names)}")
    
    if duplicates:
        print(f"\nFound {len(duplicates)} duplicate class names:")
        for duplicate in sorted(duplicates):
            # Count occurrences of each duplicate
            count = class_names.count(duplicate)
            
            # Print in red color using colorama if available
            if has_colorama:
                from colorama import Fore, Style  # Import inside the block to ensure it's defined
                print(f"{Fore.RED}{duplicate} (appears {count} times){Style.RESET_ALL}")
            else:
                # Fallback to ANSI escape codes
                print(f"{RED}{duplicate} (appears {count} times){RESET}")
    else:
        print("\nNo duplicates found.")

if __name__ == "__main__":
    import sys
    
    if len(sys.argv) > 1:
        file_path = sys.argv[1]
    else:
        file_path = "schemas.txt"
        
    remove_package_names(file_path)