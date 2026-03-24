# devops-task-scheduler-web-ui

A minimal Python HTTP server that stores named shell commands in a JSON file and exposes a tiny HTML UI to add and list them.

## Key features

- Single-file web app
- Persists tasks to tasks.json
- Simple HTML form for adding tasks
- Displays task name, command, and last_run field if present

## Project structure

- `app.py` — HTTP server and task storage logic
- `tasks.json` — Created automatically when tasks are added

## Requirements

- Python 3.9+

## Setup

```bash
git clone https://github.com/biprajit007/devops-task-scheduler-web-ui.git
cd devops-task-scheduler-web-ui
```

## Usage

### Start the server

```bash
python3 app.py
```

### Open the UI

```bash
http://localhost:8080/
```

## Notes

- The current code stores commands but does not execute them or schedule future runs.
- last_run is displayed only if another process populates it in tasks.json.

## Safety notes

- Do not treat this as a secure scheduler. There is no authentication or command sanitization.

## Limitations / next improvements

- No actual scheduling engine
- No authentication, deletion, or editing
- Not appropriate for Internet exposure
