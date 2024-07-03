from jinja2 import Template
import config
from openai_client import generate_text
from unsplash_client import get_unsplash_images

def create_landing_page(terms):
    # Generate text for the landing page
    title = generate_text(f"Generate a catchy title for a landing page about {terms[0]}")
    intro = generate_text(f"Generate an introduction paragraph for a landing page about {terms[0]}")
    services = generate_text(f"Describe the services offered in relation to {', '.join(terms)}")
    footer = generate_text("Generate a footer message for a landing page")

    # Get images from Unsplash
    images = []
    for term in terms:
        images.extend(get_unsplash_images(term))

    # Load and render the HTML template
    with open("templates/landing_page_template.html") as template_file:
        template = Template(template_file.read())
    
    html_content = template.render(title=title, intro=intro, services=services, footer=footer, images=images)

    # Save the generated HTML to a file
    with open("landing_page.html", "w") as file:
        file.write(html_content)

    print("Landing page generated successfully!")

if __name__ == "__main__":
    create_landing_page(config.TERMS)
