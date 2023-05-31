# chatGPT_cli
This is a simple program created with ChatGPT to integrate ChatGPT API into the cli of Kali Linux. 

The main features are using ChatGPT API as regular chat function, or pass a file as an argument so you can chat with the AI about the contents of the file. You can refer to the file by name.
*You will need to insert your own API key and update the ChatGPT API model(if necessary) as noted in the code. 
Usage: 

python3 ./chatgpt_cli.py   
#This is for the regular chat function.

or

python3 ./chatgpt_cli.py /path/to/your/file   
#This is for passing a file to ChatGPT to chat about the file (It's always a good idea to refer to the OpenAI API documentation or reach out to their support for the most up-to-date information on file type and size limitations.)

or

python3 ./chatgpt_cli.py -h   
#Help information.
