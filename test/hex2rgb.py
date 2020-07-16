def hex2rgb(color_code):
    rgb = []
    hex_color = color_code.lstrip('#')

    for i in (0, 2, 4):
        rgb.append(int(hex_color[i:i+2], 16))

    return rgb

print(hex2rgb('#fc3079'))    
