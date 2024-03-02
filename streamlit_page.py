import io
import localizeconst
import streamlit as st
from PIL import Image
from clip_classifier import ClipClassifier


@st.cache_data()
def load_clip_classifier():
    return ClipClassifier()


def load_image():
    """Создание формы для загрузки изображения"""
    uploaded_file = st.file_uploader(label=localizeconst.CHOOSE_IMAGE)

    if uploaded_file is None:
        return None
    
    image_data = uploaded_file.getvalue()
    st.image(image_data)
    return Image.open(io.BytesIO(image_data))


def main():
    st.title(localizeconst.IMAGE_CLASSIFICATION_TITLE)
    img = load_image()
    labels_input = st.text_input(localizeconst.ENTER_CLASSES_INSTRUCTION)
   
    run_button = st.button(localizeconst.LAUNCH_CLASSIFICATION)
    if not run_button:
        return
    
    labels = labels_input.split(',')
    if len(labels) <= 0 or labels[0] == '':
        st.error(localizeconst.NO_CLASSES_ERROR)
        return

    if img is None:
        st.error(localizeconst.NO_IMAGE_ERROR)
        return

    model = load_clip_classifier()
    with st.spinner(localizeconst.SPINNER_WAITING):
        label, score = model.predict(img, labels)
        st.write(localizeconst.CLASSIFICATION_RESULT_LABEL.format(label, int(score * 100)))


if __name__ == "__main__":
    main()
