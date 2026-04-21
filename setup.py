
from setuptools import  find_packages,setup






def get_requirements(file_path):
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n", "") for req in requirements]
        
        # Remove '-e .' if it exists in your requirements.txt
        if "-e ." in requirements:
            requirements.remove("-e .")
            
    return requirements


setup(
    name = 'repo2',
    version = '0.0.1',
    author = 'reddolivia@gmail.com',
    install_requires = get_requirements('requirement.txt'),
    packages = find_packages() # Added this so it actually finds your code!
)

