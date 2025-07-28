# WindsurfDemoPy

A simple Python project demonstrating:

- **Text file processing** (word counting)
- **TikTok-style video formatting** using MoviePy

---

## Requirements

- Python 3.7+
- [moviepy](https://github.com/Zulko/moviepy)
- [Pillow](https://python-pillow.org/) (for moviepy)

Install requirements:
```bash
pip install moviepy Pillow
```

---

## 1. Text File Word Counter (`script.py`)

Counts the number of words in a text file.

**Usage:**
```bash
python script.py path/to/textfile.txt
```
Or run and enter the path when prompted.

---

## 2. TikTok Video Formatter (`tiktok_video_formatter.py`)

- Finds the first video file in the `initialVideo` folder (`.mp4`, `.mov`, `.avi`)
- Resizes it to 1080px width, fits into a 1080x1920 (9:16) frame (TikTok format)
- Adds black bars to top/bottom if needed (no cropping)
- Saves the result to `outputFolder` with `_tiktok` appended to the filename

**Usage:**
1. Place a video in the `initialVideo` folder.
2. Run:
   ```bash
   python tiktok_video_formatter.py
   ```
3. Find the result in the `outputFolder`.

**Supported input formats:**
- `.mp4`, `.mov`, `.avi`

**Any video orientation is supported (landscape, portrait, square, etc).**

---

## Project Structure

```
initialVideo/         # Put your source videos here
outputFolder/         # Processed TikTok videos appear here
sample.txt            # Example text file for testing
script.py             # Word count script
README.md             # This file
tiktok_video_formatter.py # TikTok video formatting script
```

---

## License
MIT
