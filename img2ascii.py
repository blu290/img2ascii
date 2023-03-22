import sys
from PIL import Image
import math
def main(image_path,largeSet,saveToFile,stepsize=10):
    try:
        stepsize = int (stepsize)
    except:
        print("stepsize must be an integer")
        sys.exit(1)
    img = Image.open(image_path)
    img = img.convert('L') # convert image to grayscale
    width, height = img.size

    chars = "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. "[::-1] if largeSet else " .:-=+*#%@"
    asciiHeight = math.ceil(height/ stepsize)
    asciiWidth = math.ceil(width/ stepsize)
    asciiMatrix = [[" " for i in range(asciiWidth)] for j in range(asciiHeight)]
    for y in range(0, height, stepsize):
        for x in range(0,width, stepsize):
            pixel = img.getpixel((x, y))
            brightness = int((pixel / 255) * (len(chars) - 1))
            asciiMatrix[int(y / stepsize)][int(x / stepsize)] = chars[brightness]

    if saveToFile:
        with open("output.txt","w") as f:
            for row in asciiMatrix:
                f.write("".join(row)+"\n")
            f.close()

    if not saveToFile:
        for row in asciiMatrix:
            print("".join(row))

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: program [image_file_path] optional stepsize, optional -s to save to file,-v for the large character set")
        sys.exit(1)

    saveToFile = "-s" in sys.argv
    largeSet = "-v" in sys.argv
    if len(sys.argv)>=3:
            main(sys.argv[1],largeSet,saveToFile,sys.argv[2])
    
    else:
            main(sys.argv[1],largeSet,saveToFile)