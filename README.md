# Movie Recommendation System

## Overview
Synapse is an intelligent movie recommendation system built with Python and Streamlit. It uses content-based filtering and cosine similarity to recommend movies based on user selection. The application leverages the TMDb (The Movie Database) API to fetch movie posters and details.

## Features
- **Content-Based Recommendations**: Analyzes movie features (genres, keywords, cast, crew) to find similar movies
- **Interactive UI**: User-friendly web interface built with Streamlit
- **Real-time Poster Display**: Fetches and displays movie posters from TMDb
- **Fast Similarity Matching**: Pre-computed similarity matrix for instant recommendations
- **Top 5 Recommendations**: Returns the 5 most similar movies for any selected film

## Project Structure
```
movie_demo/
├── app.py                          # Main Streamlit application
├── app2.py                         # Alternative app version
├── artificats/                     # Pre-computed data
│   ├── movie_list.pkl             # Serialized movie list
│   └── similarity.pkl             # Pre-calculated similarity matrix
├── dataset/                        # Raw movie datasets
├── src/                           # Source packages
├── Synapse_recommendation_system.ipynb  # Jupyter notebook with ML pipeline
├── movie_data.pkl                 # Pickled movie data
├── requirements.txt               # Python dependencies
├── setup.py                       # Package configuration
└── README.md                      # This file
```

## How It Works

### Algorithm
1. **Data Preprocessing**: Movie data is cleaned and processed
2. **Feature Engineering**: Combines genres, keywords, cast, and crew information
3. **TF-IDF Vectorization**: Converts textual features into numerical vectors
4. **Cosine Similarity**: Calculates similarity scores between all movie pairs
5. **Ranking**: Returns top 5 most similar movies sorted by similarity score

### User Flow
1. User selects a movie from the dropdown menu
2. System retrieves the movie's index and corresponding similarity scores
3. Top 5 similar movies are identified
4. Movie posters are fetched from TMDb API
5. Results are displayed in a 5-column layout with movie names and posters

## Installation

### Prerequisites
- Python 3.7 or higher
- pip package manager

### Setup Steps
1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd movie_demo
   ```

2. **Create a virtual environment** (recommended)
   ```bash
   python -m venv env
   source env/bin/activate  # On Windows: env\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Install the package**
   ```bash
   pip install -e .
   ```

## Usage

### Running the Application
```bash
streamlit run app.py
```

This will launch the web application at `http://localhost:8501`

### Steps to Get Recommendations
1. Select a movie from the dropdown menu
2. Click the "Show Recommendation" button
3. View the 5 recommended movies with their posters

## Dependencies
- **streamlit**: Web application framework for building interactive UIs
- **pandas**: Data manipulation and analysis
- **requests**: HTTP library for API calls
- **pickle**: Data serialization format

See `requirements.txt` for the complete dependency list.

## API Integration
The application uses the TMDb API to fetch movie posters:
- **Endpoint**: `https://api.themoviedb.org/3/movie/{movie_id}`
- **Poster Source**: `https://image.tmdb.org/t/p/w500/{poster_path}`
- **API Key**: Required in the URL (currently embedded in app.py)

> **Note**: For production use, store the API key in environment variables instead of hardcoding.

## Training Data
The recommendation model uses a pre-computed similarity matrix based on a movie dataset containing:
- Movie titles and IDs
- Genres
- Keywords
- Cast and crew information
- Other metadata

The processed data is stored in `artificats/` directory as pickle files for fast loading.

## Performance
- **Recommendation Generation**: < 100ms
- **Poster Fetching**: Depends on TMDb API latency (typically 200-500ms)
- **Similarity Matrix Size**: Pre-computed for fast inference

## Future Enhancements
- User-based collaborative filtering
- Hybrid recommendation models
- User rating system
- Search functionality
- Recommendation explanations
- Dark mode UI
- Multi-language support

## Author
**Clovis Atiki**
- Email: atikiclovis0@gmail.com

## License
[Add your license information here]

## Contributing
Contributions are welcome! Please feel free to submit pull requests or open issues for bugs and feature requests.

## Troubleshooting

### Issue: "ModuleNotFoundError: No module named 'streamlit'"
**Solution**: Install dependencies with `pip install -r requirements.txt`

### Issue: "FileNotFoundError: artificats/movie_list.pkl"
**Solution**: Ensure the project root is set correctly. Run the app from the project directory.

### Issue: API errors when fetching posters
**Solution**: Check your internet connection and verify the TMDb API key is valid.

## Contact
For questions or support, reach out to atikiclovis0@gmail.com
