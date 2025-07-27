from flask import Flask, render_template, request
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import GridSearchCV, TimeSeriesSplit

app = Flask(__name__)

# Load dataset and train model
df = pd.read_csv(r"Data\Modeling_v1.csv")

features = [
    'driver_avg_finish_pos_season',
    'top3_driver_season_percentage',
    'driver_avg_finish_pos_season_lag',
    'top3_driver_season_percentage_lag',
    'Constructor_Top3_Percent',
    'grid',
    'Top_3_at_circuit'
]
X = df[features]
y = df['top_3'].astype(int)

# Use simplified params to reduce compute
param_grid = {
    'criterion': ['gini'],
    'n_estimators': [45],
    'max_depth': [10],
    'min_samples_split': [25],
    'min_impurity_decrease': [0.0001]
}

tss = TimeSeriesSplit(n_splits=5)
grid_search = GridSearchCV(
    RandomForestClassifier(random_state=42),
    param_grid=param_grid,
    n_jobs=-1,
    scoring='f1',
    cv=tss.split(X, y),
    verbose=0
)
grid_search.fit(X, y)
model = grid_search.best_estimator_

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        # Collect input values from form
        input_data = {
            'driver_avg_finish_pos_season': float(request.form['driver_avg_finish_pos_season']),
            'top3_driver_season_percentage': float(request.form['top3_driver_season_percentage']),
            'driver_avg_finish_pos_season_lag': float(request.form['driver_avg_finish_pos_season_lag']),
            'top3_driver_season_percentage_lag': float(request.form['top3_driver_season_percentage_lag']),
            'Constructor_Top3_Percent': float(request.form['Constructor_Top3_Percent']),
            'grid': int(request.form['grid']),
            'Top_3_at_circuit': float(request.form['Top_3_at_circuit'])
        }

        input_df = pd.DataFrame([input_data])
        prediction = model.predict(input_df)[0]
        result = "✅ Top 3 Finish" if prediction == 1 else "❌ Not in Top 3"
        return render_template("index.html", result=result)

    return render_template("index.html", result=None)

if __name__ == "__main__":
    app.run(debug=True)
