# Threatscope: VirusTotal File Scanner

A Flask-based web tool to scan uploaded files using the VirusTotal API. Designed with a dark UI inspired by red team toolkits.

---

## Features

- Scan files using VirusTotal’s public API
- Displays detection categories: harmless, malicious, suspicious, undetected
- Caches scanned file hashes to avoid repeat lookups
- Flask-based lightweight web interface

---

## How to Run

1. **Install dependencies**
   ```bash
   pip install flask requests
   ```

2. **Configure your VirusTotal API key**  
   Edit `config.py`:
   ```python
   VT_API_KEY = "your_virustotal_api_key"
   ```

3. **Start the application**
   ```bash
   python app.py
   ```

4. Open your browser:
   ```
   http://localhost:5000
   ```

> For now, the application runs locally. You can also deploy it on any cloud platform or web server of your choice.  
> ✅ I have hosted mine on **Microsoft Azure**.

---

## Screenshots

| Home | Scan Result |
|------|-------------|
| ![Home](screenshots/home.png) | ![Result](screenshots/result.png) |

---

## Project Structure

```
FileGuardian/
├── app.py          # Flask application
├── config.py       # VirusTotal API key
├── scanner.py      # API logic and hash check
├── templates/
│   ├── index.html  # Upload UI
│   └── result.html # Result UI
└── static/         # (optional assets)
```

---

## License

MIT License — free to use, modify, and distribute.

---

## Author

Built by [YourName] — created for academic and portfolio purposes.
