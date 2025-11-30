from dotenv import load_dotenv
load_dotenv()   # loads .env into environment BEFORE importing your own modules

from launchlog.cli import main

if __name__ == "__main__":
    main()
