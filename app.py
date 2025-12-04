from dotenv import load_dotenv

from launchlog.cli import main

load_dotenv()  # loads .env into environment BEFORE importing your own modules

if __name__ == "__main__":
    main()
