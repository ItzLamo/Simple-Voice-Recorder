# Voice Recorder App

## Project Description
The **Voice Recorder App** is a user-friendly software designed for recording lectures, conversations, and other audio events. The application provides an easy-to-use graphical user interface (GUI) built using Python's Tkinter library. It leverages the capabilities of several Python modules to record and save audio as WAV files, ensuring high-quality output.

### Features
- **Intuitive GUI**: A sleek and interactive interface for smooth operation.
- **Timer Display**: Real-time timer showing the duration of the current recording.
- **High-Quality Audio Recording**: Records audio in WAV format using the `sounddevice` library.
- **Simple Save Options**: Save recordings with a user-defined filename to your desired location.

### Technologies Used
1. **Tkinter**: For creating the GUI.
2. **Sounddevice**: For capturing audio input.
3. **Wavio**: For saving the recorded audio as WAV files.
4. **Time**: For implementing the recording timer.
5. **Scipy**: For handling audio signals.

---

## Installation
To run this project, ensure you have Python installed on your system. Then, install the required libraries using the following commands:

```bash
pip install sounddevice
pip install wavio
pip install scipy
```

---

## Usage
1. Launch the application by running the Python script.
2. Click **Start Recording** to begin recording audio.
3. Monitor the recording duration using the built-in timer.
4. Click **Stop Recording** to end the recording.
5. Save the audio file by entering a filename and selecting the desired location.

---

## File Structure
- **voice_recorder.py**: Main Python script for the app.
- **assets/**: Folder containing optional images for enhancing the UI (if applicable).

---

## Preview
A sample screenshot of the application:

> ![image](https://github.com/user-attachments/assets/9e7e5e3b-d48c-451e-9fe4-80c9a2c763a8)


---

## Dependencies
- Python 3.7+
- `sounddevice`
- `wavio`
- `scipy`
- `tkinter`

---

## Contributing
Contributions are welcome! If you want to improve the app, please fork the repository and submit a pull request.

---

## License
This project is licensed under the MIT License. Feel free to use, modify, and distribute it.

---

## Acknowledgements
- Special thanks to the developers of the `sounddevice`, `wavio`, and `tkinter` libraries for making this project possible.

---

## Future Enhancements
- Add visualizations for audio signals.
- Enable playback of recorded audio within the app.
- Implement advanced audio editing features.

