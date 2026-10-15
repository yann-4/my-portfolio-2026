from django.shortcuts import render

GITHUB_URL = "https://github.com/yann-4"
EMAIL = "shemaimanzi4@gmail.com"
PHONE = "+250 788 242 993"
PHONE_LINK = "+250788242993"
# Paste your Strava profile link here, e.g. "https://www.strava.com/athletes/12345678"
STRAVA_URL = "https://www.strava.com/athletes/172472779"

# Each project is a "Mark" in the armoury, like Tony's suits.
# Photos live in images/projects/. Leave "image" out to show a styled placeholder.
PROJECTS = [
    {
        "mark": "I",
        "slug": "rain-detector",
        "title": "Rain Detection System",
        "summary": "An Arduino system that senses rain and raises an alert. Built with my friends.",
        "details": (
            "We wired a rain sensor to an Arduino, read its values and set a "
            "threshold so the board can tell drizzle from a downpour. When it "
            "detects rain it triggers an alert, so you know to bring the "
            "washing in or close the windows. The demo video shows our model "
            "house prototype in action."
        ),
        "tags": ["Arduino", "C++", "Sensors", "Teamwork"],
        "image": "projects/rain-detector.jpg",
        "video": "projects/rain-detector.webm",
        "video_mp4": "projects/rain-detector.mp4",
        "link": GITHUB_URL,
        "status": "Operational",
    },
    {
        "mark": "II",
        "slug": "music-server",
        "title": "Self-hosted Music Server",
        "summary": "My own Navidrome music streaming server, running in Docker, so I can play my music library from any device.",
        "details": (
            "I run Navidrome, an open-source music streaming server, in a Docker "
            "container on my home network. I can browse my albums and stream "
            "them from any device in a web browser. It taught me about "
            "containers, volumes, ports and keeping a home server running."
        ),
        "tags": ["Docker", "Navidrome", "Linux", "Networking"],
        "image": "projects/music-server.jpg",
        "position": "left top",
        "link": GITHUB_URL,
        "status": "Online",
    },
    {
        "mark": "III",
        "slug": "portfolio",
        "title": "This Portfolio",
        "summary": "The site you are on: Django templates, custom CSS and Python-powered mini-games, hosted on PythonAnywhere.",
        "details": (
            "Built with Django using template inheritance and partials, with "
            "hand-written CSS, and mini-games that run in Python on the "
            "server. Deployed on PythonAnywhere."
        ),
        "tags": ["Django", "Python", "HTML/CSS"],
        "image": "projects/portfolio.jpg",
        "link": GITHUB_URL + "/my-portfolio-2026",
        "status": "Live",
    },
    {
        "mark": "IV",
        "slug": "python-projects",
        "title": "Python Projects",
        "summary": "A set of smaller Python programs where I practise problem solving and the fundamentals.",
        "details": (
            "Short programs and experiments I use to get better at Python: "
            "working with data, loops and functions, and writing cleaner code "
            "each time."
        ),
        "tags": ["Python", "Problem solving"],
        "image": "projects/python.jpg",
        "position": "center 30%",
        "link": GITHUB_URL,
        "status": "In development",
    },
]

# Featured run from Strava. Swap in a newer run whenever you like.
STRAVA_RUN = {
    "title": "Lunch Run",
    "date": "2 August 2026",
    "place": "Gasabo District, Kigali",
    "url": "https://www.strava.com/activities/19567456432",
}
STRAVA_STATS = [
    {"label": "Distance", "value": "5.03", "unit": "km"},
    {"label": "Moving time", "value": "31:09", "unit": ""},
    {"label": "Pace", "value": "6:11", "unit": "/km"},
    {"label": "Elevation", "value": "23", "unit": "m"},
]

SPORT_PHOTOS = [
    {"src": "sport/football-1.jpg", "caption": "Training with the team"},
    {"src": "sport/running-1.jpg", "caption": "Out on a run"},
]
MUN_PHOTO = {"src": "me/speaking.jpg", "caption": "Speaking at Path to Success Int. School"}

