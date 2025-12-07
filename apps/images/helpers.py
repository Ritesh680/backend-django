import re


def get_public_id_from_url(url):
    """Get the public ID from the image URL"""

    # regex should match after upload word
    return re.search(r"\/upload\/(.*)\.(jpg|jpeg|png|gif|webp)$", url).group(1)
