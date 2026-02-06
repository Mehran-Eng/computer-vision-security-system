# Computer Vision Security System - How to Run

## Step 1: Install Visual C++ Redistributable (Required)
Your system needs this Windows component to run PyTorch.

1. Download from: https://aka.ms/vs/17/release/vc_redist.x64.exe
2. Run the downloaded file
3. Click "Install"
4. Wait for installation to complete

## Step 2: Open Terminal
1. Open PowerShell or Command Prompt
2. Navigate to the project folder:
   ```powershell
   cd "d:\New folder"
   ```

## Step 3: Activate Virtual Environment
```powershell
venv\Scripts\activate
```
You should see `(venv)` appear at the start of your command line.

## Step 4: Run the Application
```powershell
python main.py
```

## Step 5: Using the Application
- A window will open showing your webcam feed
- The system will detect people and weapons (knives)
- Press **'q'** to quit the application

## Optional: Add Face Recognition
1. Create a folder called `reference_images` in the project directory
2. Add photos of people you want to identify (e.g., `John.jpg`, `Mary.png`)
3. Restart the application

## Troubleshooting

### Error: "No module named 'cv2'"
Run this command:
```powershell
venv\Scripts\python -m pip install opencv-python ultralytics numpy
```

### Error: "Could not open camera"
- Make sure no other application is using your webcam
- Try closing Zoom, Skype, or other video apps

### Camera Permission
- Windows may ask for camera permission - click "Allow"
