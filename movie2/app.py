from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Баштапкы кино маалыматтар
movies = [
    {
        "title": "Inception",
        "actors": ["Leonardo DiCaprio", "Joseph Gordon-Levitt", "Elliot Page"],
        "sessions": ["10:00", "14:00", "18:00"]
    },
    {
        "title": "The Matrix",
        "actors": ["Keanu Reeves", "Laurence Fishburne", "Carrie-Anne Moss"],
        "sessions": ["12:00", "16:00", "20:00"]
    },
    {
        "title": "Interstellar",
        "actors": ["Matthew McConaughey", "Anne Hathaway", "Jessica Chastain"],
        "sessions": ["11:00", "15:00", "19:00"]
    }
]

@app.route('/')
def index():
    query = request.args.get('q', '').lower()
    if query:
        filtered = [movie for movie in movies if query in movie['title'].lower()]
    else:
        filtered = movies
    return render_template('index.html', movies=filtered, query=query)

@app.route('/add_actor/<movie_title>', methods=['GET', 'POST'])
def add_actor(movie_title):
    movie = next((m for m in movies if m['title'] == movie_title), None)
    if not movie:
        return "Кино табылган жок.", 404

    if request.method == 'POST':
        new_actor = request.form.get('actor')
        if new_actor and new_actor not in movie['actors']:
            movie['actors'].append(new_actor)
        return redirect(url_for('index'))

    return render_template('add_actor.html', movie=movie)

if __name__ == '__main__':
    app.run(debug=True)
