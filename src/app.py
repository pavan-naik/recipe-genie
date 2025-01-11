import gradio as gr
from langchain_community.llms import VLLM

# Initialize vLLM
llm = VLLM(
    model="meta-llama/Llama-3.2-1B",
    trust_remote_code=True,
    max_new_tokens=512,
    top_k=10,
    top_p=0.95,
    temperature=0.8,
)

# Recipe prompt template from previous example
RECIPE_PROMPT = """You are a skilled chef and culinary expert. Create a detailed recipe for {dish_name} with the following format:

Recipe: {dish_name}

INGREDIENTS: List each ingredient with exact quantity and estimated price (USD)

NUTRITIONAL INFO:
1. Total calories
2. Protein
3. Carbs
4. Fat
5. Serving size

COOKING INSTRUCTIONS:
1. Step-by-step numbered process
2. Include cooking temperatures and times
3. Note any specific techniques or tips

CULTURAL BACKGROUND:
1. Origin of dish
2. Traditional serving occasions
3. Cultural significance
4. Regional variations

PREPARATION TIME:
1. Prep time
2. Cooking time
3. Total time

DIFFICULTY LEVEL: [Easy/Medium/Hard]

TOOLS NEEDED: List essential kitchen equipment

TIPS:
1. Storage recommendations
2. Substitution options
3. Serving suggestions

"""


def generate_recipe(dish_name):
    prompt = RECIPE_PROMPT.format(dish_name=dish_name)
    response = llm(prompt)
    return response


# Gradio interface
demo = gr.Interface(
    fn=generate_recipe,
    inputs=gr.Textbox(label="Enter dish name"),
    outputs=gr.Textbox(label="Generated Recipe", lines=20),
    title="Recipe Genie",
    description="AI-powered recipe generator with costs, nutrition facts, and cultural insights.",
    examples=["Pad Thai", "Butter Chicken", "Paella"],
)

if __name__ == "__main__":
    demo.launch()
