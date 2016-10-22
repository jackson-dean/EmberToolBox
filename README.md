# EmberToolBox

Adds an interface to EmberCLI through the sublime command palette. Also includes some useful snippets for lifecycle hooks and testing helpers.
A work in progress, but handles the basics.

If you happen to be a LinkedIn dev working on an ember app. You'll want to add the following to your user settings for this package:

```
{
  "linkedin": true
}
```

This ensures you are using the LinkedIn specific binaries for running ember cli. 

Otherwise, if you're having trouble getting the cli to work from the command palette, you may want to set the path to your ember-cli installation explicitly in the user settings for this package. Something like the following:

```
{
  "ember_path": "/usr/local/bin/ember"
}
```

Replace `/usr/local/bin/ember` with the path to your machine's specific ember-cli install path.