# Everything on the Gallery page. Add a photo: put it in images/ and add a line here.
GALLERY = [
    {"src": "me/networking-lab.jpg", "caption": "Setting up routers in the networking lab", "tag": "Tech"},
    {"src": "me/at-work.jpg", "caption": "Focused on the build", "tag": "Tech"},
    {"src": "me/speaking.jpg", "caption": "Public speaking at school", "tag": "MUN & speaking"},
    {"src": "projects/music-server.jpg", "caption": "My Navidrome music server, running in Docker", "tag": "Projects", "position": "left top"},
    {"src": "projects/python.jpg", "caption": "Battle station: OOP in Python", "tag": "Workshop", "position": "center 30%"},
    {"src": "projects/workbench.jpg", "caption": "Arduino, sensors and a 7-segment display", "tag": "Workshop", "position": "center 72%"},
    {"src": "sport/football-1.jpg", "caption": "Training with the team", "tag": "Football"},
    {"src": "sport/running-1.jpg", "caption": "Out on a run", "tag": "Running"},
    {"src": "life/movie-night-1.jpg", "caption": "Movie night: Into the Spider-Verse", "tag": "Downtime"},
    {"src": "life/movie-night-2.jpg", "caption": "Still one of the best hero films", "tag": "Downtime"},
]
GALLERY_VIDEO = {
    "webm": "projects/rain-detector.webm",
    "mp4": "projects/rain-detector.mp4",
    "poster": "projects/rain-detector.jpg",
    "caption": "Rain detection system demo (built with my friends)",
}


# ---------------------------------------------------------------------------
# Games. These run in Python: the form sends your answer, the view checks it.
# ---------------------------------------------------------------------------

MY_AGE = 17  # <- put your real age here

CHOICE_GAMES = [
    {
        "key": "career",
        "question": "What do I want to be when I grow up?",
        "options": ["Doctor", "Computer engineer", "Lawyer", "Pro footballer"],
        "answer": "Computer engineer",
        "win": "Correct! Computer engineering is the mission.",
        "lose": "Not quite. I'm going to be a computer engineer.",
    },
    {
        "key": "hero",
        "question": "Which superhero got me into tech?",
        "options": ["Batman", "Spider-Man", "Iron Man", "Black Panther"],
        "answer": "Iron Man",
        "win": "Correct! Tony Stark started it all.",
        "lose": "Nope. It was Iron Man, Tony Stark and his workshop.",
    },
]


def play_age_game(post):
    """Higher/lower guessing game. The number of tries is carried in a hidden field."""
    try:
        guess = int(post.get("guess", ""))
        tries = int(post.get("tries", "0")) + 1
    except ValueError:
        return {"message": "Type a number to guess.", "tries": post.get("tries", "0")}

    if guess == MY_AGE:
        return {"message": f"Yes! I'm {MY_AGE}. You got it in {tries} {'try' if tries == 1 else 'tries'}.",
                "won": True, "tries": 0}
    hint = "older" if guess < MY_AGE else "younger"
    return {"message": f"{guess}? I'm {hint} than that. Try again.", "tries": tries, "last_guess": guess}


def play_choice_game(post):
    game = next((g for g in CHOICE_GAMES if g["key"] == post.get("game")), None)
    if game is None or post.get("choice") not in game["options"]:
        return None, None
    correct = post.get("choice") == game["answer"]
    return game["key"], {"message": game["win"] if correct else game["lose"], "won": correct,
                         "choice": post.get("choice")}


def base_context(**extra):
    context = {
        "github_url": GITHUB_URL,
        "email": EMAIL,
        "strava_url": STRAVA_URL,
        "phone": PHONE,
        "phone_link": PHONE_LINK,
    }
    context.update(extra)
    return context


def home(request):
    return render(request, "index.html", base_context(projects=PROJECTS[:3], project_count=len(PROJECTS)))


def projects(request):
    return render(request, "projects.html", base_context(projects=PROJECTS))


def about(request):
    age_result = None
    choice_results = {}

    if request.method == "POST":
        if request.POST.get("game") == "age":
            age_result = play_age_game(request.POST)
        else:
            key, result = play_choice_game(request.POST)
            if key:
                choice_results[key] = result

    games = [dict(game, result=choice_results.get(game["key"])) for game in CHOICE_GAMES]

    return render(
        request,
        "about.html",
        base_context(
            strava_run=STRAVA_RUN,
            strava_stats=STRAVA_STATS,
            has_strava_stats=any(stat["value"] is not None for stat in STRAVA_STATS),
            sport_photos=SPORT_PHOTOS,
            mun_photo=MUN_PHOTO,
            age_result=age_result,
            choice_games=games,
        ),
    )


def gallery(request):
    return render(request, "gallery.html", base_context(photos=GALLERY, video=GALLERY_VIDEO))


def contact(request):
    return render(request, "contact.html", base_context())
