## Getting Started

### Prerequisites
 npm
    
    npm install npm@latest -g

### Installation

### Task 1: Backend

**Step 1:** Clone the repository and navigate to the backend folder.

**Step 2:** Go into routes.py and place in this line:

`openai.api_key = os.getenv("OPENAI_API_KEY","<place your api key>")`

**Step 3:** Create a `.env` file with the following information:

`OPENAI_API_KEY= <place your api key>`

**Step 3:** In the terminal, run the command:

`docker compose up`

This will start the backend, which runs on port 8000.

---

### Task 2: Frontend

**Step 1:** Navigate to the `llm-app` folder.

**Step 2:** In the terminal, run the command to install the dependencies required to run the app:

`npm install`

**Step 3:** Then run the command to start the application:

`npm run dev`

This will start the frontend. Please note that the frontend is not complete and has a few issues due to limited time and a busy schedule.
