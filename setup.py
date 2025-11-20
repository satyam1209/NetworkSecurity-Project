from setuptools import find_packages,setup
from typing import List

def get_requirements():
    try:
        lst=[]
        with open('requirements.txt') as file_obj:
            lines = file_obj.readlines()
            for line in lines:
                requirements = line.strip()
                if requirements and requirements != '-e .':
                    lst.append(requirements)
        return lst

    except Exception as e:
        print(e)

setup(
    name = 'NetworkSecurity',
    version='0.0.1',
    author='Satyam singh',
    author_email='satyamsingh12092000@gmail.com',
    packages=find_packages(),
    install_requires = get_requirements()
)

if __name__ =='__main__':
    print(get_requirements())