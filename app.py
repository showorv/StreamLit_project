import streamlit as st 
from api_calling import note_generator
from PIL import Image


#title
st.title("Note Summary and Quiz Generator")
st.markdown("Upload upto 3 images to generate Note summary and Quizzes")
st.divider()


with st.sidebar:
    st.header("Controls")

    #image
    images = st.file_uploader(
        "Upload the photos of your note",
        type=['jpg','jpeg','png'],
        accept_multiple_files=True
    )


    # pil_images = Image.open(images) for single image
    #for multiple
    pil_images = []

    for img in images:
        pil_img = Image.open(img)
        pil_images.append(pil_img)

    if images:


            
        if len(images)>3:
            st.error("Upload at max 3 images")
        else:
            st.subheader("Uploaded images")
            
            col = st.columns(len(images))

            

            for i,img in enumerate(images):
                with col[i]:
                    st.image(img)

    #difficulty 
    selected_option = st.selectbox(
        "Enter the difficulty of your quiz",
        ("Easy","Medium","Hard"),
        index = None
    )

    # if selected_option:
    #     st.markdown(f"You selected **{selected_option}** as dificulty")
    # else:
    #     st.error("Must select difficulty")

    pressed= st.button("Click the button to initiate AI",type="primary")

if pressed:
    if not images:
        st.error("Must be select 1 image")
    if not selected_option:
        st.error("Must select difficulty")


    if images and selected_option:

        #notes
        with st.container(border=True):

           
            st.subheader("Your note",anchor=False)

            with st.spinner("AI is writing notes for you"):
                note_generators = note_generator(pil_images)
                st.markdown(note_generators)
          #audio
        with st.container(border=True):

            st.subheader("Audio Transcript",anchor=False)
            st.text("will be replace by api call")
          #quiz
        with st.container(border=True):

            st.subheader("Quiz questions",anchor=False)
            st.text("will be replace by api call")
          #quiz answer
        with st.container(border=True):

            st.subheader("Answer",anchor=False)
            st.text("will be replace by api call")