import streamlit as st
from PIL import Image
from models.segmentation_model import load_segmentation_model, segment_image
from models.identification_model import load_identification_model, generate_description
from models.text_extraction_model import load_text_extraction_model, extract_text
from models.summarization_model import save_descriptions_to_db
from utils.preprocessing import load_image
from utils.postprocessing import save_segmented_objects
from utils.data_mapping import map_data
from utils.visualization import visualize_output

st.title("Image Segmentation and Data Extraction Pipeline")

uploaded_file = st.file_uploader("Choose an image...", type="jpg")

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption='Uploaded Image', use_column_width=True)
    
    st.write("Processing...")
    image_path = f"data/input_images/{uploaded_file.name}"
    image.save(image_path)

    try:
        predictor = load_segmentation_model()
        image_cv = load_image(image_path)
        instances, class_names = segment_image(predictor, image_cv)
        segmented_objects = save_segmented_objects(image_cv, instances, class_names, "data/segmented_objects")

        processor, model = load_identification_model()
        reader = load_text_extraction_model()

        descriptions = []
        for instance_image, class_name in segmented_objects:
            description = generate_description(processor, model, instance_image)
            text = extract_text(reader, instance_image)
            descriptions.append({"object": class_name, "text": text, "description": description})

        save_descriptions_to_db(descriptions)
        data_mapping = map_data(instances, class_names, descriptions, "data/output/data_mapping.json")
        visualize_output(image_cv, instances, class_names, descriptions, data_mapping)

    except Exception as e:
        st.write(f"Error: {e}")

st.write("Process Completed!")
