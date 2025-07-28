#!/usr/bin/env python3
"""
Simple Text File Processor
Reads a text file and counts the number of words in it.
"""

import sys
import os

def count_words_in_file(file_path):
    """
    Reads a text file and counts the number of words.
    
    Args:
        file_path (str): Path to the text file
    
    Returns:
        int: Number of words in the file
    """
    try:
        # Step 1: Open and read the file content
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
        
        # Step 2: Split the content into words and count them
        # This removes extra whitespace and splits on any whitespace character
        words = content.split()
        word_count = len(words)
        
        return word_count
    
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        return None
    except PermissionError:
        print(f"Error: Permission denied to read '{file_path}'.")
        return None
    except Exception as e:
        print(f"Error reading file: {e}")
        return None

def main():
    """
    Main function that handles user input and processes the file.
    """
    # Step 1: Get the file path from user input
    if len(sys.argv) > 1:
        # If file path is provided as command line argument
        file_path = sys.argv[1]
    else:
        # If no argument provided, ask user for input
        file_path = input("Enter the path to the text file: ").strip()
    
    # Step 2: Validate that the file exists
    if not os.path.exists(file_path):
        print(f"Error: File '{file_path}' does not exist.")
        return
    
    # Step 3: Process the file and count words
    print(f"Processing file: {file_path}")
    word_count = count_words_in_file(file_path)
    
    # Step 4: Print the result
    if word_count is not None:
        print(f"Number of words in the file: {word_count}")
    else:
        print("Failed to process the file.")

if __name__ == "__main__":
    main()
