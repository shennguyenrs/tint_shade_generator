# Import libraries
from tint_shade_generator.lib.rgb2hex import rgb2hex
from tint_shade_generator.lib.hex2rgb import hex2rgb

def shade_generate(rgb_list, step):
    """
    Shade generator

    Parameters:
    -----------
        rgb_list: list
            RGB color list to convert to HEX
        step: float
            The ratio between the color step of shade

    Returns:
    --------
        hex: str
            HEX of result shade color

    Raises:
    -------
    """

    current_r = rgb_list[0]
    current_g = rgb_list[1]
    current_b = rgb_list[2]

    new_r = int(round(current_r*(1-step)))
    new_g = int(round(current_g*(1-step)))
    new_b = int(round(current_b*(1-step)))

    new_rgb = [new_r, new_g, new_b]

    return rgb2hex(new_rgb)

def shade_mode(in_color, step, amount):
    """
    Shade mode: Generate tint colors and write file

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
        shade: file
            A file contains generated shade colors

    Raises:
    -------
    """

    result_hex = []
    current_rgb = hex2rgb(in_color)

    for _ in range(amount):
        rgb_shade = shade_generate(current_rgb, step)
        result_hex.append(rgb2hex(rgb_shade))
        current_rgb = rgb_shade

    with open('shade', 'w') as file:
        for i in range(amount):
            file.write("shade{0}='{1}'".format(i+1, result_hex[i]))

    print('Wrote file successfully')
