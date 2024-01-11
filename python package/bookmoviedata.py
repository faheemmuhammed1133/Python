

#horror_books=["IT by Stephen King","The Haunting of Hill House by Shirley Jackson"]
#sci_fi_books=["The Martian by Andy Weir","The Time Machine by HG Wells"]
#romantic_books=["Pride and Prejudice by Jane Austen","The Song of Achilles by Madeline Miller"]
#comedy_books=["Catch-22 by Joseph Heller","The Hitchhiker's Guide to the Galaxy by Douglas Adams"]
#historical_books=["A Short History of Nearly Everything by Bill Bryson","Sapiens: A Brief History of Humankind by Yuval Noah Harari"]
#fantasy_books=["Harry Potter series by JK Rowling","The Lord of the Rings by J.R.R. Tolkien"]
#non_fiction_books=["Entangled Life: How Fungi Make Our Worlds, Change Our Minds & Shape Our Futures by Merlin Sheldrake","Braiding Sweetgrass: Indigenous Wisdom, Scientific Knowledge, and the Teachings of Plants by Robin Wall Kimmerer"]
#mystery_books=["The Girl with the Dragon Tattoo by Stieg Larsson","The Silent Patient by Alex Michaelides"]

#horror_movies=["The Shining by Stanley Kubrick","Get Out by Jordan Peele"]
#sci_fi_movies=["Interstellar by Christopher Nolan","TRON:Legacy by Joseph Kosinski"]
#romantic_movies=["Casablanca by Michael Curtiz","Pride and Prejudice by Joe Wright"]
#comedy_movies=["Groundhog Day by Harold Ramis","The Big Lebowski by Joel and Ethan Coen"]
#historical_movies=["Gladiator by Ridley Scott","Dunkirk by Christopher Nolan"]
#fantasy_movies=["Spirited Away by Hayao Miyazaki","Pan's Labyrinth by Guillermo del Toro"]
#non_fiction_movies=["Man on Wire by James Marsh","Free Solo by Jimmy Chin"]
#mystery_movies=["The Departed by Martin Scorsese","Inception by Christopher Nolan"]

class High:
    def romanticbooks(self):
        j=1
        print("\nRecommended books for you:")
        for i in high['romantic_books']:
            print(j,".",i)
            j+=1
        print("\n")
    def romanticmovies(self):
        j=1
        print("\nRecommended movies for you:")
        for i in high['romantic_movies']:
            print(j,".",i)
            j+=1
        print("\n")
    def comedybooks(self):
        j=1
        print("\nRecommended books for you:")
        for i in high['comedy_books']:
            print(j,".",i)
            j+=1
        print("\n")
    def comedymovies(self):
        j=1
        print("\nRecommended movies for you:")
        for i in high['comedy_movies']:
            print(j,".",i)
            j+=1
        print("\n")
    def fantasybooks(self):
        j=1
        print("\nRecommended books for you:")
        for i in high['fantasy_books']:
            print(j,".",i)
            j+=1
        print("\n")
    def fantasymovies(self):
        j=1
        print("\nRecommended movies for you:")
        for i in high['fantasy_movies']:
            print(j,".",i)
            j+=1
        print("\n")
class Moderate:
    def thrillerbooks(self):
        j=1
        print("\nRecommended books for you:")
        for i in moderate['thriller_fiction_books']:
            print(j,".",i)
            j+=1
        print("\n")
    def thrillermovies(self):
        j=1
        print("\nRecommended movies for you:")
        for i in moderate['thriller_movies']:
            print(j,".",i)
            j+=1
        print("\n")
    def historybooks(self):
        j=1
        print("\nRecommended books for you:")
        for i in moderate['historical_books']:
            print(j,".",i)
            j+=1
        print("\n")
    def historymovies(self):
        j=1
        print("\nRecommended movies for you:")
        for i in moderate['historical_movies']:
            print(j,".",i)
            j+=1
        print("\n")
    def scifibooks(self):
        j=1
        print("\nRecommended books for you:")
        for i in moderate['sci_fi_books']:
            print(j,".",i)
            j+=1
        print("\n")
    def scifimovies(self):
        j=1
        print("\nRecommended movies for you:")
        for i in moderate['sci_fi_movies']:
            print(j,".",i)
            j+=1
        print("\n")
