# Pres
## Outline
This is a *workshop*. It *must not* be 1h30m of slides. However, "everyone fork
my project and follow along" feels quite pointless-- yes, it's nice to do things
yourself, but it's not cleanly possible here. We're limited by the fact that
every project, every framework, every language is used in different ways. So
instead, we should aim to show concepts applied to a handful of different
projects.

I'm thinking we have two modes: slide presentation, and slide | GitHub.

## GitHub Actions tips and tricks
### Testing a workflow? Add a manual trigger to run on demand
One of the clunkier parts of GitHub Actions is debugging a new workflow. The
main way to confirm that your workflow does what you want is to run it, and you
can't readily run a workflow locally.

Much of the time, your workflow runs on commits to a branch, and debugging will
involve updating the workflow file, so the workflow triggers every time you
want. But this isn't always the case. Instead, you may state a *manual trigger*
in your workflow file, and run it from the Actions tab. The simple syntax for
this as follows:

```yaml
name: my_workflow_in_progress

on:
  # run on pushes to main...
  push:
    branches:
    - main

  # ...but also every time I ask
  workflow_dispatch: {}

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
    - # ...
```

The `workflow_dispatch` event must be in your workflow file on your default
branch (`main` or `master`). Go to the Actions tab, select the branch to run the
workflow on, and it will run on the latest commit for that branch.

If you have a workflow with complex triggers, or perhaps are testing some
Marketplace action, this can be useful.

You can also go further, and add inputs which you configure when you trigger the
workflow:

```yaml
on:
  workflow_dispatch:
    inputs:
      run_type:
        type: choice
        description: Run type
        options:
        - full
        - partial
        required: true
      reason:
        type: string
        description: Reason for triggering manually
        required: true
```

This begins to shift away from the automated "continuous integration" idea, but
it can still be useful. For example, you may encode the steps to release a
library or package into a workflow, and allow making releases semi-automated,
without the need for (potentially arbitrary) triggers.

#### References
  * https://docs.github.com/en/actions/using-workflows/events-that-trigger-workflows#workflow_dispatch
  * https://docs.github.com/en/actions/using-workflows/workflow-syntax-for-github-actions#onworkflow_dispatchinputs
