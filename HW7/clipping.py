import matplotlib.pyplot as plt

# Kode representasi kode regio Cohen-Sutherland
INSIDE       = 0  # 0000
LEFT         = 1  # 0001
RIGHT        = 2  # 0010
BOTTOM       = 4  # 0100
TOP          = 8  # 1000

# Definisi window (jendela) dan garis
x_min, y_min, x_max, y_max = 50, 50, 250, 250
line = [(20, 80), (200, 300)]

# Fungsi untuk menghitung kode regio
def compute_code(x, y):
    code = INSIDE
    if x < x_min:
        code |= LEFT
    elif x > x_max:
        code |= RIGHT
    if y < y_min:
        code |= BOTTOM
    elif y > y_max:
        code |= TOP
    return code

# Fungsi untuk menggambar garis setelah pemotongan
def draw_clipped_line(x1, y1, x2, y2):
    plt.plot([x1, x2], [y1, y2], color='blue', linestyle='dashed')

# Fungsi untuk melakukan clipping
def cohen_sutherland_line_clipping(x1, y1, x2, y2):
    code1 = compute_code(x1, y1)
    code2 = compute_code(x2, y2)
    accept = False

    while True:
        if code1 == 0 and code2 == 0:
            accept = True
            break
        elif code1 & code2 != 0:
            break
        else:
            x, y = 0, 0
            code_out = code1 if code1 != 0 else code2

            if code_out & TOP:
                x = x1 + (x2 - x1) * (y_max - y1) / (y2 - y1)
                y = y_max
            elif code_out & BOTTOM:
                x = x1 + (x2 - x1) * (y_min - y1) / (y2 - y1)
                y = y_min
            elif code_out & RIGHT:
                y = y1 + (y2 - y1) * (x_max - x1) / (x2 - x1)
                x = x_max
            elif code_out & LEFT:
                y = y1 + (y2 - y1) * (x_min - x1) / (x2 - x1)
                x = x_min

            if code_out == code1:
                x1, y1 = x, y
                code1 = compute_code(x1, y1)
            else:
                x2, y2 = x, y
                code2 = compute_code(x2, y2)

    if accept:
        draw_clipped_line(x1, y1, x2, y2)

# Inisialisasi plot
plt.figure()
plt.xlim(0, 300)
plt.ylim(0, 300)

# Gambar window (jendela)
plt.plot([x_min, x_max, x_max, x_min, x_min], [y_min, y_min, y_max, y_max, y_min], color='black')

# Gambar garis sebelum pemotongan
plt.plot([line[0][0], line[1][0]], [line[0][1], line[1][1]], color='red', linestyle='dashed', label='Garis Sebelum Pemotongan')

# Pemotongan garis menggunakan Cohen-Sutherland
cohen_sutherland_line_clipping(line[0][0], line[0][1], line[1][0], line[1][1])

plt.title('Pemotongan Garis dengan Cohen-Sutherland')
plt.legend()
plt.show()
