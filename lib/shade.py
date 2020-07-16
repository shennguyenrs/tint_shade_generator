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
        hex_shade = shade_generate(current_rgb, step)
        result_hex.append(hex_shade)
        current_rgb = hex2rgb(hex_shade)

    print('Writing file...')
    with open('shade', 'w') as file:
        for i in range(amount):
            if i == (amount-1):
                file.write("shade{0}='{1}'".format(i+1, result_hex[i]))
            else:
                file.write("shade{0}='{1}'\n".format(i+1, result_hex[i]))

    print('Wrote file successfully')
