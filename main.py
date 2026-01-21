import time
from animation_loader import load_animation
from animation_player import AnimationPlayer

animations = {
    "idle": load_animation("animations/idle.txt"),
    "walk": load_animation("animations/walk.txt"),
    "run": load_animation("animations/run.txt")
}

current_animation = "idle"
player = AnimationPlayer(animations[current_animation])

print("ASCII Animation Player")
print("Type: idle, walk, or run. Press Ctrl+C to exit.")

try:
    animation_order = ["idle", "walk", "run"]
    current_index = 0
    last_switch_time = time.time()
    switch_delay = 3  # seconds

    while True:
        current_time = time.time()

        # Switch animation every few seconds
        if current_time - last_switch_time > switch_delay:
            current_index = (current_index + 1) % len(animation_order)
            player.frames = animations[animation_order[current_index]]
            last_switch_time = current_time

        player.play()

except KeyboardInterrupt:
    print("\nExiting Animation Player...")