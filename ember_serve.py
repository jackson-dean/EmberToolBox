import sublime, sublime_plugin

class EmberServeCommand(sublime_plugin.WindowCommand):

  def run(self):
    variables = self.window.extract_variables()
    if "folder" in variables:
      folder = variables["folder"]
      shell_cmd = " ".join(["just", "ember", "serve"])
      self.window.run_command("exec", {
        "shell_cmd": shell_cmd,
        "working_dir": folder,
        "path": "/usr/local/linkedin/bin"
      })
    else:
      sublime.status_message("Error: missing project name")

  def description(self):
    return ("Serve an ember application")
