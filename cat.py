'''
This program prints stdin to the screen.
'''
import sys

def cat(file, chunk_size=8192):
    while True:
        data = file.read(chunk_size)
        if not data:
            break
    sys.stdout.buffer.write(data)
    sys.stdout.buffer.flush()

if __name__ == "__main__":
    if len(sys.argv) > 1:
        for filename in sys.argv[1:]:
            with open(filename, "rb") as f:
                try:
                    cat(f)
                except BrokenPipeError:
                    pass
    else:
        cat(sys.stdin.buffer)
