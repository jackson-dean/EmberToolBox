import sublime, sublime_plugin

class EmberGenerateCommand(sublime_plugin.WindowCommand):

  def run(self, entity):
    self.entity = entity
    caption = "New " + self.entity.replace("-", " ").title() + ":"
    initial_text = ""
    on_done = self.on_done
    on_cancel = self.on_cancel
    on_change = None

    self.window.show_input_panel(caption, initial_text, on_done, on_change, on_cancel);

  def on_done(self, user_input):
    variables = self.window.extract_variables()
    if "folder" in variables:
      folder = variables["folder"]
      shell_cmd = " ".join(["just", "ember", "generate", self.entity, user_input])
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
    return ("Run an ember cli command directory set to the current project root directory")
