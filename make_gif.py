import math
from PIL import Image, ImageDraw, ImageFont

# Canvas dimensions
WIDTH = 256
HEIGHT = 240
SCALE = 2  # Upscale to 512x480 for crisp preview

# Colors
C_SKY = (92, 148, 252)
C_RED = (184, 28, 0)
C_SKIN = (252, 152, 56)
C_BLUE = (0, 32, 160)
C_DARK_BROWN = (80, 48, 0)
C_YELLOW = (252, 188, 56)
C_WHITE = (252, 252, 252)
C_BLACK = (0, 0, 0)
C_GREEN = (0, 168, 0)
C_LIGHT_GREEN = (128, 208, 16)
C_DARK_GREEN = (0, 80, 0)
C_BRICK = (184, 68, 24)
C_BRICK_LIGHT = (252, 152, 56)
C_BLOCK_EMPTY = (136, 84, 0)

def draw_mario(draw, x, y, state="idle", facing_left=False, run_frame=0):
    x = int(x)
    y = int(y)
    # 16x16 sprite
    if state == "jump":
        # Hat
        draw.rectangle([x+3, y+0, x+11, y+1], fill=C_RED)
        # Face / Hair
        draw.rectangle([x+3, y+2, x+5, y+2], fill=C_DARK_BROWN)
        draw.rectangle([x+6, y+2, x+7, y+2], fill=C_SKIN)
        draw.rectangle([x+8, y+2, x+8, y+3], fill=C_BLACK)
        draw.rectangle([x+4, y+3, x+8, y+4], fill=C_SKIN)
        draw.rectangle([x+8, y+5, x+11, y+5], fill=C_DARK_BROWN)
        # Arms / Shirt
        draw.rectangle([x+0, y+3, x+2, y+4], fill=C_SKIN)
        draw.rectangle([x+3, y+5, x+4, y+7], fill=C_RED)
        draw.rectangle([x+10, y+6, x+13, y+7], fill=C_SKIN)
        # Overalls
        draw.rectangle([x+4, y+8, x+9, y+10], fill=C_BLUE)
        draw.rectangle([x+7, y+8, x+7, y+8], fill=C_YELLOW)
        # Legs
        draw.rectangle([x+1, y+11, x+4, y+13], fill=C_DARK_BROWN)
        draw.rectangle([x+9, y+9, x+12, y+12], fill=C_DARK_BROWN)
    elif state == "run":
        # Hat
        draw.rectangle([x+3, y+1, x+11, y+2], fill=C_RED)
        # Face
        draw.rectangle([x+2, y+3, x+4, y+4], fill=C_DARK_BROWN)
        draw.rectangle([x+5, y+3, x+8, y+4], fill=C_SKIN)
        draw.rectangle([x+7, y+3, x+7, y+4], fill=C_BLACK)
        draw.rectangle([x+3, y+5, x+7, y+5], fill=C_SKIN)
        draw.rectangle([x+8, y+5, x+10, y+5], fill=C_DARK_BROWN)
        # Shirt
        draw.rectangle([x+4, y+6, x+8, y+7], fill=C_RED)
        draw.rectangle([x+3, y+8, x+9, y+10], fill=C_BLUE)
        draw.rectangle([x+4, y+8, x+4, y+8], fill=C_YELLOW)
        if run_frame == 0:
            draw.rectangle([x+1, y+11, x+4, y+13], fill=C_DARK_BROWN)
            draw.rectangle([x+9, y+11, x+12, y+13], fill=C_DARK_BROWN)
            draw.rectangle([x+1, y+7, x+2, y+8], fill=C_SKIN)
            draw.rectangle([x+10, y+8, x+11, y+9], fill=C_SKIN)
        else:
            draw.rectangle([x+2, y+12, x+5, y+14], fill=C_DARK_BROWN)
            draw.rectangle([x+7, y+12, x+10, y+14], fill=C_DARK_BROWN)
            draw.rectangle([x+2, y+8, x+3, y+9], fill=C_SKIN)
            draw.rectangle([x+9, y+8, x+10, y+9], fill=C_SKIN)
    else:
        # Idle
        draw.rectangle([x+3, y+1, x+7, y+1], fill=C_RED)
        draw.rectangle([x+2, y+2, x+10, y+2], fill=C_RED)
        draw.rectangle([x+2, y+3, x+4, y+3], fill=C_DARK_BROWN)
        draw.rectangle([x+5, y+3, x+6, y+3], fill=C_SKIN)
        draw.rectangle([x+7, y+3, x+7, y+4], fill=C_BLACK)
        draw.rectangle([x+3, y+4, x+8, y+5], fill=C_SKIN)
        draw.rectangle([x+8, y+5, x+10, y+5], fill=C_DARK_BROWN)
        draw.rectangle([x+7, y+6, x+10, y+6], fill=C_DARK_BROWN)
        draw.rectangle([x+3, y+7, x+9, y+8], fill=C_RED)
        draw.rectangle([x+4, y+9, x+8, y+11], fill=C_BLUE)
        draw.rectangle([x+4, y+10, x+4, y+10], fill=C_YELLOW)
        draw.rectangle([x+8, y+10, x+8, y+10], fill=C_YELLOW)
        draw.rectangle([x+0, y+8, x+1, y+9], fill=C_SKIN)
        draw.rectangle([x+11, y+8, x+12, y+9], fill=C_SKIN)
        draw.rectangle([x+2, y+13, x+4, y+15], fill=C_DARK_BROWN)
        draw.rectangle([x+8, y+13, x+10, y+15], fill=C_DARK_BROWN)

