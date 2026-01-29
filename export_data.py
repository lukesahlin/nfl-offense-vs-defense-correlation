"""
Export NFL data to JSON format for Three.js visualization
"""
import pandas as pd
import numpy as np
import json

# Load the dataset
dataset_url = "https://raw.githubusercontent.com/nflverse/nfldata/master/data/games.csv"
df = pd.read_csv(dataset_url)

# Create a long-format dataset with both home and away perspectives
home_df = df[['season', 'game_type', 'week', 'gameday', 'home_team', 'home_score', 'away_team', 'away_score']].copy()
home_df['team'] = home_df['home_team']
home_df['points_scored'] = home_df['home_score']
home_df['points_allowed'] = home_df['away_score']
home_df['opponent'] = home_df['away_team']
home_df['location'] = 'Home'
home_df['margin'] = home_df['home_score'] - home_df['away_score']

away_df = df[['season', 'game_type', 'week', 'gameday', 'away_team', 'away_score', 'home_team', 'home_score']].copy()
away_df['team'] = away_df['away_team']
away_df['points_scored'] = away_df['away_score']
away_df['points_allowed'] = away_df['home_score']
away_df['opponent'] = away_df['home_team']
away_df['location'] = 'Away'
away_df['margin'] = away_df['away_score'] - away_df['home_score']

# Combine both perspectives
combined_df = pd.concat([
    home_df[['season', 'game_type', 'week', 'gameday', 'team', 'points_scored', 'points_allowed', 'opponent', 'location', 'margin']],
    away_df[['season', 'game_type', 'week', 'gameday', 'team', 'points_scored', 'points_allowed', 'opponent', 'location', 'margin']]
], ignore_index=True)

# Add total points per game
combined_df['total_points'] = combined_df['points_scored'] + combined_df['points_allowed']

# Create a formatted date string
combined_df['game_date'] = pd.to_datetime(combined_df['gameday']).dt.strftime('%Y-%m-%d')

# Remove rows with NaN values
combined_df = combined_df.dropna(subset=['points_scored', 'points_allowed', 'margin', 'season'])

# Normalize data for 3D visualization (scale to reasonable 3D space)
min_season = combined_df['season'].min()
max_season = combined_df['season'].max()
season_range = max_season - min_season if max_season > min_season else 1

# Prepare data for export
games_data = []
for idx, row in combined_df.iterrows():
    games_data.append({
        'team': row['team'],
        'opponent': row['opponent'],
        'points_scored': float(row['points_scored']),
        'points_allowed': float(row['points_allowed']),
        'margin': float(row['margin']),
        'total_points': float(row['total_points']),
        'season': int(row['season']),
        'location': row['location'],
        'game_type': row['game_type'],
        'game_date': row['game_date'],
        # Normalized coordinates for 3D space (0-100 range)
        'x': float(row['points_scored']),  # X: points scored
        'y': float(row['points_allowed']),  # Y: points allowed
        'z': float((row['season'] - min_season) / season_range * 100)  # Z: normalized season
    })

# Calculate team statistics
team_stats = {}
for team in combined_df['team'].unique():
    team_data = combined_df[combined_df['team'] == team]
    team_stats[team] = {
        'avg_points_scored': float(team_data['points_scored'].mean()),
        'avg_points_allowed': float(team_data['points_allowed'].mean()),
        'total_games': int(len(team_data)),
        'seasons': sorted(team_data['season'].unique().tolist())
    }

# Calculate season averages
season_stats = {}
for season in sorted(combined_df['season'].unique()):
    season_data = combined_df[combined_df['season'] == season]
    season_stats[int(season)] = {
        'avg_points_scored': float(season_data['points_scored'].mean()),
        'avg_points_allowed': float(season_data['points_allowed'].mean()),
        'avg_total_points': float(season_data['total_points'].mean()),
        'total_games': int(len(season_data))
    }

# Export to JSON
export_data = {
    'games': games_data,
    'team_stats': team_stats,
    'season_stats': season_stats,
    'metadata': {
        'min_season': int(min_season),
        'max_season': int(max_season),
        'total_games': len(games_data),
        'teams': sorted(combined_df['team'].unique().tolist()),
        'seasons': sorted(combined_df['season'].unique().tolist())
    }
}

# Save to JSON file
with open('nfl_data.json', 'w') as f:
    json.dump(export_data, f, indent=2)

print(f"Data exported successfully!")
print(f"Total games: {len(games_data)}")
print(f"Teams: {len(export_data['metadata']['teams'])}")
print(f"Seasons: {export_data['metadata']['min_season']} - {export_data['metadata']['max_season']}")
print(f"JSON file saved as: nfl_data.json")
