from flask import Flask, request, jsonify
import sqlite3
import pandas as pd
import sklearn.cluster

app = Flask(__name__)

# Connect to SQLite database
conn = sqlite3.connect('database.db')
c = conn.cursor()


@app.route('/ticket_analysis_service_3', methods=['POST'])
def cluster_tickets_by_category():
    c.execute("""
              SELECT category, COUNT(*) AS count
              FROM tickets
              WHERE closing_date IS NULL
              GROUP BY category
              """)

    results = c.fetchall()
    df = pd.DataFrame(results, columns=["category", "count"])

    # Sample data for clustering (replace with actual ticket categories)
    sample_data = {
        'category': ['facility_management', 'technical_it', 'services_complaints'],
        'count': [120, 85, 95]
    }

    df_sampled = pd.DataFrame(sample_data)

    # Perform k-means clustering
    model = sklearn.cluster.KMeans(n_clusters=3)
    model.fit(df[['category']])

    clustered_df = df.copy()
    clustered_df['cluster'] = model.labels_

    return jsonify({"results": clustered_df.to_dict(orient='records')})


if __name__ == '__main__':
    app.run(debug=True)