import math
from os.path import exists
import PIL.Image
import PIL.ImageOps
import sys

MODE = "default"
CHARS = "default_chars"
USAGE = str("\nUsage: python3 converter.py [MODE] [CHARS]."
            "\n\nIf no arguments are passed [MODE] and [CHARS] will be default.."
            "\n   MODE types:"
            "\n       -default: for white background"
            "\n       -reversed for black background"
            "\n   CHARS types:"
            "\n       -minus_chars: uses 10 different chars to produce image"
            "\n       -default_chars: uses 20 different chars to produce image"
            "\n       -plus_chars: uses 70 different chars to produce image\n")

# TODO make width in chars of output be able to be passed as argument and adjust output accordingly
# TODO improve argument verification
if sys.argv.__len__() != 1 and sys.argv.__len__() != 2 and sys.argv.__len__() != 3:
    print(USAGE)
    exit(1)
else:
    if sys.argv.__len__() == 2:
        if sys.argv[1] == "default":
            MODE = "default"
        elif sys.argv[1] == "reversed":
            MODE = "reversed"
        elif sys.argv[1] == "minus_chars":
            CHARS = "minus_chars"
        elif sys.argv[1] == "default_chars":
            CHARS = "default_chars"
        elif sys.argv[1] == "plus_chars":
            CHARS = "plus_chars"
        else:
            print("\nError: Argument '" + sys.argv[1] + "' not recognized.")
            print(USAGE)
            exit(1)
    if sys.argv.__len__() == 3:
        if sys.argv[1] == "default":
            MODE = "default"
        elif sys.argv[1] == "reversed":
            MODE = "reversed"
        elif sys.argv[1] == "minus_chars":
            CHARS = "minus_chars"
        elif sys.argv[1] == "default_chars":
            CHARS = "default_chars"
        elif sys.argv[1] == "plus_chars":
            CHARS = "plus_chars"
        else:
            print("\nError: Argument '" + sys.argv[2] + "' not recognized.")
            print(USAGE)
            exit(1)

        if sys.argv[2] == "minus_chars":
            CHARS = "minus_chars"
        elif sys.argv[2] == "default_chars":
            CHARS = "default_chars"
        elif sys.argv[2] == "plus_chars":
            CHARS = "plus_chars"
        elif sys.argv[2] == "default":
            MODE = "default"
        elif sys.argv[2] == "reversed":
            MODE = "reversed"
        else:
            print("\nError: Argument '" + sys.argv[1] + "' not recognized.")
            print(USAGE)
            exit(1)

print("\nWhats the path to the image you want to convert ?")

while True:
    path = input()

    if exists(path):
        break
    elif path == "exit":
        print("\nProgram Closed")
        exit(0)
    else:
        print("\nError: File not found.\nPlease provide a valid path or type exit to exit the program.")

img = PIL.Image.open(path)
img = img.convert("L")

height = img.height
width = img.width
aspect_ratio = height / width

resize_width = 1200
resize_height = resize_width / aspect_ratio

