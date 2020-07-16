def hex2rgb(color_code):
    """
    Convert HEX code to RGB color

    Parameters:
    -----------
        color_code: str
            HEX code of  color

    Returns:
    --------
        rgb: list
            RGB color in list

    Raises:
    -------
    """

    rgb = []
    hex_color = color_code.lstrip('#')

    for i in (0, 2, 4):
        rgb.append(int(hex_color[i:i+2], 16))

    return rgb
