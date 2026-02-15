# QR Code Generator

A simple Python app, building a small desktop application that generates QR codes.

---

## Features

* Generate QR codes instantly
* Preview inside the application window
* Save as PNG image
* High error-correction (still scannable even if partially covered)
* Works offline
* Can be packaged into a `.exe` (no Python installation required)

---

## Setup (Development)

1. Create virtual environment

```
python -m venv .venv
```

3. Activate

Windows:

```
.venv\Scripts\activate
```

Mac/Linux:

```
source .venv/bin/activate
```

4. Install dependencies

```
pip install -r requirements.txt
```

---

## Run the Application

```
python qr_gui.py
```

A desktop window will appear.

---