"""
TikTok Video Formatter Script

- Finds the first video in 'initialVideo' folder
- Resizes to 1080px width (TikTok 9:16, 1080x1920), maintaining aspect ratio
- Adds blurred, zoomed-in video background (top/bottom) if needed to fill 1920px height
- Saves to 'outputFolder' with '_tiktok' appended to filename
"""
import os
from moviepy.editor import VideoFileClip, CompositeVideoClip
import cv2

# Patch for Pillow 10+ compatibility with moviepy
import PIL
if not hasattr(PIL.Image, "ANTIALIAS"):
    PIL.Image.ANTIALIAS = PIL.Image.Resampling.LANCZOS

# --- Config ---
INPUT_DIR = 'initialVideo'
OUTPUT_DIR = 'outputFolder'
TARGET_WIDTH = 1080
TARGET_HEIGHT = 1920
VIDEO_EXTS = ['.mp4', '.mov', '.avi']

def find_first_video(input_dir):
    for fname in os.listdir(input_dir):
        if any(fname.lower().endswith(ext) for ext in VIDEO_EXTS):
            return os.path.join(input_dir, fname)
    return None

def main():
    # 1. Ensure folders exist
    os.makedirs(INPUT_DIR, exist_ok=True)
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    # 2. Find the first video file
    video_path = find_first_video(INPUT_DIR)
    if not video_path:
        print(f"No video files found in '{INPUT_DIR}'. Supported: {VIDEO_EXTS}")
        return
    print(f"Found video: {video_path}")

    # 3. Load video
    clip = VideoFileClip(video_path)

    # 4. Resize to target width, maintain aspect
    new_clip = clip.resize(width=TARGET_WIDTH)
    # Calculate required top/bottom bars
    pad_top = pad_bottom = 0
    if new_clip.h < TARGET_HEIGHT:
        total_pad = TARGET_HEIGHT - new_clip.h
        pad_top = total_pad // 2
        pad_bottom = total_pad - pad_top
    
    # --- BLURRED BACKGROUND INSTEAD OF BLACK BARS ---
    # Create a blurred, zoomed-in version of the original video as background
    # 1. Resize to fill the whole 1080x1920 frame (may crop)
    bg_zoom = clip.resize(newsize=(TARGET_WIDTH, TARGET_HEIGHT))
    # 2. Apply strong gaussian blur (MoviePy >=2.0.0)
    try:
        from moviepy.video.fx.all import gaussian_blur
        blurred_bg = bg_zoom.fx(gaussian_blur, sigma=50)
    except ImportError:
        # fallback for older moviepy
        blurred_bg = bg_zoom.fl_image(lambda frame: cv2.GaussianBlur(frame, (99,99), 50))
    # 3. Compose: blurred background + original video centered
    final = CompositeVideoClip([
        blurred_bg,
        new_clip.set_position((0, pad_top))
    ], size=(TARGET_WIDTH, TARGET_HEIGHT))

    # 5. Output filename
    base = os.path.splitext(os.path.basename(video_path))[0]
    ext = os.path.splitext(video_path)[1]
    out_path = os.path.join(OUTPUT_DIR, f"{base}_tiktok{ext}")
    print(f"Saving TikTok video to: {out_path}")
    final.write_videofile(out_path, codec="libx264", audio_codec="aac")

if __name__ == "__main__":
    main()
