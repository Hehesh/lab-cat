'''
This program prints stdin to the screen.
'''
import sys

BUFFER_SIZE = 8192

def cat(file):
    while True:
        chunk = file.read(BUFFER_SIZE)
        if not chunk:
            break
        sys.stdout.buffer.write(chunk)

if __name__ == "__main__":
    if len(sys.argv) > 1:
        for filename in sys.argv[1:]:
            with open(filename, "rb") as f:
                cat(f)
    else:
        cat(sys.stdin.buffer)
