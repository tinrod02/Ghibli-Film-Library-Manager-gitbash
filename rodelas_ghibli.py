import json

class Production:
    def __init__(self, title, director, release_year, genre, plot_summary, rating=None):
        self.title = title
        self.director = director
        self.release_year = release_year
        self.genre = genre
        self.plot_summary = plot_summary
        self.rating = rating

    def __str__(self):
        return f"Title: {self.title}\nDirector: {self.director}\nRelease Year: {self.release_year}\nGenre: {self.genre}\nPlot Summary: {self.plot_summary}\nRating: {self.rating}"

class Film(Production):
    def __init__(self, title, director, release_year, genre, plot_summary, characters=None, settings=None, rating=None):
        super().__init__(title, director, release_year, genre, plot_summary, rating)
        self.characters = characters if characters else []
        self.settings = settings if settings else []

    def __str__(self):
        return super().__str__() + f"\nCharacters: {', '.join(character.name for character in self.characters)}\nSettings: {', '.join(setting.name for setting in self.settings)}"

class Character:
    def __init__(self, name, roles, description):
        self.name = name
        self.roles = roles
        self.description = description

    def __str__(self):
        return f"Name: {self.name}\nRole: {self.roles}\nDescription: {self.description}"

    def __repr__(self):
        return f"Character('{self.name}', '{self.roles}', '{self.description}')"

class Setting:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def __str__(self):
        return f"Name: {self.name}\nDescription: {self.description}"

    def __repr__(self):
        return f"Setting('{self.name}', '{self.description}')"

