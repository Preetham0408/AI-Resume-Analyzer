SKILL_CATEGORIES = {
    "Programming Languages": {
        "python", "java", "c", "c++", "c#", "javascript", "go"
    },

    "Databases": {
        "sql", "mysql", "postgresql", "mongodb"
    },

    "Web Development": {
        "html", "css", "react", "node", "express"
    },

    "Cloud": {
        "aws", "azure", "gcp"
    },

    "Tools": {
        "git", "docker", "linux"
    }
}

def categorize_skills(skills_list):

    skills_dict = {}
    for category, skills in SKILL_CATEGORIES.items():

        matched = []
        for skill in skills_list:
            if skill in skills:
                matched.append(skill)

        if matched:
            skills_dict[category] = sorted(matched)

    return skills_dict