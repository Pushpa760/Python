print("name=pushpa,usn=1AY24AI086,section=O")
def comma_code(items):
    if not items:
        return ''
    elif len(items) == 1:
        return items[0]
    elif len(items) == 2:
        return f"{items[0]} and {items[1]}"
    else:
        return ', '.join(items[:-1]) + f", and {items[-1]}"

def main():
    items = ['apples', 'bananas', 'tofu', 'cats']
    
    result = comma_code(items)
    print("Formatted list:")
    print(result)
if __name__=="__main__":
    main()
