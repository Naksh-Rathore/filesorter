import os

def main():
    folder_name = r"C:\Users\yours\Desktop\yours"

    location_dict = {
        ".docx": r"C:\Users\kumar\Desktop\Word Files",
        ".xlsx": r"C:\Users\kumar\Desktop\Excel Files",
        ".pptx": r"C:\Users\kumar\Desktop\PowerPoint Files",
        ".txt": r"C:\Users\kumar\Desktop\Text Files",
    }

    try:
        for file in os.listdir(folder_name):
            file_path = os.path.join(folder_name, file)
            
            if os.path.isdir(file_path):
                continue

            file_type = os.path.splitext(file)[1]

            if file_type in location_dict and os.path.exists(location_dict[file_type]):
                folder = location_dict[file_type]
                destination_path = os.path.join(folder, file)
                
                os.replace(file_path, destination_path)
                print(f"Moved {file} to {folder}")
            else:
                print(f"No destination folder for {file} or folder does not exist.")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()