def draw_goomba(draw, x, y, squished=False, step=0):
    x = int(x)
    y = int(y)
    if squished:
        draw.rectangle([x+1, y+9, x+14, y+11], fill=C_BRICK)
        draw.rectangle([x+3, y+12, x+12, y+13], fill=C_SKIN)
        draw.rectangle([x+4, y+11, x+5, y+11], fill=C_BLACK)
        draw.rectangle([x+10, y+11, x+11, y+11], fill=C_BLACK)
        draw.rectangle([x+0, y+14, x+15, y+15], fill=C_BLACK)
    else:
        # Cap
        draw.rectangle([x+4, y+1, x+11, y+1], fill=C_BRICK)
        draw.rectangle([x+2, y+2, x+13, y+2], fill=C_BRICK)
        draw.rectangle([x+1, y+3, x+14, y+7], fill=C_BRICK)
        # Face
        draw.rectangle([x+3, y+8, x+12, y+11], fill=C_SKIN)
        # Eyes
        draw.rectangle([x+4, y+6, x+6, y+6], fill=C_BLACK)
        draw.rectangle([x+9, y+6, x+11, y+6], fill=C_BLACK)
        draw.rectangle([x+5, y+7, x+5, y+9], fill=C_BLACK)
        draw.rectangle([x+10, y+7, x+10, y+9], fill=C_BLACK)
        draw.rectangle([x+4, y+7, x+4, y+9], fill=C_WHITE)
        draw.rectangle([x+11, y+7, x+11, y+9], fill=C_WHITE)
        # Feet
        if step == 0:
            draw.rectangle([x+1, y+12, x+5, y+15], fill=C_BLACK)
            draw.rectangle([x+10, y+13, x+13, y+15], fill=C_BLACK)
        else:
            draw.rectangle([x+2, y+13, x+5, y+15], fill=C_BLACK)
            draw.rectangle([x+10, y+12, x+14, y+15], fill=C_BLACK)

def draw_brick(draw, x, y):
    draw.rectangle([x, y, x+15, y+15], fill=C_BRICK)
    draw.line([x, y+7, x+15, y+7], fill=C_BLACK)
    draw.line([x, y+15, x+15, y+15], fill=C_BLACK)
    draw.line([x+7, y, x+7, y+6], fill=C_BLACK)
    draw.line([x+15, y, x+15, y+6], fill=C_BLACK)
    draw.line([x+3, y+8, x+3, y+14], fill=C_BLACK)
    draw.line([x+11, y+8, x+11, y+14], fill=C_BLACK)
    draw.line([x, y, x+6, y], fill=C_BRICK_LIGHT)
    draw.line([x+8, y, x+14, y], fill=C_BRICK_LIGHT)

