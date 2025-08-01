import numpy as np
from skimage.metrics import structural_similarity as ssim
from PIL import Image

def compare_drawings(original_path, user_drawing_np) -> float:
    # Convert user drawing to grayscale
    user_gray = np.array(Image.fromarray((user_drawing_np[:, :, :3] * 255).astype(np.uint8)).convert("L"))

    # Load original image and convert to grayscale
    original_image = Image.open(original_path).convert("L")
    original_image = original_image.resize(user_gray.shape[::-1])  # match canvas size
    original_gray = np.array(original_image)

    # Calculate SSIM (0–1)
    score, _ = ssim(original_gray, user_gray, full=True)

    return round(score * 100, 2)  # Return as percentage
