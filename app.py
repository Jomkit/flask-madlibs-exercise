from flask import Flask, request, render_template
from flask_debugtoolbar import DebugToolbarExtension
from stories import stories

app = Flask(__name__)
app.config['SECRET_KEY'] = 'Ma07!bs72'
debug = DebugToolbarExtension(app)

@app.route('/')
def home():
    """Home page, user can pick a story prompt"""

    madlib_stories = stories
    return render_template('home.html', stories=madlib_stories)

@app.route('/questions/<story>')
def questions(story):
    """generate questions based on story object's prompts"""
    the_story = get_story(story)
    prompts = the_story.prompts
    return render_template('questions.html', prompts=prompts,story=story)

def get_story(the_story):
    """Get the chosen story object from the stories set"""
    for story in stories:
        if the_story == story.name:
            return story

@app.route('/story/<story>')
def story_page(story):
    """Generate the respective story from the answers from /questions"""
    the_story = get_story(story)
    ans = request.args
    items = dict(ans.items())
    story_html = the_story.generate(items)
    

    return render_template('story.html', story_html=story_html)