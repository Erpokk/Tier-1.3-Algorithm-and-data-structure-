
import os 
import shutil
import argparse

def recursive_copy(source_dir, destination_dir):
    try:
        os.makedirs(destination_dir, exist_ok=True)
        for item in os.listdir(source_dir):
            source_item = os.path.join(source_dir,item)
            destination_item=os.path.join(destination_dir,item) 
            if os.path.isdir(source_item):
                recursive_copy(source_item, destination_item)
            else:
                file_extension = os.path.splitext(item)[1]
                file_extension = file_extension.strip(".").lower()
                file_destintation_dir = os.path.join(destination_dir,file_extension)
                os.makedirs(file_destintation_dir, exist_ok=True)
                shutil.copy2(source_item, file_destintation_dir)
    except Exception as e:
        print(f"An error occured {e}")

def main():
    parser = argparse.ArgumentParser(description="Recursively copy files and sort them by extension.")
    parser.add_argument("source_dir", help="Source directory path" )
    parser.add_argument("destination_dir",  nargs='?', default='dist', help="Destination directory path (default: 'dist')")
    args = parser.parse_args()
    recursive_copy(args.source_dir, args.destination_dir)

if __name__ == "__main__":
    main()