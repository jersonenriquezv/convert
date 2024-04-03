# Image Format Converter

This Python script provides a simple way to convert images from WebP format to JPG. It's designed to watch a specified directory and automatically process any WebP images placed there, saving them as JPGs.

## How It Works

The script uses the `watchdog` library to monitor a directory for new WebP files. When a new file is detected, it uses the `Pillow` library to convert the image to a JPG format.

## Setup

### Prerequisites

- Python (The script is compatible with Python 3.8 and newer.)
- Pillow library for image processing
- Watchdog library for monitoring directory changes

Install the required libraries using `pip`:

bash
pip install Pillow watchdog

### Installation
git clone https://github.com/jersonenriquezv/convert.git
cd convert
### Run the script 
python convert.py




