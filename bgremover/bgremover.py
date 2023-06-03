"""Welcome to Pynecone! This file outlines the steps to create a basic app."""
from pcconfig import config

import pynecone as pc
import rembg as rbg

style = {
    "font-family": "Verdana, sans-serif",
    "background" : "linear-gradient(114.29deg, #0B1926 -15.11%, #020606 106.05%)"
}
image = ""
class passImage(pc.State):
    img: list[str]
    name = "choose files here"
    async def handle_upload(
        self, files: list[pc.UploadFile]
    ):
        for file in files:
            upload_data = await file.read()
            outfile = f".web/public/{file.filename}"
            with open(outfile, "wb") as file_object:
                file_object.write(upload_data)
            self.img.clear()
            self.img.append(file.filename)
    
    async def naming(
       self, files: list[pc.UploadFile]
    ):
        for file in files:
            self.name = file.filename
  
    def remove_data(self):
        self.img.clear()
    



def index() -> pc.Component:
    return pc.center(
        pc.vstack(
            pc.vstack(
                pc.image(src="/logo.png", width="267px", height="auto"),
                pc.text("Transform Your Images with a ", color="#E8FFF5", font_size="35px", as_="b",),
                pc.hstack(
                    pc.text("Single  ",color="#01F28D",font_size="35px",as_="b",),
                    pc.text("Click!",color="#E8FFF5",font_size="35px",as_="b",),
                    spacing ="10px",
                ),
                pc.text("Effortlessly Remove Backgrounds, Transform Images, and Unleash Your Creative Potential with", color="#E8FFF5", font_size="15px"),
                pc.text("Our Revolutionary Background Removal Tool", color="#E8FFF5", font_size="15px"),
                spacing=".5em",),
            pc.vstack(
                pc.upload(
                    pc.center(
                        pc.text(passImage.name,color="#0B1926",font_size="15px", as_="b",),
                    ),
                    height ="69.3px",
                    width="242.31px",
                    background="#01F28D",
                    padding="25px",
                    border_radius="5px",
                    accept={
                    "image/png": [".png"],
                    "image/jpeg": [".jpg", ".jpeg"],
                    "image/webp": [".webp"],
                    },
                    max_files=5,
                    disabled=False,
                    on_keyboard=True,
                    spacing="1em",
                ),
                pc.button(
                "Upload",
                on_click=lambda: passImage.handle_upload(
                    pc.upload_files()
                    ),
                ),
            ),
            pc.box(
            pc.foreach(
                passImage.img,
                lambda img: pc.vstack(
                    pc.text(img,color="#E8FFF5",),
                    pc.box(
                        pc.image(
                        src=img,
                        height="500px",
                        width="500px",
                        object_fit="cover",
                        ),
                    ),
                    pc.button(
                    "convert",
                    height ="69.3px",
                    width="242.31px",
                    background="#01F28D",
                    color="#0B1926",
                    margin_top="20px",
                ),
                ),
            ),
            spacing="5px",
            ),
            pc.vstack(
                pc.text("Effortlessly Remove Backgrounds, Transform Images, and Unleash Your Creative Potential with", color="#E8FFF5", font_size="15px"),
            margin_top="250px",
            ),
        ),
        padding_top = "30px",
    )


# Add state and page to the app.
app = pc.App(state=passImage, style=style)
app.add_page(index,on_load=passImage.remove_data)
app.compile()
