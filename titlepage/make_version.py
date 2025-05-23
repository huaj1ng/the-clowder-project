from functions import *
import preprocess
path = get_path()
absolute_path = preprocess.absolute_path()

version = version(path)
print("\\documentclass[tikz]{standalone}")
print("\\usepackage{tikz}")
print("\\usepackage{fontspec}")
print("\setmainfont[%")
print("    Path = ../../fonts/darwin/,%")
print("    Ligatures=TeX,%")
print("    UprightFont={DarwinSerif-Regular.ttf},%")
print("    BoldFont={DarwinSerif-Regular.ttf},%")
print("]{Darwin}")
print("\\begin{document}")
print("\\nopagecolor")
print("\\begin{tikzpicture}")
print("    \\node {\\bf{"+version+"}};")
print("\\end{tikzpicture}")
print("\\end{document}")
