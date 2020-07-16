# Import libraries
from tint_shade_generator.lib.rgb2hex import rgb2hex
from tint_shade_generator.lib.hex2rgb import hex2rgb

def tint_generate(rgb_list, step):
    """
    Tint generator

    Parameters:
    -----------
        rgb_list: str
            RGB color list to convert to HEX
        step: float
            The ratio between the color step of tint

    Returns:
    --------
        hex: str
            HEX of result tint color

    Raises:
    -------
    """

    current_r = rgb_list[0]
    current_g = rgb_list[1]
    current_b = rgb_list[2]

    new_r = int(round(current_r + (255 - current_r)*step))
    new_g = int(round(current_g + (255 - current_g)*step))
    new_b = int(round(current_b + (255 - current_b)*step))

    new_rgb = [new_r, new_g, new_b]

    return rgb2hex(new_rgb)

def tint_mode(in_color, step, amount):
    """
    Tint mode: Generate tint colors and write file

    Parameters:
    -----------
        rgb_list: str
            RGB color list to convert to HEX
        step: float
            The ratio between the color step of tint
        amount: int
            The number of colors that user wish to generate

    Returns:
    --------
        tint: file
            A file contains generated shade colors

    Raises:
    -------
    """

    result_hex = []
    current_rgb = hex2rgb(in_color)

    for _ in range(amount):
        hex_tint = tint_generate(current_rgb, step)
        result_hex.append(hex_tint)
        current_rgb = hex2rgb(hex_tint)

    print('Writing file...')
    with open('tint', 'w') as file:
        for i in range(amount):
            if i == (amount-1):
                file.write("tint{0}='{1}'".format(i+1, result_hex[i]))
            else:
                file.write("tint{0}='{1}'\n".format(i+1, result_hex[i]))

    print('Wrote file successfully')
