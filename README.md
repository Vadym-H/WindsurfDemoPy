# WindsurfDemoPy

A simple Python project demonstrating:

- **JSON user filtering** (age-based filtering)
- **TikTok-style video formatting** using MoviePy

---

## Requirements

- Python 3.7+
- [moviepy](https://github.com/Zulko/moviepy)
- [Pillow](https://python-pillow.org/) (for moviepy)
- [opencv-python](https://pypi.org/project/opencv-python/) (for video blur effects)

Install requirements:
```bash
pip install moviepy Pillow opencv-python
```

---

## Project Structure

```
simplePythonProj/
├── JsonFilter/
│   ├── filter_underage_users.py    # JSON user filtering script
│   └── users_db.json               # Sample user database
├── VideoFormatter/
│   ├── tiktok_video_formatter.py   # TikTok video formatting script
│   ├── initialVideo/               # Put your source videos here
│   └── outputFolder/               # Processed TikTok videos appear here
└── README.md                       # This file
```

---

## 1. JSON User Filter (`JsonFilter/`)

Filters users from a JSON database based on age (finds users under 18).

**Usage:**
```bash
cd JsonFilter
python filter_underage_users.py
```

The script automatically uses `users_db.json` in the same directory. You can also specify a custom JSON file:
```bash
python filter_underage_users.py path/to/custom/file.json
```

**Sample Output:**
```
Using default JSON file: D:\...\JsonFilter\users_db.json
Underage users:
{'name': 'Alice', 'age': 17, 'email': 'alice@example.com'}
{'name': 'Charlie', 'age': 15, 'email': 'charlie@example.com'}
{'name': 'Eva', 'age': 12, 'email': 'eva@example.com'}
```

---

## 2. TikTok Video Formatter (`VideoFormatter/`)

- Finds the first video file in the `initialVideo` folder (`.mp4`, `.mov`, `.avi`)
- Resizes it to 1080px width, fits into a 1080x1920 (9:16) frame (TikTok format)
- Adds a **blurred, zoomed-in background** instead of black bars (no cropping)
- Saves the result to `outputFolder` with `_tiktok` appended to the filename

**Usage:**
1. Place a video in the `VideoFormatter/initialVideo` folder.
2. Run:
   ```bash
   cd VideoFormatter
   python tiktok_video_formatter.py
   ```
3. Find the result in the `VideoFormatter/outputFolder`.

**Supported input formats:**
- `.mp4`, `.mov`, `.avi`

**Any video orientation is supported (landscape, portrait, square, etc).**

---

## License
MIT
