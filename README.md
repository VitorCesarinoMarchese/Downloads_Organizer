# 🧹 Folder Organizer

A simple Python script to organize the contents of a folder into subfolders based on file types.

---

## 📦 Features

- Automatically moves files into categorized folders (e.g., Images, Documents, Music).
- File type categories are defined in an external JSON file.
- Easy to run from the command line.
- Handles unknown file types gracefully (optional extension).

---

## 📁 Example

Before:
```
Downloads/
├── image1.jpg
├── resume.pdf
├── song.mp3
├── video.mp4
├── script.py
```

After running the script:
```
Downloads/
├── Images/
│   └── image1.jpg
├── Documents/
│   └── resume.pdf
├── Music/
│   └── song.mp3
├── Videos/
│   └── video.mp4
├── Scripts/
│   └── script.py
```

---

## 🚀 Getting Started

### 1. Clone the repository (or copy the files)
```bash
git clone https://github.com/your-username/folder-organizer.git
cd folder-organizer
```

### 2. Add your file type categories

Create a file called `file_types.json`:

```json
{
  "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp"],
  "Documents": [".pdf", ".docx", ".txt", ".xlsx", ".pptx"],
  "Videos": [".mp4", ".mov", ".avi", ".mkv"],
  "Music": [".mp3", ".wav", ".aac"],
  "Archives": [".zip", ".rar", ".tar", ".gz"],
  "Scripts": [".py", ".js", ".sh"]
}
```

### 3. Run the script

```bash
python organizer.py /path/to/your/folder
```

---

## 🛠 How It Works

1. Loads file type mappings from `file_types.json`.
2. Scans the provided directory.
3. Moves each file into the corresponding subfolder based on extension.
4. Skips folders and already organized files.

---

## 📄 License

MIT License. Use it freely in personal or commercial projects.

---

## 🤝 Contributing

Pull requests are welcome! If you have ideas or improvements, feel free to open an issue or submit a PR.

