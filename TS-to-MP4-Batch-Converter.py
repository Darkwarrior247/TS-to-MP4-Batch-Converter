import os
import subprocess

def convert_ts_to_mp4(input_path, output_path):
    try:
        subprocess.run([
            'ffmpeg',
            '-i', input_path,
            '-c', 'copy',
            output_path
        ], check=True)
        print(f"✅ Converted: {input_path} → {output_path}")
    except subprocess.CalledProcessError as e:
        print(f"❌ Error converting {input_path}: {e}")

def convert_single_file():
    ts_path = input("Enter full path of the .ts file: ").strip('"')
    if not ts_path.lower().endswith(".ts") or not os.path.isfile(ts_path):
        print("❌ Invalid file. Make sure it exists and has a .ts extension.")
        return

    mp4_path = os.path.splitext(ts_path)[0] + ".mp4"
    convert_ts_to_mp4(ts_path, mp4_path)

def convert_batch():
    folder = input("Enter folder path containing .ts files: ").strip('"')
    if not os.path.isdir(folder):
        print("❌ Invalid folder path.")
        return

    ts_files = [f for f in os.listdir(folder) if f.lower().endswith(".ts")]
    if not ts_files:
        print("❌ No .ts files found in the folder.")
        return

    for ts_file in ts_files:
        ts_path = os.path.join(folder, ts_file)
        mp4_path = os.path.splitext(ts_path)[0] + ".mp4"
        convert_ts_to_mp4(ts_path, mp4_path)

def main():
    print("=== TS to MP4 Converter ===")
    print("1. Convert a single file")
    print("2. Convert all .ts files in a folder")
    choice = input("Enter choice (1 or 2): ")

    if choice == '1':
        convert_single_file()
    elif choice == '2':
        convert_batch()
    else:
        print("❌ Invalid choice. Exiting.")

if __name__ == "__main__":
    main()
