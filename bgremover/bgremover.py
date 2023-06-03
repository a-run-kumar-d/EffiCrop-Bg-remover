"""Welcome to Pynecone! This file outlines the steps to create a basic app."""
from pcconfig import config

import pynecone as pc

docs_url = "https://pynecone.io/docs/getting-started/introduction"
filename = f"{config.app_name}/{config.app_name}.py"

style = {
    "font-family": "Verdana, sans-serif",
    "background" : "linear-gradient(114.29deg, #0B1926 -15.11%, #020606 106.05%)"
}

class State(pc.State):
    

    pass


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
            pc.upload(
                pc.center(
                    pc.text("Upload Here",color="#0B1926",font_size="15px", as_="b",),
                ),
                height ="69.3px",
                width="242.31px",
                background="#01F28D",
                padding="25px",
                border_radius="5px",
            ),
            # pc.button(
            #     "Upload Here",
            #     height ="69.3px",
            #     width="242.31px",
            #     background="#01F28D",
            #     color="#0B1926",
            # ),
            spacing="5em",
        ),
        padding_top = "30px",
    )


# Add state and page to the app.
app = pc.App(state=State, style=style)
app.add_page(index)
app.compile()
