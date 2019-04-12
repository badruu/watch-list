from flask import render_template,request,redirect,url_for
from . import main
from ..request import get_movies,get_movie,search_movie
from ..models import Review
from .forms import ReviewForm

#views
@main.route('/')
def index():
    '''
    view root page function that returns the index page and its data
    '''
    #Getting popular movie
    popular_movies = get_movies('popular')
    upcoming_movie = get_movies('upcoming')
    now_showing_movie = get_movies('now_playing')
    title = 'Home - Welcome to the best movie review website online'

    search_movie = request.args.get('movie_query')
    if search_movie:
        return redirect(url_for('.index'))
    else:
        return render_template('index.html',title = title,popular = popular_movies,upcoming = upcoming_movie,now_playing = now_showing_movie)


# @app.route('/movie/<int:movie_id>')
# def movie(movie_id):
#     '''
#     View movie page function that returns the movie details page and its data
#     '''
#     title = f'You are viewing {movie_id}'
#     return render_template('movie.html',title = title)

@main.route('/movie/<int:id>')
def movie(id):
    '''
    view movie page function that returns the movie details page and its data
    '''

    movie = get_movie(id)
    title = f'{movie.title}'

    return render_template('movie.html',title = title,movie = movie)

@main.route('/search/<movie_name>')
def search(movie_name):
    '''
    view function to display the search results
    '''

    movie_name_list = movie_name.split(" ")
    movie_name_format = "+".join(movie_name_list)
    searched_movies = search_movie(movie_name_format)
    title = f'search results for {movie_name}'
    return render_template('search.html',movies = searched_movies)


@main.route('/movie/review/new/<int:id>', methods = ['GET','POST'])
def new_review(id):
    form = ReviewForm()
    movie = get_movie(id)

    if form.validate_on_submit():
        title = form.title.data
        review = form.review.data
        new_review = Review(movie.id,title,movie.poster,review)

        new_review.save_review()
        return redirect(url_for('.index'))

    title = f'{movie.title} review'
    return render_template('new_review.html',title = title,review_form=form, movie=movie)