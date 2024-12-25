import cv2

# Hardcoded positions for extracting fields from the cropped CIN card
FIELD_POSITIONS = {
    "name": (289, 89, 161, 54),
    "family_name": (288, 145, 167, 30),
    "date_of_birth": (460, 163, 139, 38),
    "place_of_birth": (295, 207, 338, 47),
    "id_number": (88, 375, 151, 68),
    "expiration_date": (561, 376, 115, 69),
    "arabic_name": (600, 71, 200, 45),
    "arabic_family_name": (616, 121, 184, 43),
    "place_of_birth_arabic": (584, 197, 187, 44),
}

def extract_fields(cropped_cin_path, debug=False):
    """
    Extracts predefined fields from a cropped CIN card.
    
    :param cropped_cin_path: Path to the cropped CIN card image
    :param debug: Boolean to save debug images for each field
    :return: Dictionary containing extracted field images
    """
    image = cv2.imread(cropped_cin_path)
    if image is None:
        raise ValueError(f"Could not read image: {cropped_cin_path}")

    extracted_fields = {}
    for field_name, (x, y, w, h) in FIELD_POSITIONS.items():
        cropped_field = image[y:y+h, x:x+w]
        extracted_fields[field_name] = cropped_field

        # Optionally save debug images for each field
        if debug:
            debug_path = f"debug_{field_name}.png"
            cv2.imwrite(debug_path, cropped_field)

    return extracted_fields
