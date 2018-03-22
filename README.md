# overlay

pyqt5 python application for rendering an overlay for an uploaded .tif orthomosaic with google maps like controls

run with 'python Main.py' from src/overlay/

in dependencies folder are wheels for installing gdal in order to get the gps coordinates of corners of the image.
use them as 'pip install example_wheel.whl'

Contributing

    Create your feature branch: git checkout -b new_branch_name
    Stage your changes for commit git add .
    Commit your changes: git commit -am 'Add some feature'
    Push to the branch: git push origin new_branch_name
    Submit a pull request to the Master Branch when you are done with your feature, do NOT push directly

Development Workflow

    The master branch at any time represents a stable (and tested) build of the code base.
    All development work should be performed in feature branches. In most cases, feature branches will be branched off of the master branch. Naming of the feature branches is up to the developer. Using your initials is helpful so we know who is working where, but not crucial. (Ex: ma-feature_name)
    Pull from master often, and especially before submitting a pull request to make sure your feature branch has the latest codebase.
    When commits are made be sure to describe what is done
    BEFORE submitting a pull request, ensure that your branch is up to date with master
    When a feature branch is ready and up to date with master, submit a pull request detailing the changes made, any dependency updates, and any other information to help with the merge.
    The repo admin will be responsible for merging all pull requests, enforcing coding standards and generally keeping master stable and clean. In most cases the repo admin will be responsible for upgrading dependencies as well.
