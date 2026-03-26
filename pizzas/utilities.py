import os

def get_next_filename(folder, ext):
    os.makedirs(folder, exist_ok=True)

    num = 1
    while os.path.exists(os.path.join(folder, f"{num:02d}{ext}")):
        num += 1

    return os.path.join(folder, f"{num:02d}{ext}")

def greek_labels(n):
    base = [chr(i) for i in range(0x03B1, 0x03C9 + 1)]
    labels = []
    if n > 24:
        for i in range(n):
            letter = base[i % 24]
            number = i // 24 + 1
            labels.append(f"{letter}{number}")
    else:
        for i in range(n):
            labels.append(base[i])
    return labels