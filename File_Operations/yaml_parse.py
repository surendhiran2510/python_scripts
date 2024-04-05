import yaml
import os



def read_parameters (File_path):
    try:
        with open(rf"{File_path}", 'r') as f:
            config_data = yaml.load(f, Loader=yaml.FullLoader)
    except FileNotFoundError:
        print(f'File not found in file_path')
    except Exception as e:
        print(f'Exception {e}')
    if config_data is None:
        return None
    else:
        print(config_data['database'])
        name = config_data['database'].get('username')
        print(name)
    

if __name__ == '__main__':

    File_path = f"C:\\Users\\dell\OneDrive\\Documents\Python\\Scripts-Level-1\\config_files\\sample.yml"
    #print(os.path.basename(File_path))
    #print(File_path)
    #file_path = os.path.normpath(File_path)
    #print(file_path)
    read_parameters(File_path)