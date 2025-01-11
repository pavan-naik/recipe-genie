import gradio as gr
from transformers import pipeline
import os
from huggingface_hub import login

login(token=os.getenv('HF_TOKEN'))


def setup_pipeline():
    # return pipeline(
    #     "text-generation",
    #     model="meta-llama/Llama-3.2-1B",  # Smaller model suitable for CPU
    #     device=-1  # Force CPU
    # )
    return None

def generate_recipe(dish_name):
    if not dish_name:
        return "Please enter a dish name"
    
    try:
        
        prompt = f"""Create a recipe for {dish_name} including:
        - Ingredients with quantities
        - Steps to cook
        - Cultural background"""
        
        result = generator(prompt, max_length=500, num_return_sequences=1)
        return result[0]['generated_text']
    except Exception as e:
        return f"Error: {str(e)}"
    
generator = setup_pipeline()

demo = gr.Interface(
    fn=generate_recipe,
    inputs=gr.Textbox(label="Enter dish name"),
    outputs=gr.Textbox(label="Generated Recipe", lines=20),
    title="RecipeGenie",
    description="AI-powered recipe generator"
)

if __name__ == "__main__":
    demo.launch()

