import streamlit as st
import random
import os
from PIL import Image
import time
from streamlit_drawable_canvas import st_canvas
from scoring import compare_drawings
import numpy as np

# --- Set up folder paths ---
ASSETS_PATH = os.path.join(os.path.dirname(__file__), "..", "assets")
ASSETS_PATH = os.path.abspath(ASSETS_PATH)
DIFFICULTY_LEVELS = ['easy', 'medium', 'hard']

# --- Sidebar: Difficulty selection ---
st.sidebar.title("EchoTrainer")
difficulty = st.sidebar.selectbox("Choose difficulty:", DIFFICULTY_LEVELS)

# --- Get all images from selected difficulty folder ---
image_folder = os.path.join(ASSETS_PATH, difficulty)
image_files = [f for f in os.listdir(image_folder) if f.endswith(".png")]

# --- Randomly select one ---
if image_files:
    selected_image_file = random.choice(image_files)
    selected_image_path = os.path.join(image_folder, selected_image_file)
    image = Image.open(selected_image_path)

    st.session_state["current_image_path"] = selected_image_path  # Save for later use
    st.image(image, caption=f"Memorize this shape!", use_container_width=True)
else:
    st.warning("No images found in the selected difficulty folder.")


if st.button('Start Round'):
    st.session_state['game_started'] = True

difficulty_times = {'easy' : 5, 'medium' : 3, 'hard' : 2}


if 'game_started' in st.session_state and st.session_state['game_started']:
    st.image(image, caption = 'Memorise this!', use_container_width=True)

    time.sleep(difficulty_times)
    st.empty()

    st.write('Now draw from memory :')

    canvas_result = st_canvas(
        fill_color="black",
        stroke_width=5,
        stroke_color="black",
        background_color="white",
        height=256,
        width=256,
        drawing_mode="freedraw",
        key="canvas",
    )

    if st.button('Submit Drawing'):
        if canvas_result.image_data is not None:
            st.session_state["user_drawing"] = canvas_result.image_data
            st.success("Drawing submitted!")

            user_img = Image.fromarray((st.session_state["user_drawing"][:, :, :3] * 255).astype(np.uint8))
            original_img = Image.open(st.session_state["current_image_path"])
            original_img = original_img.resize(user_img.size)

            col1, col2 = st.columns(2)

            with col1:
                st.markdown("### 🎯 Original Shape")
                st.image(original_img, use_container_width=True)

            with col2:
                st.markdown("### ✏️ Your Drawing")
                st.image(user_img, use_container_width=True)


            score = compare_drawings(
            st.session_state["current_image_path"],
            st.session_state["user_drawing"]
        )

        st.markdown(f"### 🧠 Similarity Score: `{score}%`")

        # Optional feedback
        if score > 85:
            st.success("Excellent memory! 🎯")
        elif score > 60:
            st.info("Good job! You remembered most of it. 🧠")
        else:
            st.warning("Tough one! Want to try again? 🔁")
    else:
        st.warning("Please draw something before submitting.")




if st.button("🔄 Play Again"):
    # Reset all relevant session variables
    for key in ["game_started", "user_drawing", "current_image_path"]:
        if key in st.session_state:
            del st.session_state[key]
    
    # Rerun the app from the top (fresh round)
    st.experimental_rerun()
