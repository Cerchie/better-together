scenario1 = {
    "id": 1,
    "title": "Work Scenario",
    "description": "A talkative new colleague is an avid tabloid and social media fan. She believes most of the things she reads a little too much, and talks constantly about refugees and asylum seekers being responsible for all kinds of issues that exist in our society. It has gotten to the point where you can't even talk about find a new property to rent without her loudly blaming immigrants for 'leeching off of the government' and 'getting handouts'.  Her husband has had a difficult time finding a job after being laid off, and she fully thinks immigrants are responsible and have 'taken all the jobs'. How do you respond to these statements?",
    "suggestions": ["Have you considered ____","I don’t see it the way you do. I see it as __________.", "Tell me more about ___", "We don't agree on ___ but we can agree on _____"],
    "insights": ["How am I processing the experience?", "What body sensations do I have?", "What is my emotional reaction?"]
}

scenario2 = {
    "id": 2,
    "title": "Holiday Family Gathering",
    "description": "You are dreading your annual family Thanksgiving dinner this year. Given the polarizing political climate, you know how difficult it will be to navigate the discussions around your uncle's strong opinions. You make it all the way to pie when it becomes difficult to not engage. Your aunt usually makes a delicious pumpkin pie, but this year has decided to try a new and different recipe as well. You decline the new pie flavor, and opt for the traditional pumpkin. Upon seeing this exchange, your uncle makes a sweeping statement that all conservatives are racists who hate progress and change. How do you respond?",
    "suggestions": ["Have you considered ____","I don’t see it the way you do. I see it as __________.", "Tell me more about ___", "We don't agree on ___ but we can agree on _____"],
    "insights": ["How am I processing the experience?", "What body sensations do I have?", "What is my emotional reaction?"]
}

scenario3 = {
    "id": 3,
    "title": "Social Scenario",
    "description": "It's been ages since you've had lunch with your friends since having your second child. You are excited to leave the baby at home with your mother so you can meet them for brunch and catch up. You arrive at the restaurant, greet each other, then place your order. One of your friends makes a face and questions your decision to order a mimosa. Aren't you nursing? Should you be drinking that? She is horrified when you discuss your excitement to return to work, and comments that since your significant other makes a large salary, it should be your job to stay home and raise your child. How do you respond?",
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
