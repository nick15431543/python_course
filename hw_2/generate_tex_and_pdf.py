from tex_lib.generator import generate_table, make_document, generate_image
with open('table_image.tex', 'w') as f:
    s = generate_table([[1, 2, 3, 4], [1, 2, 3, 4]])
    i = generate_image('spb_st_isaacs_2.jpg')
    s = s + i
    s = make_document(s)
    f.write(s)

import subprocess

tex_file = "table_image"

try:
    subprocess.check_call(["pdflatex", f"{tex_file}.tex"])
except subprocess.CalledProcessError as e:
    print(f"Error: {e}")

subprocess.call(['rm', f'{tex_file}.log'])
subprocess.call(['rm', f'{tex_file}.aux'])