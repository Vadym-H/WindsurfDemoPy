#!/usr/bin/env python3
"""
JSON User Filter
Filters JSON user data based on age.
"""

import sys
import os
import json

def filter_underage_users(json_data):
    """
    Filters JSON user data and returns users who are underage.
    
    Args:
        json_data (dict): JSON user data
    
    Returns:
        list: List of underage users
    """
    underage_users = []
    for user in json_data['users']:
        if user['age'] < 18:
            underage_users.append(user)
    return underage_users

def main():
    """
    Main function that handles user input and filters JSON user data.
    """
    # Step 1: Get the JSON file path from user input
    if len(sys.argv) > 1:
        file_path = sys.argv[1]
    else:
        # Default to users_db.json in the same directory as this script
        script_dir = os.path.dirname(os.path.abspath(__file__))
        file_path = os.path.join(script_dir, "users_db.json")
        print(f"Using default JSON file: {file_path}")
    
    # Step 2: Validate that the file exists
    if not os.path.exists(file_path):
        print(f"Error: File '{file_path}' does not exist.")
        return
    
    # Step 3: Read the JSON file
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            json_data = json.load(file)
    except json.JSONDecodeError as e:
        print(f"Error parsing JSON: {e}")
        return
    
    # Step 4: Filter underage users
    underage_users = filter_underage_users(json_data)
    
    # Step 5: Print the result
    if underage_users:
        print("Underage users:")
        for user in underage_users:
            print(user)
    else:
        print("No underage users found.")

if __name__ == "__main__":
    main()