
# MathAPI: Calculate Average of Numbers

MathAPI is a simple FastAPI application that calculates the average of a list of numbers provided in a POST request.

## Requirements

- Python 3.6 or later
- `uvicorn` (for running the development server)
- `pyenv` and `pyenv-virtualenv` (for managing Python versions and virtual environments)

## Installation

1. **Clone the repository**:
   ```bash
   git clone [https://github.com/winston-brown/mathapi_fastapi](https://github.com/winston-brown/mathapi_fastapi)
   cd MathAPI
   ```

2. **Install `pyenv` and `pyenv-virtualenv`** if you haven't already:
   - Follow the [pyenv installation guide](https://github.com/pyenv/pyenv#installation) for your operating system.
   - Install the `pyenv-virtualenv` plugin by following the instructions [here](https://github.com/pyenv/pyenv-virtualenv#installation).

3. **Install the required Python version** and create a virtual environment:
   ```bash
   pyenv install 3.8.10  # (or your preferred Python version)
   pyenv virtualenv 3.8.10 mathapi-env
   ```

4. **Activate the virtual environment**:
   ```bash
   pyenv activate mathapi-env
   ```

5. **Install the dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

## Running the API Locally

1. **Save the application code** as `main.py` in the project directory.

2. **Run the API using uvicorn**:
   ```bash
   uvicorn main:app --reload
   ```

   The FastAPI development server will start, and you can access the API at [http://127.0.0.1:8000](http://127.0.0.1:8000).

## Testing the API

You can test the `/average` endpoint using a tool like Postman, curl, or any HTTP client. Here’s an example using `curl`:

```bash
curl -X POST http://127.0.0.1:8000/average -H "Content-Type: application/json" -d '{"numbers": [1, 2, 3, 4]}'
```

This will send a POST request to the API with the following JSON payload:

```json
{
  "numbers": [1, 2, 3, 4]
}
```

The response should return the average of the numbers provided (in this case, `2.5`).

## API Documentation

FastAPI provides an automatically generated interactive API documentation interface, available at [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs). This documentation includes details on available endpoints, data models, and example requests.

## Notes

- The `--reload` option in the `uvicorn` command automatically reloads the server if the code changes, making development easier.
- Use code with caution, especially when integrating into production environments.

---

Enjoy using MathAPI
