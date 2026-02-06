# Computer Vision Security System

A real-time security monitoring application that detects people, weapons (knives), and identifies individuals using face recognition. Built with YOLOv8 for efficient object detection and OpenCV for computer vision processing.

## Features

- **Real-time Detection**: Detects people and weapons in live video streams
- **Face Recognition**: Identifies individuals from reference images
- **YOLOv8 Integration**: State-of-the-art object detection model
- **Webcam Support**: Works with any connected camera device
- **Alert System**: Generates alerts for detected threats
- **Easy Configuration**: Customizable detection settings and reference images

## Quick Start

1. Clone or download the repository
2. Install Visual C++ Redistributable (see Prerequisites below)
3. Run the setup script or follow manual installation steps
4. That's it! Simply run `python main.py`

## Prerequisites

### System Requirements

- **OS**: Windows 10 or later
- **Python**: 3.8 or higher
- **RAM**: Minimum 4GB (8GB recommended)
- **Disk Space**: At least 1GB for dependencies and models
- **Webcam**: Compatible USB or built-in camera

### Required Software

- **Visual C++ Redistributable**: Download from [Microsoft](https://aka.ms/vs/17/release/vc_redist.x64.exe)

## Installation

### Why Clone is Lightweight

The repository is kept lightweight because:
- **Virtual Environment** (`venv/`) is gitignored - each user creates their own
- **Installed Packages** are not committed - users install them locally with `pip install -r requirements.txt`
- **Model Files** (`yolov8n.pt`) are gitignored - automatically downloaded on first run
- **Python Cache** (`__pycache__/`) is gitignored

This is why cloning is fast and the repo stays small!

### Step 1: Install Visual C++ Redistributable

This Windows component is required to run PyTorch and CUDA dependencies.

1. Download the installer from the link above
2. Run the executable file
3. Click "Install" and follow the prompts
4. Restart your computer if prompted





### Step 2: Clone or Download Project

Navigate to your desired directory and obtain the project files.

### Step 3: Set Up Python Virtual Environment

Open PowerShell or Command Prompt and navigate to the project directory:

```powershell
cd "d:\New folder"
```

Create and activate the virtual environment:

```powershell
python -m venv venv
venv\Scripts\activate
```

You should see `(venv)` at the beginning of your command line prompt.

### Step 4: Install Dependencies

With the virtual environment activated, install all required packages from `requirements.txt`:

```powershell
pip install -r requirements.txt
```

This single command installs all dependencies listed in the project's `requirements.txt` file, just like `npm install` in web development projects.

## Usage

### Running the Application

Ensure your virtual environment is activated, then execute:

```powershell
python main.py
```

A window will open displaying your webcam feed with real-time detection overlays.

### Keyboard Controls

| Key | Action |
|-----|--------|
| `q` | Quit the application |

### Detection Output

The application displays:
- **Bounding boxes** around detected people and weapons
- **Confidence scores** for each detection
- **Recognized faces** with identity labels (if configured)
- **Alert notifications** for threats

## Configuration

### Adding Face Recognition

To enable face recognition, add reference images:

1. Create a folder named `reference_images` in the project directory (if it doesn't exist)
2. Add clear facial images with filenames matching the person's name:
   ```
   reference_images/
   ├── John.jpg
   ├── Mary.png
   ├── Michael.jpg
   └── Sarah.png
   ```
3. Restart the application

**Best Practices for Reference Images**:
- Use high-quality, clear photos
- Ensure faces are well-lit and frontal
- Use at least one image per person (multiple angles recommended)
- Standard image formats: JPG, PNG

### Model Files

The YOLOv8 model (`yolov8n.pt`) is automatically downloaded on first run. Ensure you have stable internet connectivity during initial startup.

## Project Structure

```
.
├── main.py              # Application entry point
├── detector.py          # YOLO object detection module
├── recognizer.py        # Face recognition module
├── alert.py             # Alert notification system
├── yolov8n.pt           # YOLOv8 nano model weights
├── reference_images/    # Face recognition database
├── requirements.txt     # Python dependencies (like package.json)
├── venv/                # Python virtual environment
└── README.md            # This file
```

## Troubleshooting

### Error: "No module named 'cv2'"

OpenCV is not installed. Reinstall dependencies:

```powershell
pip install -r requirements.txt --upgrade
```

### Error: "Could not open camera" or "Failed to open camera"

**Solutions**:
1. Ensure no other application is using your webcam
   - Close Zoom, Skype, Teams, or other video conferencing apps
   - Check browser tabs with camera access
2. Verify camera hardware:
   - Check Device Manager (devmgmt.msc) for camera listing
   - Test camera with another application
3. Restart the application
4. Reconnect the USB camera (if external)

### Camera Permission Denied

Windows may prompt for camera access:
1. Click "Allow" when the permission dialog appears
2. If prompted in Settings, enable camera access for the Python application
3. Check Privacy & Security settings in Windows

### Model Download Issues

If `yolov8n.pt` fails to download:

```powershell
pip install --upgrade ultralytics
python -c "from ultralytics import YOLO; YOLO('yolov8n.pt')"
```

### Poor Detection Performance

- Ensure adequate lighting in the monitored area
- Adjust camera angle for optimal coverage
- Verify minimum Python version requirements
- Check system resources (CPU/RAM usage)

### Virtual Environment Activation Issues

If `(venv)` does not appear after activation:

```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
venv\Scripts\Activate.ps1
```

## License

[Add your license here]

## Support

For issues, questions, or feature requests, please create an issue or contact the development team.

