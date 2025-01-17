import os
import argparse

def rename_files(directory, prefix, start_num=1, include_folders=False):
    try:
        items = os.listdir(directory)
        items.sort()  # Sort items to maintain order
        num = start_num
        
        for item in items:
            item_path = os.path.join(directory, item)
            if os.path.isfile(item_path) or (include_folders and os.path.isdir(item_path)):
                file_extension = os.path.splitext(item)[1] if os.path.isfile(item_path) else ''
                new_name = f"{prefix}_{num}{file_extension}"
                new_path = os.path.join(directory, new_name)
                os.rename(item_path, new_path)
                print(f"Renamed: {item} -> {new_name}")
                num += 1
    
    except Exception as e:
        print(f"An error occurred: {e}")

def main():
    parser = argparse.ArgumentParser(description='Batch rename files and folders.')
    parser.add_argument('directory', type=str, help='The directory containing files to rename.')
    parser.add_argument('prefix', type=str, help='The prefix for the renamed files.')
    parser.add_argument('-s', '--start', type=int, default=1, help='The starting number for the renaming sequence.')
    parser.add_argument('-f', '--folders', action='store_true', help='Include folders in the renaming process.')
    
    args = parser.parse_args()
    
    rename_files(args.directory, args.prefix, args.start, args.folders)

if __name__ == '__main__':
    main()