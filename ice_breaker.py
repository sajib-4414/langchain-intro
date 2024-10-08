import os
from dotenv import load_dotenv
if __name__ == "__main__":
    load_dotenv()
    print("hello langchjain")
    print(os.environ['COOL_API_KEY'])
