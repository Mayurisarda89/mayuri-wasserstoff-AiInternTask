# mayuri-wasserstoff-AiInternTask

##  Image Segmentation and Data Extraction Pipeline
### Project Overview
This project aims to develop a pipeline for image segmentation, data extraction, and generating structured outputs, including data mapping and visualizations. The pipeline is designed to be user-friendly and interactive, leveraging a Streamlit UI to allow users to upload images and process them through various stages of the pipeline.

### Setup Instructions
#### Prerequisites
Python 3.8 or later
pip (Python package installer)
### Installation
#### Clone the repository:
git clone <repository_url>
cd project_root
#### Install the required packages:
pip install -r requirements.txt

### Usage Instructions
Run the Streamlit application:
streamlit run streamlit.py
#### Upload an input image:

Navigate to the Streamlit UI in your web browser.
Use the file upload widget to upload an image.
#### Process the image:

The application will process the uploaded image through segmentation, text extraction, and summarization.
View the segmented objects, descriptions, and extracted text.
#### View final output:

The final output image with annotations will be displayed.
A table containing all mapped data for each object in the master image will be presented.
Streamlit UI Features
#### File Upload:

Allows users to upload an input image for processing.
#### Segmentation Display:

Displays the segmented objects on the original image with bounding boxes and labels.
#### Object Details:

Shows extracted object images with unique IDs.
Displays descriptions, extracted text/data, and summarized attributes for each object.
#### Final Output:

Displays the final output image with annotations.
Presents a table containing all mapped data for each object in the master image.
#### User Interaction:

Allows users to interact with and review each step of the pipeline.
Challenges and Solutions
#### Model Compatibility:

Issue: Ensuring compatibility between Detectron2 and Torch versions.
Solution: Proper dependency management and installation order.
#### Corrupted Files:

Issue: Handling truncated/corrupted model files.
Solution: Validating file integrity before loading.
#### Performance Optimization:

Issue: Efficient processing for large images and complex segmentations.
Solution: Implementing optimized image processing techniques.
## Future Improvements
Enhance UI: Improve the user interface for better interaction and usability.
Robust Error Handling: Implement more robust error handling mechanisms.
Model Accuracy: Explore additional models for improved segmentation and text extraction accuracy.
