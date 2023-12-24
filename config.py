# config.py

# Import necessary libraries
import os

# Define the base directory for the project
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Define the directory for the templates
TEMPLATES_DIR = os.path.join(BASE_DIR, 'templates')

# Define the default project structure
DEFAULT_PROJECT_STRUCTURE = {
    'src': {
        'main': {
            'python': {},
            'resources': {}
        },
        'test': {
            'python': {},
            'resources': {}
        }
    },
    'docs': {},
    'libs': {},
    'bin': {}
}

# Define the default template
DEFAULT_TEMPLATE = 'default'

# Define the version control system to use
VCS = 'git'

# Define the dependencies file
DEPENDENCIES_FILE = 'requirements.txt'

# Define the AI optimization settings
AI_OPTIMIZATION = {
    'enabled': True,
    'algorithm': 'genetic',
    'population_size': 100,
    'mutation_rate': 0.01,
    'max_generations': 100
}

# Define the dynamic structure adaptation settings
DYNAMIC_STRUCTURE_ADAPTATION = {
    'enabled': True,
    'feedback_file': 'feedback.txt'
}

# Define the automated documentation settings
AUTOMATED_DOCUMENTATION = {
    'enabled': True,
    'output_file': 'README.md'
}
