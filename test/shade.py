def hex2rgb(color_code):
    rgb = []
    hex_color = color_code.lstrip('#')

    for i in (0, 2, 4):
        rgb.append(int(hex_color[i:i+2], 16))

    return rgb

def rgb2hex(color_list):
    r_color = color_list[0]
    g_color = color_list[1]
    b_color = color_list[2]
    return f'#{r_color:02x}{g_color:02x}{b_color:02x}'

def shade_generate(rgb_list, step):

    current_r = rgb_list[0]
    current_g = rgb_list[1]
    current_b = rgb_list[2]

    new_r = int(round(current_r*(1-step)))
    new_g = int(round(current_g*(1-step)))
    new_b = int(round(current_b*(1-step)))

    new_rgb = [new_r, new_g, new_b]

    return rgb2hex(new_rgb)

def shade_mode(in_color, step, amount):

    current_rgb = hex2rgb(in_color)

    for _ in range(amount):
        hex_shade = shade_generate(current_rgb, step)
        print(hex_shade)
        current_rgb = hex2rgb(hex_shade)
        print(current_rgb)

shade_mode('#fc3079', 0.15, 6)
