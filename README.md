# Multi-Feature Desktop Application using Tkinter

This Python application provides a graphical user interface (GUI) built using Tkinter, offering various functionalities and features accessible through buttons. Each button corresponds to a specific action, from opening applications to performing tasks like capturing video or generating QR codes.

## Features

- **Open Notepad & Calculator**: Launches the Notepad and Calculator applications respectively using subprocess.
- **Open YouTube**: Opens a web browser window to search for and play a user-specified song on YouTube.
- **Deaf People Help**: Utilizes computer vision to assist deaf individuals by recognizing hand gestures and providing corresponding audio feedback.
- **Capture Video**: Captures video from the default camera and saves it as a video file.
- **Get Weather Update**: Planned feature for retrieving weather information using an API (implementation pending).
- **Voice Assistant**: Utilizes speech recognition to process voice commands and provide feedback accordingly.
- **Generate QR Code**: Creates a QR code from user-provided text or URL using the qrcode library.
- **Your Additional Feature**: Placeholder for adding custom functionalities or integrating additional APIs.

## Installation

1. **Install Required Libraries**: Ensure that the necessary Python libraries are installed. You can install them using pip:

    ```bash
    pip install pyttsx3 speechrecognition qrcode opencv-python-headless
    ```

2. **Run the Application**: Execute the Python script provided (`desktop_app.py` or any preferred filename) using a Python interpreter.

    ```bash
    python desktop_app.py
    ```

3. **Interact with the GUI**: Click on the buttons to perform various actions as described above.

4. **Exit the Application**: Click on the "Exit" button to close the application.

## Dependencies

- **Tkinter**: Standard GUI library for Python.
- **Subprocess**: Module for spawning new processes.
- **Pyttsx3**: Text-to-speech conversion library for generating audio output.
- **SpeechRecognition**: Library for performing speech recognition.
- **Qrcode**: Library for generating QR codes.
- **OpenCV**: Computer vision library for processing images and video (headless version used).

## Notes

- The application provides a convenient way to access various functionalities through a simple graphical interface.
- Some features like weather updates may require additional API integration, which can be implemented based on specific requirements.
- Ensure that your system has the necessary dependencies installed and configured correctly.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
