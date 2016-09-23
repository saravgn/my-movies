import webbrowser
import os
import re


# Styles and scripting for the page
main_page_head = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <title>Trailerland</title>
    <!-- Bootstrap 3 -->
    <link rel="stylesheet" href="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/css/bootstrap.min.css">
    <link rel="stylesheet" href="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/css/bootstrap-theme.min.css">
    <script src="http://code.jquery.com/jquery-1.10.1.min.js"></script>
    <script src="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/js/bootstrap.min.js"></script>
    <style type="text/css" media="screen">
        body {
            padding-top: 80px;
            background-color: orange;
        }
        #trailer .modal-dialog {
            margin-top: 200px;
            width: 640px;
            height: 480px;
        }
        .hanging-close {
            position: absolute;
            top: -12px;
            right: -12px;
            z-index: 9001;
        }
        #trailer-video {
            width: 100%;
            height: 100%;
        }
        .movie-tile {
            margin-bottom: 20px;
            padding-top: 20px;
            font-family: "Comic Sans MS"
        }
        .movie-tile:hover {
            background-color: orange;
            cursor: pointer;
        }
        .scale-media {
            padding-bottom: 56.25%;
            position: relative;
        }
        .scale-media iframe {
            border: none;
            height: 100%;
            position: absolute;
            width: 100%;
            left: 0;
            top: 0;
            background-color: white;
        }

        .navbar-header {
            float: left;
            padding: 20px;
            text-align: right;
            width: 100%;
        }

        .navbar-brand {
            float:none;
        }

        .hovereffect {
          width: 100%;
          height: 100%;
          float: left;
          overflow: hidden;
          position: relative;
          text-align: center;
          cursor: default;
        }

        .hovereffect .overlay {
          width: 100%;
          height: 100%;
          position: absolute;
          overflow: hidden;
          top: 0;
          left: 0;
          background-color: rgba(0,0,0,0.6);
          opacity: 0;
          filter: alpha(opacity=0);
          -webkit-transform: translate(460px, -100px) rotate(180deg);
          -ms-transform: translate(460px, -100px) rotate(180deg);
          transform: translate(460px, -100px) rotate(180deg);
          -webkit-transition: all 0.2s 0.4s ease-in-out;
          transition: all 0.2s 0.4s ease-in-out;
        }

        .hovereffect img {
          display: block;
          position: relative;
          -webkit-transition: all 0.2s ease-in;
          transition: all 0.2s ease-in;
        }

        .hovereffect h2 {
          text-transform: uppercase;
          color: #fff;
          text-align: center;
          position: relative;
          font-size: 17px;
          padding: 10px;
          background: rgba(0, 0, 0, 0.6);
        }

        .hovereffect a.info {
          display: inline-block;
          text-decoration: none;
          padding: 7px 14px;
          text-transform: uppercase;
          color: #fff;
          border: 1px solid #000000;
          margin: 50px 0 0 0;
          background-color: transparent;
          -webkit-transform: translateY(-200px);
          -ms-transform: translateY(-200px);
          transform: translateY(-200px);
          -webkit-transition: all 0.2s ease-in-out;
          transition: all 0.2s ease-in-out;
        }

        .hovereffect a.info:hover {
          box-shadow: 0 0 5px #fff;
        }

        .hovereffect:hover .overlay {
          opacity: 1;
          filter: alpha(opacity=100);
          -webkit-transition-delay: 0s;
          transition-delay: 0s;
          -webkit-transform: translate(0px, 0px);
          -ms-transform: translate(0px, 0px);
          transform: translate(0px, 0px);
        }

        .hovereffect:hover h2 {
          -webkit-transform: translateY(0px);
          -ms-transform: translateY(0px);
          transform: translateY(0px);
          -webkit-transition-delay: 0.5s;
          transition-delay: 0.5s;
        }

        .hovereffect:hover a.info {
          -webkit-transform: translateY(0px);
          -ms-transform: translateY(0px);
          transform: translateY(0px);
          -webkit-transition-delay: 0.3s;
          transition-delay: 0.3s;
        }
        
    </style>
    <script type="text/javascript" charset="utf-8">
        // Pause the video when the modal is closed
        $(document).on('click', '.hanging-close, .modal-backdrop, .modal', function (event) {
            // Remove the src so the player itself gets removed, as this is the only
            // reliable way to ensure the video stops playing in IE
            $("#trailer-video-container").empty();
        });
        // Start playing the video whenever the trailer modal is opened
        $(document).on('click', '.movie-tile', function (event) {
            var trailerYouTubeId = $(this).attr('data-trailer-youtube-id')
            var sourceUrl = 'http://www.youtube.com/embed/' + trailerYouTubeId + '?autoplay=1&html5=1';
            $("#trailer-video-container").empty().append($("<iframe></iframe>", {
              'id': 'trailer-video',
              'type': 'text-html',
              'src': sourceUrl,
              'frameborder': 0
            }));
        });
        // Animate in the movies when the page loads
        $(document).ready(function () {
          $('.movie-tile').hide().first().show("fast", function showNext() {
            $(this).next("div").show("fast", showNext);
          });
        });
    </script>
