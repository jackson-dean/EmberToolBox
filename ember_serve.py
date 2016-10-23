import sublime, sublime_plugin

class EmberServeCommand(sublime_plugin.WindowCommand):

  def run(self):
    variables = self.window.extract_variables()
    if "folder" in variables:
      folder = variables["folder"]
      shell_cmd = " ".join(["ember", "serve"])
      settings = sublime.load_settings('ember-tool-box.sublime-settings')
      linkedin = settings.get("linkedin", False);

      if linkedin:
        self.window.run_command("exec", {
          "shell_cmd": "just " + shell_cmd,
          "working_dir": folder,
          "path": "/usr/local/linkedin/bin/"
        })
      else:
        self.window.run_command("exec", {
          "shell_cmd": shell_cmd,
          "working_dir": folder,
          "path": settings.get("ember_path", "/usr/local/bin/ember")
        })
    else:
      sublime.status_message("Error: missing project name")

  def description(self):
    return ("Serve an ember application")
