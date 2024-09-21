# LLM Conversations Backend

## Overview

This backend component allows CRUD operations for conversations containing queries and responses with an LLM (OpenAI GPT-3.5 Turbo). It uses FastAPI, Beanie, and MongoDB.

## Features

1. CRUD operations for conversations.
2. Sends prompts to LLM and retrieves responses.
3. Maintains conversation history as context.
4. Anonymizes and stores prompts and responses for auditing.

## Tech Stack

- Python >= 3.8
- FastAPI
- Beanie (MongoDB ODM)
- OpenAI Python Client
- Docker

## Getting Started

### Prerequisites

- Docker and Docker Compose installed

### Running the Application

1. Clone this repository.
2. Navigate to the project directory.
3. Create a `.env` file for environment variables with your MongoDB and OpenAI API keys.
4. Run the application with Docker Compose:

   ```bash
   docker-compose up
