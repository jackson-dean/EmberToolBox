import sublime, sublime_plugin

class EmberGenerateCommand(sublime_plugin.WindowCommand):

  def run(self, entity, flag=None):
    self.entity = entity
    self.flag = flag
    caption = "New " + self.entity.replace("-", " ").title() + ":"
    self.window.show_input_panel(caption, "", self.generate_entity, None, self.on_cancel);

  def generate_entity(self, user_input):
    if self.flag == "-ir":
      self.entity_name = user_input
      self.window.show_input_panel("Addon Name:", "", self.generate_in_repo_entity, None, self.on_cancel)
    else:
      shell_cmd = " ".join(["just", "ember", "g", self.entity, user_input])
      self.run_ember_command(shell_cmd)

  def generate_in_repo_entity(self, user_input):
    shell_cmd = " ".join(["just", "ember", "g", self.entity, self.entity_name, "-ir", user_input])
    self.run_ember_command(shell_cmd)

  def run_ember_command(self, shell_cmd):
    variables = self.window.extract_variables()
    if "folder" in variables:
      folder = variables["folder"]
      self.window.run_command("exec", {
        "shell_cmd": shell_cmd,
        "working_dir": folder,
        "path": "/usr/local/linkedin/bin"
      })
    else:
      sublime.status_message("Error: missing project name")

  def on_cancel():
    sublime.status_message("EmberCLI operation canceled.")

  def description(self):
    return ("Run an ember cli command with directory set to the current project root directory")