def draw_question_block(draw, x, y, hit=False):
    if hit:
        draw.rectangle([x, y, x+15, y+15], fill=C_BLOCK_EMPTY)
        draw.rectangle([x, y, x+15, y+15], outline=C_BLACK)
        draw.point([(x+2, y+2), (x+13, y+2), (x+2, y+13), (x+13, y+13)], fill=C_BLACK)
    else:
        draw.rectangle([x, y, x+15, y+15], fill=C_YELLOW)
        draw.rectangle([x, y, x+15, y+15], outline=C_BLACK)
        draw.point([(x+1, y+1), (x+14, y+1), (x+1, y+14), (x+14, y+14)], fill=C_BLACK)
        # ? Mark
        draw.rectangle([x+5, y+3, x+8, y+4], fill=C_WHITE)
        draw.rectangle([x+8, y+5, x+9, y+6], fill=C_WHITE)
        draw.rectangle([x+5, y+7, x+7, y+8], fill=C_WHITE)
        draw.rectangle([x+5, y+11, x+6, y+12], fill=C_WHITE)

def draw_pipe(draw, x, y, h=32):
    # Top rim
    draw.rectangle([x, y, x+31, y+15], fill=C_GREEN)
    draw.rectangle([x+2, y, x+4, y+15], fill=C_LIGHT_GREEN)
    draw.rectangle([x+26, y, x+30, y+15], fill=C_DARK_GREEN)
    draw.rectangle([x, y, x+31, y+15], outline=C_BLACK)
    # Body
    draw.rectangle([x+2, y+16, x+29, y+h-1], fill=C_GREEN)
    draw.rectangle([x+4, y+16, x+6, y+h-1], fill=C_LIGHT_GREEN)
    draw.rectangle([x+24, y+16, x+28, y+h-1], fill=C_DARK_GREEN)
    draw.line([x+2, y+16, x+2, y+h-1], fill=C_BLACK)
    draw.line([x+29, y+16, x+29, y+h-1], fill=C_BLACK)

def draw_ground(draw, x, y):
    draw.rectangle([x, y, x+15, y+15], fill=C_BRICK)
    draw.line([x, y, x+15, y], fill=C_BRICK_LIGHT)
    draw.line([x, y, x, y+15], fill=C_BRICK_LIGHT)
    draw.line([x+15, y, x+15, y+15], fill=C_DARK_BROWN)
    draw.line([x, y+15, x+15, y+15], fill=C_DARK_BROWN)
    draw.rectangle([x+3, y+4, x+4, y+5], fill=C_DARK_BROWN)
    draw.rectangle([x+10, y+5, x+11, y+6], fill=C_DARK_BROWN)
    draw.rectangle([x+6, y+10, x+7, y+11], fill=C_DARK_BROWN)

def draw_coin(draw, x, y, frame=0):
    w = [8, 6, 4, 6][frame % 4]
    off_x = (16 - w) // 2
    draw.rectangle([x+off_x, y+2, x+off_x+w-1, y+13], fill=C_YELLOW)
    if w >= 4:
        draw.rectangle([x+off_x+1, y+3, x+off_x+w-2, y+12], fill=C_WHITE)

