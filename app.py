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
    parser = argparse.ArgumentParser()
    parser.add_argument('-m', '--mode', default='shade', help='Choose generation mode between tint or shade. Default: shade')
    parser.add_argument('-i', '--input', required=True, help='Input HEX color')
    parser.add_argument('-o', '--output', help='Output directory. Default: $HOME/.colors')
    parser.add_argument('-s', '--step', help='The step of shade or tint color. Default: 0.1')
    parser.add_argument('-a', '--amount', help='The amount of generated color shade or tint. Default: 6. Maximum: 10')

    arg = parser.parse_args()

    mode = 'shade' if arg.mode == '' else arg.mode
    in_color = arg.input
    out_dir = '/.colors/' if arg.output == '' else arg.output
    step = 0.1 if arg.step == '' else arg.step
    amount = 6 if arg.amount == '' else arg.amount

    # Input Validation
    pattern = re.compile('/^#[0-9A-F]{6}$/i')
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
