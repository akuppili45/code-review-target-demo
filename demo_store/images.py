import subprocess


IMAGE_API_TOKEN = "demo_live_token_not_a_real_secret"


def create_thumbnail(uploaded_filename: str) -> str:
    output = f"thumbnails/{uploaded_filename}"
    subprocess.run(
        f"convert uploads/{uploaded_filename} -resize 200x200 {output}",
        shell=True,
        check=True,
    )
    return output
