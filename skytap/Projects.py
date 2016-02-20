from skytap.models.Project import Project
from skytap.models.SkytapGroup import SkytapGroup

class Projects(SkytapGroup):
    def __init__(self):
        super(Projects, self).__init__()
        self.load_list_from_api('/v2/projects', Project)
