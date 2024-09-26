import tkinter as tk
from tkinter import filedialog
import customtkinter
import cv2
import easyocr
import pytesseract
import keras_ocr
import torch
import numpy as np
from PIL import Image, ImageTk
import threading

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
# Define functions first
def select_gpu():
    if torch.cuda.is_available():
        gpu_count = torch.cuda.device_count()
        gpu_names = [torch.cuda.get_device_name(i) for i in range(gpu_count)]
        return gpu_names
    return ["No GPU available"]

def preprocess_image(image_path, preprocessing_method):
    image = cv2.imread(image_path)
    if preprocessing_method == "Grayscale":
        return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    elif preprocessing_method == "Threshold":
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        return cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]
    elif preprocessing_method == "Denoise":
        return cv2.fastNlMeansDenoisingColored(image, None, 10, 10, 7, 21)
    else:
        return image

def perform_ocr(image_path, method):
    try:
        preprocessing_method = preprocessing_combobox.get()
        if preprocessing_method != "None":
            preprocessed_image = preprocess_image(image_path, preprocessing_method)
            cv2.imwrite("temp_preprocessed.jpg", preprocessed_image)
            image_path = "temp_preprocessed.jpg"

        if method == "EasyOCR":
            reader = easyocr.Reader(['en', 'ar'])
            result = reader.readtext(image_path)
            # Filter out unsupported characters
            text = ' '.join([text[1] for text in result])
            return text.encode('utf-8', 'ignore').decode('utf-8')  # Ignore unsupported characters
        elif method == "Pytesseract":
            image = Image.open(image_path)
            return pytesseract.image_to_string(image)
        elif method == "Keras-OCR":
            pipeline = keras_ocr.pipeline.Pipeline()
            images = [keras_ocr.tools.read(image_path)]
            prediction_groups = pipeline.recognize(images)
            return ' '.join([text[0] for text in prediction_groups[0]])
        else:
            return "Invalid OCR method selected"
    except Exception as e:
        return f"Error performing OCR: {str(e)}"

def upload_image():
    file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.png *.jpg *.jpeg *.bmp *.tiff")])
    if file_path:
        image = Image.open(file_path)
        image.thumbnail((window_width // 2 - 100, window_height - 100))  # Resize image to fit the window
        photo = ImageTk.PhotoImage(image)
        image_label.configure(image=photo, text="")
        image_label.image = photo
        window.image_path = file_path

def perform_ocr_thread():
    progress_bar.start()
    result = perform_ocr(window.image_path, ocr_combobox.get())
    result_label.configure(text=result)
    progress_bar.stop()
    progress_bar.set(0)

def perform_ocr_on_image():
    if hasattr(window, 'image_path'):
        ocr_method = ocr_combobox.get()
        gpu = gpu_combobox.get()
        
        if gpu != "No GPU available":
            torch.cuda.set_device(gpu_names.index(gpu))
        
        threading.Thread(target=perform_ocr_thread).start()
    else:
        result_label.configure(text="Please upload an image first.")

# Set up the main window
customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

window = customtkinter.CTk()
window.title("Document Scanner")

# Get screen dimensions
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

# Set window size to 80% of screen size
window_width = int(screen_width * 0.8)
window_height = int(screen_height * 0.8)
window.geometry(f"{window_width}x{window_height}")

# Create main frame
main_frame = customtkinter.CTkFrame(window)
main_frame.pack(fill="both", expand=True, padx=20, pady=20)

# Create left frame for controls
left_frame = customtkinter.CTkFrame(main_frame, width=200)
left_frame.pack(side="left", fill="y", padx=(0, 20))

# Create right frame for image and results
right_frame = customtkinter.CTkFrame(main_frame)
right_frame.pack(side="right", fill="both", expand=True)

# Create frame for image display
image_frame = customtkinter.CTkFrame(right_frame)
image_frame.pack(side="left", fill="both", expand=True, padx=(0, 10))

# Create frame for OCR results
result_frame = customtkinter.CTkFrame(right_frame)
result_frame.pack(side="right", fill="both", expand=True, padx=(10, 0))

# Image display
image_label = customtkinter.CTkLabel(image_frame, text="No image selected")
image_label.pack(pady=10, fill="both", expand=True)

# OCR result display
result_label = customtkinter.CTkLabel(result_frame, text="OCR Result will appear here")
result_label.pack(pady=10, fill="both", expand=True)

# OCR method selection
ocr_methods = ["EasyOCR", "Pytesseract", "Keras-OCR"]
ocr_combobox = customtkinter.CTkComboBox(left_frame, values=ocr_methods, width=180)
ocr_combobox.pack(pady=10)
ocr_combobox.set("Select OCR method")

# GPU selection
gpu_names = select_gpu()
gpu_combobox = customtkinter.CTkComboBox(left_frame, values=gpu_names, width=180)
gpu_combobox.pack(pady=10)
gpu_combobox.set("Select GPU")

# Preprocessing method selection
preprocessing_methods = ["None", "Grayscale", "Threshold", "Denoise"]
preprocessing_combobox = customtkinter.CTkComboBox(left_frame, values=preprocessing_methods, width=180)
preprocessing_combobox.pack(pady=10)
preprocessing_combobox.set("Select preprocessing")

# Button to upload image
upload_button = customtkinter.CTkButton(left_frame, text="Upload Image", command=upload_image, width=180)
upload_button.pack(pady=10)

# Button to perform OCR
ocr_button = customtkinter.CTkButton(left_frame, text="Perform OCR", command=perform_ocr_on_image, width=180)
ocr_button.pack(pady=10)

# Progress bar for OCR processing
progress_bar = customtkinter.CTkProgressBar(left_frame, width=180)
progress_bar.pack(pady=10)
progress_bar.set(0)

# Start the Tkinter event loop
window.mainloop()

