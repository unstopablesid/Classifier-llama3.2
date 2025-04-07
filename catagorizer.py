import ollama
import os

model = "llama3.2"

input_file ="./data/Grocery_list.txt"
output_file = "./data/Catagorized_list.txt"

if not os.path.exists(input_file):
    print(f"Input file '{input_file}' does not exist.")
    exit(1)

with open(input_file, "r") as f:
    items = f.read().strip()



prompt = f"""
You are a grocery list categorizer. You will be given a list of grocery items, and you need to categorize them into different sections.


here is the list of grocery items:

{items}

please:
1. categorize the items into sections like dairy, vegetables, fruits, etc.
2. write the categorized list in a markdown format.
3. do not add any additional information or explanations.

""" 
### Send the prompt and get the response
try:
    response = ollama.generate(model=model, prompt=prompt)
    generated_text = response.get("response", "")
    print("Generated Text:")
    print("=================Catagorized List================\n")
    print(generated_text)
    with open(output_file, "w") as f:
        f.write(generated_text.strip())

    print(f"Categorized list saved to '{output_file}'.")
except Exception as e:
    print(f"An error occurred: str{e}")
    