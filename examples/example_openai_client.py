#!/usr/bin/env python3
"""
Description: Simple CLI utility for sending a prompt to the OpenAI API and printing the response.

Usage: python ai_prompt_cli.py "Explain Terraform in one sentence."

Requirements:
    - pip install openai
    - OPENAI_API_KEY environment variable set
"""
# flake8: noqa: E401

__author__ = "Paul Fry"
__version__ = "1.0"
__date_created__ = ""

import os
import sys
import logging

from openai import OpenAI

logging.basicConfig(format="%(message)s")
logger = logging.getLogger("application_logger")
logger.setLevel(logging.INFO)


def get_openai_client() -> OpenAI:
    """Create an OpenAI client using OPENAI_API_KEY from the environment.

    Raises: EnvironmentError: If OPENAI_API_KEY is not set."""
    api_key = os.getenv("OPENAI_API_KEY")

    if not api_key:
        raise EnvironmentError("OPENAI_API_KEY not set. Set it as an environment variable before running.")

    # Note: OpenAI() will also read OPENAI_API_KEY automatically in many setups, but we pass it explicitly here for clarity.
    return OpenAI(api_key=api_key)


def ask_openai(prompt: str, model: str = "gpt-4o-mini") -> str:
    """Send a prompt to OpenAI and return the text response.

    Args:
        prompt: User prompt text.
        model: Model name to use.

    Returns: The model's response text."""
    client = get_openai_client()

    response = client.responses.create(
        model=model,
        input=prompt,
    )

    # Responses API returns a structured "output" list; this is the typical path for text output.
    return response.output[0].content[0].text


def main():
    """Main entry point of the script."""
    logger.debug("Function called 'main()'")

    # Basic CLI usage: first argument is the prompt
    if len(sys.argv) < 2:
        logger.info('Usage: python ai_prompt_cli.py "<your prompt here>"')
        sys.exit(1)

    prompt = sys.argv[1]
    model = os.getenv("OPENAI_MODEL", "gpt-4o-mini")  # optional override via env var

    try:
        result = ask_openai(prompt=prompt, model=model)
        logger.info("\n--- OpenAI Response ---\n")
        logger.info(result)

    except Exception as exc:
        logger.info(f"Error calling OpenAI API: {exc}")
        sys.exit(2)


if __name__ == "__main__":
    """This is executed when run from the command line"""
    main()
