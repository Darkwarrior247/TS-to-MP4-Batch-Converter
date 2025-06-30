# TS to MP4 Batch Converter 🎥

A simple and lightweight Python script that uses **FFmpeg** to convert `.ts` (MPEG-TS) video files to `.mp4` format.

✅ Supports:
- Single `.ts` file conversion
- Batch conversion from a folder
- Fast remuxing using `ffmpeg` (no re-encoding, lossless & fast)

---

## 📦 Requirements

- Python 3.6 or higher
- [FFmpeg](https://ffmpeg.org/download.html) installed and added to PATH

---

## 🚀 How to Use

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/Darkwarrior247/TS-to-MP4-Batch-Converter.git
cd TS-to-MP4-Batch-Converter
```
### 2️⃣ Install Python (if not already)

Download and install Python from the official website:

🔗 https://www.python.org

Make sure to check the box that says:

✅ "Add Python to PATH" during installation.

### 3️⃣ Install FFmpeg

Download from: https://www.gyan.dev/ffmpeg/builds/

Extract the ZIP file.

Add the `bin` folder to your system PATH  
(e.g., `C:\ffmpeg\bin`)

### 4️⃣ Run the Script

In terminal or PyCharm, run:

```bash
python ts_to_mp4_converter.py
```

###🖥️ Example Run:

=== TS to MP4 Converter ===
1. Convert a single file
2. Convert all .ts files in a folder
Enter choice (1 or 2):


- **Single file conversion:**  
  `C:\Users\YourName\Videos\video.ts`

- **Batch conversion:**  
  `C:\Users\YourName\Videos\TS_Folder`

### 🛠 How It Works
- Uses Python's `subprocess` to run FFmpeg
- Converts .ts files by remuxing (no quality loss)
- Output .mp4 files are saved in the same directory

### ❓ Troubleshooting
**FFmpeg not found error?**
1. Verify FFmpeg is installed
2. Confirm the `bin` folder is in your system PATH
3. Restart your terminal/PyCharm after changes

### 💡 Future Features
- GUI with drag-and-drop support
- Re-encoding options (quality/bitrate control)
- Detailed logging and error tracking
- Progress indicators for batch conversions