</head>
'''


# The main page layout and title bar
main_page_content = '''
  <body>
    <!-- Trailer Video Modal -->
    <div class="modal" id="trailer">
      <div class="modal-dialog">
        <div class="modal-content">
          <a href="#" class="hanging-close" data-dismiss="modal" aria-hidden="true">
            <img src="https://lh5.ggpht.com/v4-628SilF0HtHuHdu5EzxD7WRqOrrTIDi_MhEG6_qkNtUK5Wg7KPkofp_VJoF7RS2LhxwEFCO1ICHZlc-o_=s0#w=24&h=24"/>
          </a>
          <div class="scale-media" id="trailer-video-container">
          </div>
        </div>
      </div>
    </div>
    <!-- Main Page Content -->
    <div class="container">
      <div class="navbar navbar-inverse navbar-fixed-top" role="navigation">
        <div class="container">
          <div class="navbar-header">
            <a class="navbar-brand" href="#" style="color: #FF8100">Trailerland</a>
          </div>
        </div>
      </div>
    </div>
    <div class="container">
      {movie_tiles}
    </div>
  </body>
</html>
'''


# A single movie entry html template
movie_tile_content = '''
 <div class="col-md-6 col-lg-4 movie-tile text-center" data-trailer-youtube-id="{trailer_youtube_id}" data-toggle="modal" data-target="#trailer">

    <div class="hovereffect">
        <img class="img-responsive" src="{poster_image_url}" alt="" width="420">
        <div class="overlay">
            <h2>{movie_actors}</h2>
        </div>
      <h2>{movie_title}</h2>

    </div>
</div>
'''

def create_movie_tiles_content(movies):
    # The HTML content for this section of the page
    content = ''
    for movie in movies:
        # Extract the youtube ID from the url
        youtube_id_match = re.search(
            r'(?<=v=)[^&#]+', movie.trailer_youtube_url)
        youtube_id_match = youtube_id_match or re.search(
            r'(?<=be/)[^&#]+', movie.trailer_youtube_url)
        trailer_youtube_id = (youtube_id_match.group(0) if youtube_id_match
                              else None)

        # Append the tile for the movie with its content filled in
        content += movie_tile_content.format(
            movie_title=movie.title,
            poster_image_url=movie.poster_image_url,
            trailer_youtube_id=trailer_youtube_id,
            movie_actors=movie.actors,
            imdb_url_movie=movie.imdb
        )
    return content


def open_movies_page(movies):
    # Create or overwrite the output file
    output_file = open('Trailerland.html', 'w')

    # Replace the movie tiles placeholder generated content
    rendered_content = main_page_content.format(
        movie_tiles=create_movie_tiles_content(movies))

    # Output the file
    output_file.write(main_page_head + rendered_content)
    output_file.close()

    # open the output file in the browser (in a new tab, if possible)
    url = os.path.abspath(output_file.name)
    webbrowser.open('file://' + url, new=2)
