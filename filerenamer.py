import os

# function to remove end part of filename
def remove_end_part(filename):
    name, ext = os.path.splitext(filename)
    if ext not in ('.txt', '.py'):
        name_parts = name.split('_')
        if len(name_parts) > 2:
            new_name = '_'.join(name_parts[:2]) + ext
        else:
            new_name = name + ext
        return new_name
    else:
        return filename

# create input and output directories if they don't exist
if not os.path.exists('input'):
    os.mkdir('input')
if not os.path.exists('output'):
    os.mkdir('output')

# process files in input directory
for filename in os.listdir('input'):
    if os.path.isfile(os.path.join('input', filename)):
        new_filename = remove_end_part(filename)
        if new_filename != filename:
            os.rename(os.path.join('input', filename), os.path.join('output', new_filename))
            print(f'Renamed file "{filename}" to "{new_filename}" and moved to "output" folder.')
