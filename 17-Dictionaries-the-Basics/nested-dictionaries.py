# słowniki zagnieżdżone - jeden słownik zawiera wiele słowników

tv_shows = {
    "Friends": {
        "Season1": {
            "Episodes": ["Ten, w ktrym wszystko sie zaczyna"],
            "Genre": "Comedy",
            "Year": 1990
        },
        "Season2": {
            "Episodes": ["Ten, w ktorym Monica robi indyka"],
            "Genre": "Comedy",
            "Year": 1992
        }
    },
    "How I Met Your Mother": {
        "Season1": {
            "Episodes": ["Gdy poznałem Barneya", "Ciotka Lilie"],
            "Genre": "Comedy",
            "Year": 1994
        }
    }
}

print(tv_shows["Friends"]["Season1"]["Episodes"])