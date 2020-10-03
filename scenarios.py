scenario1 = {
    "id": 1,
    "title": "Work Scenario",
    "description": "A talkative new colleague is an avid tabloid and social media fan. She believes most of the things she reads a little too much, and talks constantly about refugees and asylum seekers being responsible for all kinds of issues that exist in our society. It has gotten to the point where you can't even talk about find a new property to rent without her loudly blaming immigrants for 'leeching off of the government' and 'getting handouts'.  Her husband has had a difficult time finding a job after being laid off, and she fully thinks immigrants are responsible and have 'taken all the jobs'. How do you respond to these statements?",
    "suggestions": ["Have you considered ____","I don’t see it the way you do. I see it as __________.", "Tell me more about ___", "We don't agree on ___ but we can agree on _____"],
    "insights": ["How am I processing the experience?", "What body sensations do I have?", "What is my emotional reaction?"]
}

MAIN_LIST = [scenario1]

def create_scenario(title, desc, sugg, insights):
    """Creates a new scenario object and adds it to master List"""
    new_scenario = {
        "id": len(MAIN_LIST)+1,
        "title": title,
        "description": desc,
        "suggestions": sugg.split(','),
        "insights": insights.split(',')
    }

    MAIN_LIST.append(new_scenario)

    return MAIN_LIST
