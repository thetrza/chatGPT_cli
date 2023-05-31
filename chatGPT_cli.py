import openai
import sys

# Insert your API key from OpenAI
API_KEY = "your-api-key-here"

# If necessary update the ChatGPT API model
def chat(conversation):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=conversation
    )
    return response['choices'][0]['message']['content']

def start_chat(file_contents):
    if file_contents:
        file_name = file_contents.splitlines()[0].split("'")[1]
        prompt = f"ChatGPT@{file_name}"
    else:
        prompt = "ChatGPT"
    
    conversation = [
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": file_contents}
    ]
    
    print(f"\033[1;36m{prompt}:\033[0m", end=' ')
    
    while True:
        message = input()
        if message == 'exit':
            break
        conversation.append({"role": "user", "content": message})
        response = chat(conversation)
        print("\033[1;36mChatGPT:\033[0m", response)
        print(f"\033[1;36m{prompt}:\033[0m", end=' ')

def process_file(file_path):
    with open(file_path, 'r') as file:
        file_contents = file.read()
    file_name = file_path.split("/")[-1]
    file_contents_with_name = f"The file '{file_name}' contains:\n{file_contents}"
    
    while True:
        print("\033[1;36mChatGPT:\033[0m Would you like to print the contents of the file? (yes/no/exit)")
        print_contents = input().lower()
        
        if print_contents == 'yes':
            print("\033[1;36mChatGPT:\033[0m File Contents:")
            print(file_contents)
            break
        elif print_contents == 'no':
            break
        elif print_contents == 'exit':
            sys.exit()
        else:
            print("\033[1;36mChatGPT:\033[0m Invalid input. Please enter 'yes', 'no', or 'exit'.")
    
    print("\033[1;36mChatGPT:\033[0m You can now ask questions or continue the conversation.")
    start_chat(file_contents_with_name)

def print_help():
    print("Usage: chatgpt_cli.py [OPTIONS] [FILE]")
    print()
    print("Options:")
    print("  -h    Display this help message and exit")
    print()
    print("Arguments:")
    print("  FILE  Path to the input file")
    print()
    print("Description:")
    print("  This program allows you to chat with ChatGPT or process a file with ChatGPT.")
    print("  If a FILE is provided, the program will process the contents of the file.")
    print("  If no arguments are provided, the program enters chat mode, allowing you to interact with ChatGPT.")
    print()

def main():
    openai.api_key = API_KEY
    if len(sys.argv) > 1:
        if sys.argv[1] == "-h":
            print_help()
        else:
            file_path = sys.argv[1]
            process_file(file_path)
    else:
        start_chat("")

if __name__ == "__main__":
    main()