class Low:
    def novels(self):
        j=1
        print("\nRecommended books for you:")
        for i in low['classics_books']:
            print(j,".",i)
            j+=1
        print("\n")
    def classicmovies(self):
        j=1
        print("\nRecommended movies for you:")
        for i in low['classic_movies']:
            print(j,".",i)
            j+=1
        print("\n")
    def fictionbooks(self):
        j=1
        print("\nRecommended books for you:")
        for i in low['literary_fiction_books']:
            print(j,".",i)
            j+=1
        print("\n")
    def indiemovies(self):
        j=1
        print("\nRecommended movies for you:")
        for i in low['indie_movies']:
            print(j,".",i)
            j+=1
        print("\n")
    def mysterybooks(self):
        j=1
        print("\nRecommended books for you:")
        for i in low['mystery_books']:
            print(j,".",i)
            j+=1
        print("\n")
    def mysterymovies(self):
        j=1
        print("\nRecommended movies for you:")
        for i in low['mystery_movies']:
            print(j,".",i)
            j+=1
        print("\n")
high={
    'romantic_books':["Pride and Prejudice by Jane Austen","The Song of Achilles by Madeline Miller"],
    'comedy_books':["Catch-22 by Joseph Heller","The Hitchhiker's Guide to the Galaxy by Douglas Adams"],
    'fantasy_books':["Harry Potter series by JK Rowling","The Lord of the Rings by J.R.R. Tolkien"],
    'romantic_movies':["Casablanca by Michael Curtiz","Pride and Prejudice by Joe Wright"],
    'comedy_movies':["Groundhog Day by Harold Ramis","The Big Lebowski by Joel and Ethan Coen"],
    'fantasy_movies':["Spirited Away by Hayao Miyazaki","Pan's Labyrinth by Guillermo del Toro"]}
low={
    'classics_books':["Pride and Prejudice by Jane Austen","Romeo and Juliet by William Shakespeare"],
    'literary_fiction_books':["One Hundred Years of Solitude by Gabriel García Márquez","Blindness by José Saramago"],
    'mystery_books':["Sherlock Holmes by Arthur Conan Doyle","The Silent Patient by Alex Michaelides"],
    'classic_movies':["Casablanca by Michael Curtiz","Pride and Prejudice by Joe Wright"],
    'indie_movies':["Amelie by Jean-Pierre Jeunet","The Spirit of the Beehive by Victor Erice"],
    'mystery_movies':["The Departed by Martin Scorsese","Inception by Christopher Nolan"]}
moderate={
    'thriller_fiction_books':["The Girl on the Train by Paula Hawkins","The Shining by Stephen King"],
    'historical_books':["A Short History of Nearly Everything by Bill Bryson","Sapiens: A Brief History of Humankind by Yuval Noah Harari"],
    'sci_fi_books':["The Martian by Andy Weir","The Time Machine by HG Wells"],
    'thriller_movies':["The Departed by Martin Scorsese","Inception by Christopher Nolan"],
    'sci_fi_movies':["Interstellar by Christopher Nolan","TRON:Legacy by Joseph Kosinski"],
    'historical_movies':["Gladiator by Ridley Scott","Dunkirk by Christopher Nolan"]}

# a=High()
# a.fantasybooks()
# a.comedybooks()
# a.romanticbooks()
# a.comedymovies()
# a.romanticmovies()
# a.fantasymovies()
# b=Moderate()
# b.historybooks()
# b.scifibooks()
# b.thrillerbooks()
# b.thrillermovies()
# b.historymovies()
# b.scifimovies()
# c=Low()
# c.fictionbooks()
# c.mysterybooks()
# c.novels()
# c.classicmovies()
# c.indiemovies()
# c.mysterymovies()
