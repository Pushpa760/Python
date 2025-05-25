print("name=pushpa,usn=1AY24AI086,section=O")
import time
import sys

def zigzag(steps):
    indent = 0
    indent_increasing = True

    try:
        for _ in range(steps):
            print(' ' * indent + '*')
            time.sleep(0.1)

            if indent_increasing:
                indent += 1
                if indent == 5:
                    indent_increasing = False
            else:
                indent -= 1
                if indent == 0:
                    indent_increasing = True
    except KeyboardInterrupt:
        sys.exit("\nZigzag animation stopped.")

zigzag(10)
