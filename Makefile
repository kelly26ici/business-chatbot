.PHONY: chat serve test install clean lint settings constants streamlit test-customer test-connections test-extractor test-chat

# ------------------------
# RUN APP
# ------------------------

chat:
	python -m src.services.chat

gemini:
	python -m src.services.gemini_client

groq:
	python -m src.services.groq_client

serve:
	uvicorn src.handlers.webhook_handler:app --host 0.0.0.0 --port 8000 --reload

streamlit:
	python app.py

# ------------------------
# CONFIG / DEBUG
# ------------------------

settings:
	python -m src.config.settings

constants:
	python -m src.config.constants

# ------------------------
# INSTALL
# ------------------------

install:
	uv pip install -r requirements.txt

# ------------------------
# TESTS
# ------------------------

test:
	python -m pytest tests/

test-groq:
	python -m tests.test_groq

test-chat:
	python -m tests.test_chat_full

test-live:
	python -m tests.test_chat_live

test-customer:
	python -m tests.test_customer

test-connections:
	python -m tests.test_connections

test-extractor:
	python -m tests.test_extractor

# ------------------------
# CODE QUALITY
# ------------------------

lint:
	python -m flake8 src/

# ------------------------
# CLEANUP
# ------------------------

clean:
	find . -type d -name "__pycache__" -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete