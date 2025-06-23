# 🐐 FatGoats BedrockAddonInstaller

Welcome to the FatGoats BedrockAddonInstaller — a one-click, Docker-powered web GUI for managing Minecraft Bedrock Server packs with style and simplicity.

---

## 🧠 What Is This?

This tool allows you to:

- Upload `.mcpack` and `.mcaddon` files
- Automatically extract and sync them to Bedrock worlds
- View and manage your worlds and their associated packs
- Run everything in a dark-mode themed web GUI on port `43287`
- Use a portable Docker container so it's cross-platform and easy to install

---

## 🚀 How To Use

### 📦 1. Clone and Build

```bash
git clone https://github.com/YourUsername/FatGoats-BedrockAddonInstaller.git
cd FatGoats-BedrockAddonInstaller
docker-compose up --build
```

Then visit: [http://localhost:43287](http://localhost:43287)

---

### 📁 2. Folder Structure

| Folder        | Purpose                                  |
|---------------|-------------------------------------------|
| `backend/`    | Python Flask app                         |
| `frontend/`   | HTML, CSS, and JS for GUI                |
| `packs/`      | Uploaded `.mcpack` / `.mcaddon` files    |
| `data/`       | Mounted Minecraft Bedrock server folder  |

---

## 🌐 Web Interface Features

- Drag-and-drop upload for `.mcpack`/`.mcaddon`
- Sync button to auto-integrate packs into all worlds
- Pack manifest reader: shows UUID, type, version
- Tooltips for beginners
- FatGoats favicon + logo ready to customize

---

## 🔌 API Endpoints

| Endpoint       | Method | Description                    |
|----------------|--------|--------------------------------|
| `/upload`      | POST   | Upload and extract packs       |
| `/sync`        | POST   | Sync packs to all worlds       |
| `/worlds`      | GET    | List available worlds          |

---

## 🧪 Sample Screenshot

> 🖼️ _Replace this with a screenshot later!_

![screenshot-placeholder](https://placehold.co/600x400?text=FatGoats+GUI+Here)

---

## 🛠 Roadmap

- [x] Upload & extract packs
- [x] Sync into BDS world configs
- [ ] Rename/delete/clone worlds
- [ ] Edit server.properties from GUI
- [ ] Restart BDS from button
- [ ] View server logs from browser
- [ ] Toggle light/dark mode

---

## 🤝 Contributing

We welcome pull requests, issues, and feedback! Feel free to fork and suggest changes.

---

## 📜 License

MIT — do whatever you want, just don’t remove the 🐐

---

## 💖 Support

Like it? Consider donating or crediting **FatGoats**! Ko-fi support coming soon.

---

## 🧑‍💻 Author

Tyler "FatGoats" Sciullo

## 🖥️ Optional: Run Without Docker (Windows EXE)

We included a `fatgoats_installer.py` script you can convert into a standalone EXE.

### 🔨 Steps to Build the EXE

1. Install Python 3.10+
2. Install dependencies:
   ```bash
   pip install flask
   pip install pyinstaller
   ```
3. Build it:
   ```bash
   pyinstaller --onefile fatgoats_installer.py
   ```

4. Run the EXE:
   ```bash
   dist\fatgoats_installer.exe
   ```

5. Visit [http://localhost:43287](http://localhost:43287) in your browser

This version will serve the web interface just like the Docker one — but runs as a native Windows EXE without installing Docker.

_Include `frontend/`, `packs/`, and `backend/` in the same folder!_
