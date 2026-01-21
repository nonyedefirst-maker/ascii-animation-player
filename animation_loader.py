def load_animation(file_path):
    with open(file_path, 'r') as file:
        frames = file.read().splitlines()
    return frames