def render_frame(t, total_frames=72):
    img = Image.new("RGB", (WIDTH, HEIGHT), C_SKY)
    draw = ImageDraw.Draw(img)

    # 1. Background Hill & Bush
    # Hill
    draw.chord([40, 160, 120, 240], 180, 360, fill=C_GREEN, outline=C_DARK_GREEN)
    # Clouds
    draw.rectangle([30, 40, 66, 52], fill=(255, 255, 255))
    draw.rectangle([36, 32, 60, 52], fill=(255, 255, 255))
    draw.rectangle([170, 60, 206, 72], fill=(255, 255, 255))
    draw.rectangle([176, 52, 200, 72], fill=(255, 255, 255))

    # 2. Scenery Objects
    # Pipe
    draw_pipe(draw, 210, 176, 32)

    # Blocks at y=144
    draw_brick(draw, 80, 144)
    q_hit = t >= 25
    q_y = 144 - (3 if (25 <= t <= 28) else 0)
    draw_question_block(draw, 96, q_y, hit=q_hit)
    draw_brick(draw, 112, 144)
    draw_brick(draw, 128, 144)

    # 3. Game State & Animation timeline
    # Coin animation
    score = 0
    coins = 0
    if t >= 25:
        score += 200
        coins = 1
        coin_t = t - 25
        if coin_t < 16:
            coin_y = 136 - math.sin(coin_t / 16.0 * math.pi) * 32
            draw_coin(draw, 96, int(coin_y), frame=coin_t // 2)

    # Floating text for coin
    if 27 <= t <= 44:
        ft_y = 120 - (t - 27) * 0.8
        draw.text((98, int(ft_y)), "200", fill=C_WHITE)

    # Goomba logic
    # Goomba walks left from x=180 to x=120
    goomba_x = 180 - t * 0.9
    goomba_y = 192
    goomba_squished = t >= 44
    if t >= 44:
        score += 100
        # Floating text for stomp
        if t <= 62:
            draw.text((int(goomba_x), 175 - (t - 44) * 0.6), "100", fill=C_WHITE)

    if t < 65:  # Despawn flat goomba after a bit
        draw_goomba(draw, goomba_x, goomba_y, squished=goomba_squished, step=(t // 6) % 2)

    # Mario logic
    m_state = "run"
    m_x = 20
    m_y = 192
    run_f = (t // 4) % 2

    if t < 16:
        # Running toward block
        m_x = 20 + t * 4.2
        m_y = 192
        m_state = "run"
    elif t < 36:
        # Jumping to hit block
        jump_t = (t - 16) / 20.0
        m_x = 20 + 16 * 4.2 + (t - 16) * 1.5
        m_y = 192 - math.sin(jump_t * math.pi) * 44
        m_state = "jump"
    elif t < 44:
        # Falling toward Goomba
        fall_t = (t - 36) / 8.0
        m_x = 117 + (t - 36) * 2.8
        m_y = 148 + fall_t * 44
        m_state = "jump"
    elif t < 54:
        # Stomp bounce
        bounce_t = (t - 44) / 10.0
        m_x = 140 + (t - 44) * 2.5
        m_y = 192 - math.sin(bounce_t * math.pi) * 18
        m_state = "jump"
    else:
        # Jogging toward pipe
        m_x = 165 + (t - 54) * 2.2
        m_y = 192
        m_state = "run" if m_x < 200 else "idle"

    draw_mario(draw, m_x, m_y, state=m_state, run_frame=run_f)

    # 4. Ground Blocks (y=208 and y=224)
    for c in range(0, WIDTH, 16):
        draw_ground(draw, c, 208)
        draw_ground(draw, c, 224)

    # 5. HUD Top Bar
    draw.text((16, 8), "MARIO", fill=C_WHITE)
    draw.text((16, 18), f"{score:06d}", fill=C_WHITE)

    draw_coin(draw, 80, 16, frame=(t // 4) % 4)
    draw.text((90, 18), f"x{coins:02d}", fill=C_WHITE)

    draw.text((140, 8), "WORLD", fill=C_WHITE)
    draw.text((146, 18), "1-1", fill=C_WHITE)

    draw.text((200, 8), "TIME", fill=C_WHITE)
    draw.text((206, 18), f"{375 - t // 3}", fill=C_WHITE)

    # Upscale cleanly with NEAREST filter for crisp pixels
    img_scaled = img.resize((WIDTH * SCALE, HEIGHT * SCALE), Image.NEAREST)
    return img_scaled

def main():
    print("Generating gameplay frames...")
    frames = []
    TOTAL_FRAMES = 72
    for t in range(TOTAL_FRAMES):
        frames.append(render_frame(t, TOTAL_FRAMES))

    output_path = r"E:\work\mario-game\preview.gif"
    print(f"Saving animated GIF to {output_path}...")
    frames[0].save(
        output_path,
        save_all=True,
        append_images=frames[1:],
        duration=65,  # ~15.4 fps
        loop=0
    )
    print("Done! GIF successfully created.")

if __name__ == "__main__":
    main()
