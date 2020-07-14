# Import libraries
import argparse
import os

def run():
    """
    A tool generate tint or shade in HEX of the given color

    Parameters:
    -----------

    Returns:
    --------

    Raises:
    -------
    """

    # Parser arguments
    parser = argparse.ArgumentParser()
    parser.add_argument('-m', '--mode', default='shade', help='Choose generation mode between tint or shade. Default: shade')
    parser.add_argument('-i', '--input', required=True, help='Input HEX color')
    parser.add_argument('-o', '--output', help='Output directory. Default: $HOME/.colors')

    arg = parser.parse_args()

    mode = arg.mode
    in_color = arg.input
    out_dir = arg.output

    # Pass the default setting
    if mode == '':
        mode = 'shade'

    if out_dir == '':
        out_dir = '/.colors/'

    # Check output directory
    home = os.path.expanduser('~')
    out_path = home + out_dir

    # Create new folder if output directory not exists
    if os.path.exists(out_path):
        print('Output directory not found')
        print('Create new directory {0}'.format(out_path))
        os.chdir(home)
        os.mkdir(out_dir)

    # hex2rgb
    hex_color = in_color.lstrip('#')
    rgb = []
    for i in (0, 2, 4):
        rgb.append(int(hex_color[i:i+2], 16))

    # Define Factor
    factor = 0.25
    current_r = rgb[0]
    current_g = rgb[1]
    current_b = rgb[2]

    # Shade mode
    new_r = int(round(current_r*(1-factor)))
    new_g = int(round(current_g*(1-factor)))
    new_b = int(round(current_b*(1-factor)))

    # Tint mode
    new_r = int(round(current_r + (255 - current_r)*factor))
    new_g = int(round(current_g + (255 - current_g)*factor))
    new_b = int(round(current_b + (255 - current_b)*factor))

    # rgb2hex
    new_hex = f'#{new_r:02x}{new_g:02x}{new_b:02x}'

    # Save result file
    os.chdir(out_path)
    if mode == 'tint':
        with open('tint', 'w') as file:
            file.write("shade='{0}'".format(new_hex))
    else:
        with open('shade', 'w') as file:
            file.write(new_hex)
