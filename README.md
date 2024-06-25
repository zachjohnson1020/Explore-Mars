

ExploreMars is a web application built with Django, leveraging the NASA Mars Rover API to display images captured by various Mars rover cameras. Dive into the Red Planet's exploration history with this interactive tool.

## Features

- **Image Display**: View the latest images captured by the Mars rovers Spirit, Opportunity, and Curiosity.
- **Mars Weather from most recent 7 Sols (Martian Days)
## Planned Features
- **Rover Camera Selection**: Choose from different camera to see images taken by each.
- **Date Selection**: Filter images by the date they were taken on Mars.

## Installation

To run ExploreMars locally, follow these steps:

1. Clone the repository:

   ```
   git clone https://github.com/zachjohnson1020/Explore-Mars.git
   ```

2. Navigate into the project directory:

   ```
   cd ExploreMars
   ```

3. Set up a virtual environment (optional but recommended):

   ```
   python -m venv env
   ```

4. Activate the virtual environment:

   - On Windows:

     ```
     .\env\Scripts\activate
     ```

   - On macOS and Linux:

     ```
     source env/bin/activate
     ```

5. Install dependencies:

   ```
   pip install -r requirements.txt
   ```

6. Apply migrations:

   ```
   python manage.py migrate
   ```

7. Start the Django development server:

   ```
   python manage.py runserver
   ```

8. Open your browser and go to:

   ```
   http://localhost:8000
   ```

## Technologies Used

- **Framework**: Django
- **Frontend**: HTML, CSS, JavaScript (integrating Django templates)
- **Backend**: Python
- **API**: NASA Mars Rover API

## API Reference

- [NASA Mars Rover API Documentation](https://api.nasa.gov/)

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request with your improvements.

- Thanks to NASA for providing the Mars Rover API.🚀🔴