width_count = (resize_width // 6)
height_count = resize_height // 8

img = img.resize((1200, math.floor(resize_height)), PIL.Image.LANCZOS)
# char arrays
# char_dict_minus 10% increment
# char_dict 5% increment
# char_dict_plus ~= 1.44927536232% increment
char_dict_minus_chars_default = {"@": 100,
                                 "%": 90,
                                 "#": 80,
                                 "*": 70,
                                 "+": 60,
                                 "=": 50,
                                 "-": 40,
                                 ":": 30,
                                 ".": 20,
                                 " ": 10}

char_dict_minus_chars_reversed = {"@": 10,
                                  "%": 20,
                                  "#": 30,
                                  "*": 40,
                                  "+": 50,
                                  "=": 60,
                                  "-": 70,
                                  ":": 80,
                                  ".": 90,
                                  " ": 100}

char_dict_default_chars_default = {"$": 100,
                                   "@": 95,
                                   "&": 90,
                                   "%": 85,
                                   "#": 80,
                                   "*": 75,
                                   "W": 70,
                                   "w": 65,
                                   "Z": 60,
                                   "Y": 55,
                                   "v": 50,
                                   "/": 45,
                                   "(": 40,
                                   "+": 35,
                                   "=": 30,
                                   "^": 25,
                                   ":": 20,
                                   ",": 15,
                                   ".": 10,
                                   " ": 5}

char_dict_default_chars_reversed = {"$": 0,
                                    "@": 5,
                                    "&": 10,
                                    "%": 15,
                                    "#": 20,
                                    "*": 25,
                                    "W": 30,
                                    "w": 35,
                                    "Z": 40,
                                    "Y": 45,
                                    "v": 50,
                                    "/": 55,
                                    "(": 60,
                                    "+": 65,
                                    "=": 70,
                                    "^": 75,
                                    ":": 80,
                                    ",": 85,
                                    ".": 90,
                                    " ": 95}

char_dict_plus_chars_reversed = {"$": 0,
                                 "@": 1.44927536232,
                                 "B": 2.89855072464,
                                 "%": 4.3478260869600005,
                                 "8": 5.79710144928,
                                 "&": 7.2463768116,
                                 "W": 8.695652173920001,
                                 "M": 10.14492753624,
                                 "#": 11.59420289856,
                                 "*": 13.04347826088,
                                 "o": 14.4927536232,
                                 "a": 15.94202898552,
                                 "h": 17.391304347840002,
                                 "k": 18.840579710160004,
                                 "b": 20.289855072480005,
                                 "d": 21.739130434800007,
                                 "p": 23.18840579712001,
                                 "q": 24.63768115944001,
                                 "w": 26.086956521760012,
                                 "m": 27.536231884080014,
                                 "Z": 28.985507246400015,
                                 "O": 30.434782608720017,
                                 "0": 31.88405797104002,
                                 "Q": 33.33333333336002,
                                 "L": 34.78260869568002,
                                 "C": 36.23188405800002,
                                 "J": 37.68115942032002,
                                 "U": 39.13043478264002,
                                 "Y": 40.579710144960025,
                                 "X": 42.02898550728003,
                                 "z": 43.47826086960003,
                                 "c": 44.92753623192003,
                                 "v": 46.37681159424003,
                                 "u": 47.82608695656003,
                                 "n": 49.275362318880035,
                                 "x": 50.724637681200036,
                                 "r": 52.17391304352004,
                                 "j": 53.62318840584004,
                                 "f": 55.07246376816004,
                                 "t": 56.52173913048004,
                                 "/": 57.971014492800045,
                                 "|": 59.420289855120046,
                                 "\\": 60.86956521744005,
                                 "(": 62.31884057976005,
                                 ")": 63.76811594208005,
                                 "1": 65.21739130440005,
                                 "{": 66.66666666672005,
                                 "}": 68.11594202904004,
                                 "[": 69.56521739136004,
                                 "]": 71.01449275368003,
                                 "?": 72.46376811600003,
                                 "-": 73.91304347832002,
                                 "_": 75.36231884064001,
                                 "+": 76.81159420296001,
                                 "~": 78.26086956528,
                                 "<": 79.7101449276,
                                 ">": 81.15942028991999,
                                 "i": 82.60869565223999,
                                 "!": 84.05797101455998,
                                 "l": 85.50724637687998,
                                 "I": 86.95652173919997,
                                 ";": 88.40579710151997,
                                 ":": 89.85507246383996,
                                 ",": 91.30434782615995,
                                 '"': 92.75362318847995,
                                 "^": 94.20289855079994,
                                 "`": 95.65217391311994,
                                 "'": 97.10144927543993,
                                 ".": 98.55072463775993,
                                 " ": 100.00000000007992}

char_dict_plus_chars_default = {"$": 100,
                                "@": 98.55072463775993,
                                "B": 97.10144927543993,
                                "%": 95.65217391311994,
                                "8": 94.20289855079994,
                                "&": 92.75362318847995,
                                "W": 91.30434782615995,
                                "M": 89.85507246383996,
                                "#": 88.40579710151997,
                                "*": 86.95652173919997,
                                "o": 85.50724637687998,
                                "a": 84.05797101455998,
                                "h": 82.60869565223999,
                                "k": 81.15942028991999,
                                "b": 79.7101449276,
                                "d": 78.26086956528,
                                "p": 76.81159420296001,
                                "q": 75.36231884064001,
                                "w": 73.91304347832002,
                                "m": 72.46376811600003,
                                "Z": 71.01449275368003,
                                "O": 69.56521739136004,
                                "0": 68.11594202904004,
                                "Q": 66.66666666672005,
                                "L": 65.21739130440005,
                                "C": 63.76811594208005,
                                "J": 62.31884057976005,
                                "U": 60.86956521744005,
                                "Y": 59.420289855120046,
                                "X": 57.971014492800045,
                                "z": 56.52173913048004,
                                "c": 55.07246376816004,
                                "v": 53.62318840584004,
                                "u": 52.17391304352004,
                                "n": 50.724637681200036,
                                "x": 49.275362318880035,
                                "r": 47.82608695656003,
                                "j": 46.37681159424003,
                                "f": 44.92753623192003,
                                "t": 43.47826086960003,
                                "/": 42.02898550728003,
                                "|": 40.579710144960025,
                                "\\": 39.13043478264002,
                                "(": 37.68115942032002,
                                ")": 36.23188405800002,
                                "1": 34.78260869568002,
                                "{": 33.33333333336002,
                                "}": 31.88405797104002,
                                "[": 30.434782608720017,
                                "]": 28.985507246400015,
                                "?": 27.536231884080014,
                                "-": 26.086956521760012,
                                "_": 24.63768115944001,
                                "+": 23.18840579712001,
                                "~": 21.739130434800007,
                                "<": 20.289855072480005,
                                ">": 18.840579710160004,
                                "i": 17.391304347840002,
                                "!": 15.94202898552,
                                "l": 14.4927536232,
                                "I": 13.04347826088,
                                ";": 11.59420289856,
                                ":": 10.14492753624,
                                ",": 8.695652173920001,
                                '"': 7.2463768116,
                                "^": 5.79710144928,
                                "`": 4.3478260869600005,
                                "'": 2.89855072464,
                                ".": 1.44927536232,
                                " ": 0}

# crop image in grid of 6x8 images and save in array
# TODO isto aqui nao esta a fazer o crop bem
cropped_img = []
for i in range(0, int(resize_height), 16):
    for j in range(0, int(resize_width), 6):
        cropped_img.append(img.crop((j, i, j + 6, i + 16)))

# get average color of each cropped image
avg_color = []
for i in range(cropped_img.__len__()):
    mean = 0
    for j in range(0, cropped_img[i].width):
        for k in range(0, cropped_img[i].height):
            value = cropped_img[i].getpixel((j, k))
            black_level = (1 - value / 255) * 100
            mean += black_level
    mean = mean / (cropped_img[i].width * cropped_img[i].height)
    avg_color.append(mean)

# for each cropped image get corresponding char and print to console
print_ascii = ""
dict_to_use = "char_dict_" + CHARS + "_" + MODE
for i in range(cropped_img.__len__()):
    if not 0 and i % width_count == 0:
        print_ascii += "\n"  # line break every time i is multiple of width_count

    print_ascii += (min(globals()[dict_to_use].items(), key=lambda x: abs(avg_color[i] - x[1])))[0]

print(print_ascii)
