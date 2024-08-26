from PIL import Image, ImageOps
import sys

def main():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    if len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    try:
        extententions = ['jpg', 'png', 'jpeg']
        ext = set()

        filename1 = sys.argv[1]
        filename2 = sys.argv[2]
        filenames = [filename1, filename2]
        for filename in filenames:
            filename = filename.split(".")
            if len(filename) != 2 or filename[1].lower() not in extententions:
                sys.exit("Invalid output")
            ext.add(filename[1])
        if len(ext) != 1:
            sys.exit("Input and output have different extensions")

        shirt(filename1, filename2)
    except FileNotFoundError:
        sys.exit("Input does not exist")

def shirt(read_file, write_file):
    shirt = Image.open("shirt.png")
    read_image = Image.open(read_file)
    shirt_size = shirt.size
    
    read_image = ImageOps.fit(read_image, shirt_size)
    read_image.paste(shirt, box = (0, 0), mask = shirt)

    read_image.save(write_file)

    return read_image

if __name__ == "__main__":
    main()