class GhibLibrary:
    def __init__(self):
        self.films = []

    def add_film(self, film):
        self.films.append(film)

    def remove_film(self, title):
        for film in self.films:
            if film.title == title:
                self.films.remove(film)
                return True
        return False

    def update_film(self, title, attribute, new_update):
        for film in self.films:
            if film.title == title:
                setattr(film, attribute, new_update)
                return True
        return False

    def display_library_info(self):
        print("\n---------------------------------------")
        print("          GHIBLI FILM LIBRARY           ")
        print("---------------------------------------")
        print("\n                ⠄⠀⠀⠀⠀⡀⠀⡀⠀⠀⠀⠀⠀     ")
        print("             ⢀⡔⠘⠀⠉⠉⢀⢤⠀              ")
        print("            ⢠⣿⣶⡒⠳⠧⠟⣙⢣⠀⠀            ")
        print("          ⢀⠤⡽⡟⠣⠅⠀⠀⠀⠑⠚⡖⡲           ")
        print("          ⠉⠙⣷⣷⣀⠀⠀⠀⡀⣠⡞⠋⠀           ")
        print("            ⢸⡻⣏⠉⠉⠈⢉⡩⡇⠀⠀           ")
        print("         ⡀⠀⠀⠈⠉⠙⠯⠽⠉⠉⠀⠀⠀            ")   
        print("\n")
        for film in self.films:
            print("\n---------------------------------------")
            print("              FILM DETAILS              ")
            print("---------------------------------------")
            print(film)
            print("\n---------------------------------------")
            print("            CHARACTERS                  ")
            print("---------------------------------------")
            for character in film.characters:
                print(character)
            print("\n---------------------------------------")
            print("             SETTINGS                   ")
            print("---------------------------------------")
            for setting in film.settings:
                print(setting)

    def genre_film(self, genre):
        categorized_films = [film for film in self.films if film.genre == genre]
        return categorized_films

    def director_film(self, director):
        categorized_films = [film for film in self.films if film.director == director]
        return categorized_films

    def year_film(self, year):
        categorized_films = [film for film in self.films if film.release_year == year]
        return categorized_films

    def save_to_json(self):
        filename = input("Enter filename to save JSON data: ")
        try:
            with open(filename, 'w') as file:
                data = []
                for film in self.films:
                    film_data = {
                        "title": film.title,
                        "director": film.director,
                        "release_year": film.release_year,
                        "genre": film.genre,
                        "plot_summary": film.plot_summary,
                        "rating": film.rating,
                        "characters": [{"name": character.name, "roles": character.roles, "description": character.description} for character in film.characters],
                        "settings": [{"name": setting.name, "description": setting.description} for setting in film.settings]
                    }
                    data.append(film_data)
                json.dump(data, file, indent=4)
            print("\nData saved to JSON successfully!")
        except Exception as e:
            print("\nError saving data to JSON:", e)

    def load_from_json(self):
        filename = input("Enter filename to load JSON data: ")
        try:
            with open(filename, 'r') as file:
                data = json.load(file)
                self.films = []
                for film_data in data:
                    characters = [Character(character['name'], character['roles'], character['description']) for character in film_data.get('characters', [])]
                    settings = [Setting(setting['name'], setting['description']) for setting in film_data.get('settings', [])]
                    film = Film(
                        film_data['title'],
                        film_data['director'],
                        film_data['release_year'],
                        film_data['genre'],
                        film_data['plot_summary'],
                        characters,
                        settings,
                        film_data.get('rating')
                     )
                    self.add_film(film)
            print("\nData loaded from JSON successfully!")
        except FileNotFoundError:
            print("\nError: File not found.")
        except json.JSONDecodeError as e:
            print("\nError decoding JSON:", e)


    def menu(self):
        while True:
            print("\n---------------------------------------")
            print("\n  STUDIO GHIBLI FILM LIBRARY MANAGER  ")
            print("\n---------------------------------------")
            print("                   ⢠⣾⡆⠀⠀⢀⣶         ")
            print("                   ⢸⣿⣇⣀⣀⣼⣿⠆       ")
            print("                  ⣠⡟⡝⣿⣿⣿⠿⢯        ")
            print("           ⣀⠀⢀⣆⠀⠀⣰⣿⣷⣶⣿⣿⣿⣭⣼⣇       ")
            print("           ⢹⣷⣼⡿⡄⢰⣿⠟⣁⠀⣀⠈⠙⣿⣿⣿⣀     ")
            print("           ⢸⣦⣿⣷⣷⠈⡏⠈⠉⠈⠉⠈⠓⢿⣿⣿⣿⡇    ")
            print("           ⢸⣿⣿⣿⡿⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⣿⠟       ")
            print("            ⠉⠉⠉⠀⠀⠀⠈⠁⠀⠀⠀⠀⠈⠁          ")
            print(" ╔═════════════════════════════════════╗")
            print(" ║                                     ║")
            print(" ║  1. Add Film                        ║")
            print(" ║  2. Remove Film                     ║")
            print(" ║  3. Update Film                     ║")
            print(" ║  4. Classify by Genre               ║")
            print(" ║  5. Classify by Director            ║")
            print(" ║  6. Classify by Year                ║")
            print(" ║  7. Display Information             ║")
            print(" ║  8. Save to JSON                    ║")
            print(" ║  9. Load from JSON                  ║")
            print(" ║  0. Exit                            ║")
            print(" ║                                     ║")
            print(" ╚═════════════════════════════════════╝")

            choice = input("\nEnter your choice: ")

            if choice == "1":
                self.add_film_from_input()
            elif choice == "2":
                self.remove_film_by_title()
            elif choice == "3":
                self.update_film_by_title()
            elif choice == "4":
                self.genre_film_from_input()
            elif choice == "5":
                self.director_film_from_input()
            elif choice == "6":
                self.year_film_from_input()
            elif choice == "7":
                self.display_library_info()
            elif choice == "8":
                self.save_to_json()
            elif choice == "9":
                self.load_from_json()
            elif choice == "0":
                print("\nThank you for using the Ghibli Film Library Manager! I hope it gives you thrilling adventures and learnings!")
                print("                                                                                                               ")
                print("Studio Ghibli films are like dreams you wish you could wake up and live in.- Hayao Miyazaki")
                print("                                                                                                               ")
                break
            else:
                print("Invalid input. Please try again!")

    def add_film_from_input(self):
        title = input("Enter Ghibli film title: ")
        director = input("Enter director: ")
        while True:
            year_released = input("Enter release year: ")
            try:
                year_released = int(year_released)
                break
            except ValueError:
                print("Please enter a valid year.")
        genre = input("Enter film genre: ")
        plots = input("Enter plot summary: ")
        characters = self.get_characters_from_input()
        settings = self.get_settings_from_input()
        rating = input("Enter rating (optional): ")
        if rating:
            rating = float(rating)
        film = Film(title, director, year_released, genre, plots, characters, settings, rating)
        self.add_film(film)
        print("\nGhibli Film added successfully!")

    def remove_film_by_title(self):
        title = input("Enter title of the film to remove: ")
        if self.remove_film(title):
            print("\nGhibli Film removed successfully!")
        else:
            print("\nGhibli Film not found!")

    def update_film_by_title(self):
        title = input("Enter title of the ghibli film to update: ")
        attribute = input("Enter attribute to update (title/director/release_year/genre/plot_summary/rating): ")
        new_update = input(f"Enter new update for {attribute}: ")
        if attribute == "rating" and new_update:
            new_update = float(new_update)
        if self.update_film(title, attribute, new_update):
            print("\nGhibli Film updated successfully!")
        else:
            print("\nGhibli Film not found!")

    def genre_film_from_input(self):
        genre = input("Enter film genre: ")
        categorized_films = self.genre_film(genre)
        if categorized_films:
            for film in categorized_films:
                print(film)
        else:
            print("\nNo films found in this genre.")

    def director_film_from_input(self):
        director = input("Enter director: ")
        categorized_films = self.director_film(director)
        if categorized_films:
            for film in categorized_films:
                print(film)
        else:
            print("\nNo ghibli films found directed by this director.")
    
    def year_film_from_input(self):
        year = input("Enter release year: ")
        try:
            year = int(year)
            categorized_films = self.year_film(year)
            if categorized_films:
                for film in categorized_films:
                    print(film)
            else:
                print("\nNo ghibli films found released in this year.")
        except ValueError:
            print("\nPlease enter a valid year.")

    def get_characters_from_input(self):
        characters = []
        while True:
            name = input("Enter character name (or tap enter to finish): ")
            if not name:
                break
            roles = input("Enter character role: ")
            description = input("Enter character description: ")
            character = Character(name, roles, description)
            characters.append(character)
        return characters

    def get_settings_from_input(self):
        settings = []
        while True:
            name = input("Enter setting name (or tap enter to finish): ")
            if not name:
                break
            description = input("Enter ghibli film setting description: ")
            setting = Setting(name, description)
            settings.append(setting)
        return settings

if __name__ == "__main__":
    library = GhibLibrary()
    library.menu()
