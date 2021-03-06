from appframe import Application, Command


class RunCommand(Command):
    """
    Ruan an application

    run
        {project-directory : directory of the project to run}
    """

    def handle(self):
        project_directory = self.argument("project-directory")
        app = Application(project_directory)
        app.run()
