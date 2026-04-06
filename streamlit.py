import gradio as gr

from main import generate_plan


interface = gr.Interface(
    fn=generate_plan,
    inputs=[
        gr.Textbox(label="Destination"),
        gr.Textbox(label="Start Date"),
        gr.Textbox(label="End Date"),
        gr.Dropdown(["Low", "Medium", "Luxury"], label="Budget"),
        gr.CheckboxGroup(
            [
                "Beaches",
                "Mountains",
                "Adventure",
                "Food",
                "Culture",
                "Shopping",
                "Nature",
                "Nightlife",
            ],
            label="Travel Interests",
        ),
        gr.Slider(minimum=1, maximum=10, value=1, label="Number of Travelers"),
    ],
    outputs=gr.Textbox(label="Travel Plan"),
    title="🌍 AI Travel Planner",
    description="Plan your perfect trip easily.",
)


if __name__ == "__main__":
    interface.launch(share=True)
