import sublime, sublime_plugin

class EmberCommandCommand(sublime_plugin.WindowCommand):

  def run(self, ember_cli):
    self.ember_cli = ember_cli
    self.window.show_input_panel("New Component:", "", self.on_done, None, self.on_cancel);

  def on_cancel():
      sublime.status_message("EmberCLI operation canceled.")

  def on_done(self, user_input):
    variables = self.window.extract_variables()
    if "folder" in variables:
      folder = variables["folder"]
      self.window.run_command("exec", {
        "shell_cmd": "just ember " + self.ember_cli + " " + user_input,
        "working_dir": folder,
        "path": "/usr/local/linkedin/bin/just"
      })
    else:
      sublime.status_message("Error: missing project name")

  def description(self):
    return ("Run an ember cli command directory set to the current project root directory")
