from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

# Sample data (You can store this in the database)
HOLIDAY_TRIPS = [
    {
        "country": "France",
        "city": "Paris",
        "description": (
            "Visit the Eiffel Tower, one of the most iconic landmarks in the world. "
            "Explore the Louvre Museum, home to the Mona Lisa and other masterpieces. "
            "Walk along the Champs-Élysées, a famous avenue with shops and cafés. "
            "Enjoy a boat cruise on the Seine River and admire Paris’s stunning architecture. "
            "Visit the Notre-Dame Cathedral, a masterpiece of Gothic architecture. "
            "Experience the beauty of Montmartre and the Sacré-Cœur Basilica. "
            "Indulge in authentic French cuisine, including croissants and escargots. "
            "Discover the historic Palace of Versailles and its breathtaking gardens. "
            "Explore the artistic treasures in the Musée d'Orsay. "
            "Experience the magic of Disneyland Paris, a favorite for families."
        )
    },
    {
        "country": "Italy",
        "city": "Rome",
        "description": (
            "Explore the Colosseum, the grand amphitheater of ancient Rome. "
            "Visit Vatican City, home to St. Peter’s Basilica and the Sistine Chapel. "
            "Marvel at Michelangelo’s masterpiece on the ceiling of the Sistine Chapel. "
            "Throw a coin into the Trevi Fountain and make a wish. "
            "Walk through the Roman Forum, once the center of Roman public life. "
            "Discover the Pantheon, a remarkable ancient Roman temple. "
            "Enjoy authentic Italian pizza, pasta, and gelato. "
            "Visit the Spanish Steps and enjoy the lively atmosphere. "
            "Explore the charming Trastevere district with its beautiful streets. "
            "Take a day trip to the ancient ruins of Pompeii or the Amalfi Coast."
        )
    },
    {
        "country": "Japan",
        "city": "Tokyo",
        "description": (
            "Experience the bright lights and energy of Shibuya Crossing. "
            "Explore the historic Asakusa district and visit Senso-ji Temple. "
            "Enjoy shopping and fashion trends in Harajuku’s Takeshita Street. "
            "Discover the traditional side of Tokyo in the Meiji Shrine. "
            "Visit the high-tech district of Akihabara, a paradise for anime lovers. "
            "Experience the nightlife and entertainment of Shinjuku. "
            "Indulge in delicious sushi at Tsukiji Outer Market. "
            "Take a day trip to Mount Fuji and enjoy stunning views. "
            "Relax in an onsen (hot spring) and experience Japanese hospitality. "
            "Enjoy cherry blossom season in Ueno Park during spring."
        )
    },
    {
        "country": "USA",
        "city": "New York",
        "description": (
            "See Times Square and experience the heart of New York’s energy. "
            "Visit the Statue of Liberty, a symbol of freedom and democracy. "
            "Explore Central Park, an urban oasis with beautiful landscapes. "
            "Take in the stunning views from the top of the Empire State Building. "
            "Enjoy a Broadway show in the world-famous theater district. "
            "Discover world-class art at the Metropolitan Museum of Art. "
            "Walk across the Brooklyn Bridge and enjoy the city skyline. "
            "Experience the vibrant culture of Chinatown and Little Italy. "
            "Visit the 9/11 Memorial and Museum to honor history. "
            "Explore the bustling streets and shops of Fifth Avenue."
        )
    },
    {
        "country": "UAE",
        "city": "Dubai",
        "description": (
            "Visit the Burj Khalifa, the tallest building in the world. "
            "Enjoy shopping at the Dubai Mall, featuring luxury brands and an aquarium. "
            "Experience the thrill of a desert safari with dune bashing and camel rides. "
            "Relax at Jumeirah Beach and admire the stunning Burj Al Arab hotel. "
            "Explore the vibrant souks of Old Dubai and experience traditional culture. "
            "Take a boat ride on Dubai Creek and visit the Al Fahidi Historic District. "
            "Enjoy world-class dining with cuisines from around the globe. "
            "Visit Palm Jumeirah, a man-made island shaped like a palm tree. "
            "Explore the indoor ski resort at Ski Dubai inside the Mall of the Emirates. "
            "Experience the nightlife, rooftop bars, and entertainment of Dubai Marina."
        )
    }
]


@login_required
def destinations_view(request):
    return render(request, "destinations/destinations.html", {"tours": HOLIDAY_TRIPS})

@login_required
def destination_details_view(request, country):
    # Find the destination based on the country
    destination = next((tour for tour in HOLIDAY_TRIPS if tour["country"] == country), None)

    if not destination:
        return redirect("destinations")  # Redirect back if country is not found

    return render(request, "destinations/details.html", {"destination": destination})

def logout_view(request):
    logout(request)
    return redirect("home")

#
# def book_tour(request, country):
#     return render(request, 'book_tour.html', {'country': country})

def destinations(request):
    tours = [
        {'country': 'France', 'city': 'Paris'},
        {'country': 'Italy', 'city': 'Rome'},
    ]
    return render(request, 'destinations.html', {'tours': tours})




def book_tour(request, country):
    return render(request, 'destinations/book_tour.html', {'country': country})


def payment_page(request, country):
    return render(request, 'destinations/payment.html', {'country': country})

def payment_success(request, country):
    return render(request, 'destinations/payment_success.html', {'country': country})

