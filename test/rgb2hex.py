def rgb2hex(color_list):
    r_color = color_list[0]
    g_color = color_list[1]
    b_color = color_list[2]
    return f'#{r_color:02x}{g_color:02x}{b_color:02x}'

print(rgb2hex([252, 48, 121]))
