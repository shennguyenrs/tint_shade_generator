# Import libraries
import argparse
import os
import re
from tint_shade_generator.lib.tint import tint_mode
from tint_shade_generator.lib.shade import shade_mode

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
    parser = argparse.ArgumentParser(description='Tint and Shade generator tool from a given HEX color code')
    parser.add_argument('-m', '--mode', type=str, default='shade', choices=['shade', 'tint'], help='Choose generation mode between tint or shade. Default: shade')
    parser.add_argument('-i', '--input', type=str, required=True, help='Input HEX color')
    parser.add_argument('-o', '--output', type=str, default='/.colors/', help='Output directory. Default: $HOME/.colors')
    parser.add_argument('-s', '--step', type=float, default=0.25, choices=(0, 1), help='The step of shade or tint color. Default: 0.25. Maximum: 1')
    parser.add_argument('-a', '--amount', type=int, default=5, choices=range(1, 11), help='The amount of generated color shade or tint. Default: 5. Maximum: 10')

    arg = parser.parse_args()

    mode = arg.mode
    in_color = arg.input
    out_dir = arg.output
    step = arg.step
    amount = arg.amount

    # Input Validation
    pattern = re.compile('^#[0-9A-F]{6}$', re.IGNORECASE)
    input_validate = re.search(pattern, in_color)

    if not input_validate:
        print('Invalid HEX color code! Please try again')

    else:
        # Check output directory
        home = os.path.expanduser('~')
        out_path = home + out_dir

        # Create new folder if output directory not exists
        if not os.path.exists(out_path):
            print('Output directory not found')
            print('Create new directory {0}'.format(out_path))
            os.chdir(home)
            os.mkdir(out_dir)

        # Change current working directory
        os.chdir(out_path)

        # Tint mode
        if mode == 'tint':
            tint_mode(in_color, step, amount)

        # Shade mode
        else:
            shade_mode(in_color, step, amount)
