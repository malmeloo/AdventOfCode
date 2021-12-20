import aoc

input_data = aoc.get_input('\n\n')
algorithm = input_data[0]

_input_image = [list(l) for l in input_data[1].splitlines()]
input_pixels = {}
for row_i, row in enumerate(_input_image):
    for col_i, value in enumerate(row):
        if value == '#':
            input_pixels[(col_i, row_i)] = value


surrounding_pixels = '.'


def _bbox(pixels):
    max_x = 0
    max_y = 0
    for pix in pixels.keys():
        if pix[0] > max_x:
            max_x = pix[0]
        if pix[1] > max_y:
            max_y = pix[1]

    return max_x, max_y


def _neighbors(x, y):
    for _y in range(x - 1, x + 2):
        for _x in range(y - 1, y + 2):
            yield _x, _y


def _enhanced_pixel(x, y, bound_x, bound_y, img, algo):
    bin_str = ''
    for neigh in _neighbors(x, y):
        if _get_pixel(neigh[0], neigh[1], bound_x, bound_y, img) == '#':
            bin_str += '1'
        else:
            bin_str += '0'

    new_pix = algo[int(bin_str, 2)]
    return new_pix


def _get_pixel(x, y, bound_x, bound_y, img):
    if x <= -1 or x >= bound_x + 1 or y <= -1 or y >= bound_y + 1:
        return surrounding_pixels

    return img.get((x, y), '.')


def _enhance(in_img, algo):
    global surrounding_pixels

    out_img = {}
    bound_x, bound_y = _bbox(in_img)
    for x in range(-1, bound_x + 2):
        for y in range(-1, bound_y + 2):
            new_pixel = _enhanced_pixel(x, y, bound_x, bound_y, in_img, algo)
            if new_pixel == '#':
                out_img[(y + 1, x + 1)] = new_pixel

    if algo[0] == '#' and surrounding_pixels == '.':
        surrounding_pixels = '#'
    elif algo[-1] == '.' and surrounding_pixels == '#':
        surrounding_pixels = '.'

    return out_img


def challenge(n):
    im = _enhance(input_pixels, algorithm)
    for _ in range(n-1):
        im = _enhance(im, algorithm)

    return len(im.keys())


aoc.run(lambda: challenge(2))
aoc.run(lambda: challenge(50))
