#!/bin/sh
# Start Uvicorn processes
echo "Starting ax_logger producer."

exec python -m uvicorn src.server.app:create_app --reload --factory --port 8000 --host 0.0.0.0