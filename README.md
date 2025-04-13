# FpForceCalculator

[FpForce.net](http://fpforce.net/)

ASCE 7-22 Nonstructural Seismic Force Calculator

## Overview

FpForceCalculator is a web application built with Flask that simplifies the calculation of nonstructural seismic forces according to ASCE 7-22 standards. The application provides an intuitive interface for engineers and professionals to quickly compute seismic forces for nonstructural components.

## Project Structure

The project is organized as follows:

```
.
├── flask-app/                 # Main application directory
│   ├── app/                   # Flask application package
│   │   ├── static/           # Static files (CSS, JS, images)
│   │   ├── templates/        # HTML templates
│   │   ├── functions.py      # Core calculation functions
│   │   ├── views.py          # Route handlers and view logic
│   │   ├── application.py    # Application factory
│   │   └── __init__.py       # Package initialization
│   ├── requirements.txt      # Python dependencies
│   ├── pyproject.toml        # Project metadata and build configuration
│   ├── Dockerfile            # Container configuration
│   └── wsgi.py               # WSGI entry point
├── nginx/                    # Nginx configuration
└── compose.yaml              # Docker Compose configuration
```

## Features

- ASCE 7-22 compliant seismic force calculations
- User-friendly web interface
- Containerized deployment with Docker
- Nginx reverse proxy for production deployment

## Development

To run the application locally:

1. Navigate to the `flask-app` directory
2. Create a virtual environment: `python -m venv .venv`
3. Activate the virtual environment: `source .venv/bin/activate`
4. Install dependencies: `pip install -r requirements.txt`
5. Run the development server: `python wsgi.py`

## Deployment

The application is containerized using Docker and can be deployed using Docker Compose:

```bash
docker-compose up -d
```

## License

This project is licensed under the MIT License - see the LICENSE file for details.

