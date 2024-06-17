import os


def find_string_in_files(main_folder, search_string):
    for root, dirs, files in os.walk(main_folder):
        for file in files:
            file_path = os.path.join(root, file)
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    for line_num, line in enumerate(f, 1):
                        if search_string in line:
                            print(f'Found "{search_string}" in file: {file_path}, line: {line_num}')
            except Exception as e:
                print(f'Error reading file {file_path}: {e}')

if __name__ == "__main__":
    main_folder = "Library"
    search_string = input("Enter the string to search for: ").strip()
    find_string_in_files(main_folder, search_string)
