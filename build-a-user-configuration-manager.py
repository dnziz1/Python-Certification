def add_setting(setting, key_value):
    key, value = key_value 
    key = key.lower()
    value = value.lower()

    if key in setting:
        return f'Setting \'{key}\' already exists! Cannot add a new setting with this name.'
    
    setting[key] = value
    return f'Setting \'{key}\' added with value \'{value}\' successfully!'

def update_setting(setting, key_value):
    key, value = key_value
    key = key.lower()
    value = value.lower()

    if key in setting:
        setting[key] = value
        return f'Setting \'{key}\' updated to \'{value}\' successfully!'
    
    return f'Setting \'{key}\' does not exist! Cannot update a non-existing setting.'

def delete_setting(setting, key):
    key = key.lower()

    if key in setting:
        del setting[key]
        return f'Setting \'{key}\' deleted successfully!'
    return 'Setting not found!'

def view_settings(setting):
    if not setting:
        return 'No settings available.'
    
    result = 'Current User Settings:\n'

    for key, value in setting.items():            
        result += f'{key.capitalize()}: {value}\n'

    return result

test_settings = {
    'theme': 'dark',
    'font_size': 12
}
new_setting = ('language', 'English')
update_theme = ('theme', 'light')
del_theme = ('font_size')
update_set = add_setting(test_settings, new_setting)
change_theme = update_setting(test_settings, update_theme)
del_setting = delete_setting(test_settings, del_theme)
view = view_settings(test_settings)
print(change_theme)
print(del_setting)
print(view)
print(test_settings)
