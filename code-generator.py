import json
import os
from openai import OpenAI
from datetime import datetime
import re

api_key = input('OpenAI API Key: ')
print()

client = OpenAI(
    api_key=api_key
)

def translate_message(message: str, language: str = 'english') -> str:
    
    messages = []
    
    messages.append({
        "role": "system",
        "content": f"Translate the following message to {language}"
    })

    messages.append({
        "role": 'user',
        "content": message,
    })

    translator_stream = client.chat.completions.create(
        model="gpt-4-1106-preview",
        messages=messages,
    )

    return translator_stream.choices[0].message.content

def send_prompt(messages: list):
    formatted_messages = []

    for message in messages:
        formatted_messages.append({
            "role": "user",
            "content": message
        })

    chat = client.chat.completions.create(
        model="gpt-4-1106-preview",
        messages=formatted_messages
    )

    return chat.choices[0].message.content

user_language = input("Your lanuguage (program will follow the language you choose): " )

translated_phrase = translate_message('Input your project description: ', user_language)
raw_project_description = input(translated_phrase)
print()


while True:
    project_description = translate_message(raw_project_description)
    refinement_messages = [
        "Within a backend project scope, consider the following project description and point out any areas of ambiguity or potentially unintended outcomes. Also provide a revised version that solves the ambiguities. If there are no ambiguity points, respond with \"No changes needed\".",
        project_description
    ]

    suggestions = send_prompt(refinement_messages)
    translated_suggestions = translate_message(suggestions, user_language)

    print(translated_suggestions)
    print()

    translated_phrase = translate_message('Type your new project description or press enter to continue: ', user_language)
    user_input = input(translated_phrase)
    print()

    if user_input == "":
        break
    else:
        raw_project_description = user_input

generation_messages = [
    f"In the context of the following project description, the system must adhere to Robert C. Martin's clean architecture principles, with a \"Core\" module that will contain the project entities and interfaces for the use cases. Keep in mind to use dependency inversion to avoid higher abstraction level modules to depend on lower abstraction level modules. List all the system components that will be present in the final version os the project ordered by dependecy count (less dependent modules first), include a \"Root\" where the root level files will be if needed. Write the names as they will be in the project folders. Respond with only the module names as a JSON array without markdown formatting and without comments or explanations about your choices. Project description: {project_description}."
]

modules_response = send_prompt(generation_messages)
modules_response = re.sub(r'^```.*?\n', '', modules_response).removesuffix('\n```')
modules = json.loads(modules_response)

generation_messages.append(modules_response)

out_directory = f"./out/{datetime.now().strftime('%Y-%m-%dT%H-%M-%S')}/"

for module_name in modules:
    module_path = f"{out_directory}{module_name}/" if module_name != "Root" else out_directory

    if not os.path.exists(module_path):
        os.makedirs(module_path)

    generation_messages.append("You're now a senior developer that received this project description and modules and is starting to create the application")
    generation_messages.append(f"List all the files that need to be created for the component {module_name}, including a README file, as a JSON array whithout markdown formatting. Return raw json only without comments or any explanation about your choices. For files that should be inside a directory include the directory name in the file name, separating them with a /. Do not include the module directory in the file name. If it is the Root module, don't include files for other modules.")
    module_files_response = send_prompt(generation_messages)
    module_files_response = re.sub(r'^```.*?\n', '', module_files_response).removesuffix('\n```')

    module_files = json.loads(module_files_response)

    generation_messages.append(module_files_response)

    for file_name in module_files:
        directory_name = '\\'.join(file_name.split('/')[:-1])

        if len(directory_name) > 0 and not os.path.exists(f"{module_path}{directory_name}"):
            os.makedirs(f"{module_path}{directory_name}")

        generation_messages.append(f"Now develop the {file_name} file for the module {module_name}. Your responses should be raw code text only, without explanation and without markdown formatting wrapping the code.")

        file_content = send_prompt(generation_messages)
        file_content = re.sub(r'^```.*?\n', '', file_content).removesuffix('\n```')

        f = open(f"{module_path}{file_name}", "w")

        f.write(file_content)
        f.close()


print("Project generated!!!")