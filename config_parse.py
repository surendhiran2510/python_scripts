import configparser

def update_config(config_file, section, option, new_value):
    config = configparser.ConfigParser()
    config.read(config_file)
    print(config.sections())

    if section in config:
        config[section][option] = new_value
        with open(config_file, 'w') as configfile:
            config.write(configfile)
        print(f"Updated {option} in section [{section}] to {new_value}")
    else:
        print(f"Section [{section}] not found in the configuration file.")

# Example usage
config_file_path = 'db.ini'  # Path to your configuration file
section_name = 'Release1'  # Name of the section in the configuration file
option_name = 'url'  # Name of the option you want to update
new_option_value = input("Enter the new value for option1: ")

update_config(config_file_path, section_name, option_name, new_option_value)
