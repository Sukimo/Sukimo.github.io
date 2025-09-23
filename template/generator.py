import json
import os

def format_tags(tags):
    return " ".join(f"<span class='tag'>{tag}</span>" for tag in tags)

def format_media(media_list):
    html = ""
    for item in media_list:
        if item.lower().endswith(('.mp4', '.webm')):
            html += f"<video src='{item}' controls></video>\n"
        elif item.lower().endswith(('.jpg', '.jpeg', '.png', '.gif')):
            html += f"<img src='{item}' alt='Project Media'>\n"
        elif "youtube.com" in item or "youtu.be" in item:
            # optionally handle YouTube links here
            html += f"<iframe src='{item}' allowfullscreen></iframe>\n"
        else:
            html += f"<p>Unsupported media: {item}</p>\n"
    return html

# Load the template
with open("template.html", "r", encoding="utf-8") as f:
    template = f.read()

# Load project data
with open("data.json", "r", encoding="utf-8") as f:
    projects = json.load(f)

# Ensure output directory exists
os.makedirs("output", exist_ok=True)

# Generate a page for each project
for project in projects:
    output_html = template

    # Replace standard text fields
    replacements = {
        "TITLE": project["name"],
        "GITHUB": project["github"],
        "GENRE": project["genre"],
        "DESC_A": project["descA"],
        "DESC_B": project["descB"],
        "TAGS": format_tags(project["tags"]),
        "MEDIA": format_media(project["media"])
    }

    for key, value in replacements.items():
        output_html = output_html.replace(f"{{{{{key}}}}}", value)

    # Output to file based on slug
    filename = f"{project['slug']}.html"
    with open(f"output/{filename}", "w", encoding="utf-8") as f:
        f.write(output_html)

    print(f"✅ Generated: output/{filename}")
