from flask import Flask,jsonify, render_template

app = Flask(__name__)

@app.route("/songs")
def list_songs():
    songs=[
        { 
            'id':1,
            'title': 'Let it Be',
            'artist': 'The beatles',
            'album': 'let it Be',
            'release_year':1970
        },
        {
            'id': 2,
            'title': 'Bohemian Rhapsody',
            'artist': 'A Night at the Opera',
            'release_year': 1975
        },
        {
            'id': 3,
            'title': 'Stairway to Heaven',
            'artist': 'Led Zeppelin',
            'album': 'Led Zeppelin IV',
            'release_year': 1971
        }
    ]
    return jsonify(songs)

@app.errorhandler(404)
def invalid_route(e):
    return render_template('404.html')
    

if __name__ == '__main__':
    app.run(debug=True)
