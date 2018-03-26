import random

def separate_projects(projects):
    popular = filter(lambda x: x['nreceiving_from'] > 5,projects)
    others = filter(lambda x: x['nreceiving_from'] <= 5, projects)
    return (popular, others)

def randomize_projects(projects):
    return get_random_projects(projects,len(projects))

def get_random_projects(projects, number):
    result = random.sample(projects, number)
    return result

def get_featured_projects(all_projects):
    (pop_projects, oth_projects) = separate_projects(all_projects)

    numberOfPopProjects = 0
    numberOfOthProjects = 0

    if len(all_projects) >= 10:
        if len(pop_projects) < 7:
            numberOfPopProjects = len(pop_projects)
            numberOfOthProjects = 7 - len(pop_projects)
        else :
            numberOfPopProjects = 7
        if len(oth_projects) < 3:
            numberOfPopProjects = 7 + 3 - len(oth_projects)
            numberOfOthProjects = len(oth_projects)
        else :
            numberOfOthProjects =numberOfOthProjects + 3
    else:
        return randomize_projects(all_projects)

    return randomize_projects(get_random_projects(pop_projects, numberOfPopProjects) + get_random_projects(oth_projects, numberOfOthProjects))
