def generate_plan(destination, start_date, end_date, budget, interests, travelers):
    if destination.strip() == "":
        return "Please enter a destination."

    plan = f"""
🌍 Travel Plan

Destination: {destination}
Travelers: {travelers}
Budget: {budget}
Dates: {start_date} to {end_date}

Interests: {", ".join(interests)}

Suggested Itinerary

Day 1:
Arrival and hotel check-in. Explore the nearby area.

Day 2:
Visit major tourist attractions and try local food.

Day 3:
Adventure activities or cultural exploration.

Day 4:
Shopping, relaxation, and return journey.
"""

    return plan
