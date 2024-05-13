
def print_welcome_message():
    print("Welcome to the CV Generator!")
    print("This tool will help you create your CV.")

def read_template(template_path):
    try:
        with open(template_path, 'r') as file:
            return file.read()
    except FileNotFoundError:
        raise FileNotFoundError("Template file not found.")

def parse_template(template_string):
    language_parts = []
    stripped_template = template_string
    while '{' in stripped_template:
        start_index = stripped_template.find('{')
        end_index = stripped_template.find('}')
        language_part = stripped_template[start_index + 1:end_index]
        language_parts.append(language_part)
        stripped_template = stripped_template[:start_index] + stripped_template[end_index + 1:]
    return stripped_template.strip(), tuple(language_parts)


def prompt_user_for_input(language_parts):
    user_inputs = {}
    for part in language_parts:
        user_input = input(f"Enter your {part.replace('_', ' ').title()}: ")
        user_inputs[part] = user_input
    return user_inputs

def merge(template_string, user_inputs):
    for placeholder, value in user_inputs.items():
        template_string = template_string.replace("{" + placeholder + "}", value)
    return template_string

def generate_cv():
    pass

def write_to_file(output_path, cv_content):
    with open(output_path, 'w') as file:
        file.write(cv_content)


def main():
    print_welcome_message()
    template_path = "assets/cv_template.txt"
    template_content = read_template(template_path)
    language_parts = parse_template(template_content)
    user_inputs = prompt_user_for_input(language_parts)
    completed_cv = merge(template_content, user_inputs)
    output_path = "cv_output.txt"
    write_to_file(output_path, completed_cv)
    print("CV successfully generated. Check cv_output.txt for the result.")

if __name__ == "__main__":
    main()
