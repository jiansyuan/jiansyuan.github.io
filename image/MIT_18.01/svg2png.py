import subprocess
import glob

for svg_file in glob.glob("*.svg"):
    png_file = svg_file.replace(".svg", ".png")
    subprocess.run([
        "G:/SoftwareFile/Inkscape/bin/inkscape",
        svg_file,
        "--export-type=png",
        f"--export-filename={png_file}"
    ])
    print(f"Converted {svg_file}")