def rgb2hex(color_list):
    """
    A tool generate tint or shade in HEX of the given color

    Parameters:
    -----------
        color_list: list
            Input list of RGB color

    Returns:
    --------
        hex: str
            HEX color code

    Raises:
    -------
    """

    r_color = color_list[0]
    g_color = color_list[1]
    b_color = color_list[2]
    return f'#{r_color:02x}{g_color:02x}{b_color:02x}'
