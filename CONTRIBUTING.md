# Contributing to Python Extensive Development Environment Constructor (PyEDEC)

First off, thank you for considering contributing to PyEDEC. It's people like you that make PyEDEC such a great tool.

## Where do I go from here?

If you've noticed a bug or have a feature request, make sure to check our [Issues](https://github.com/your-username/PyEDEC/issues) page to see if someone else in the community has already created a ticket. If not, go ahead and [make one](https://github.com/your-username/PyEDEC/issues/new)!

## Fork & create a branch

If this is something you think you can fix, then [fork PyEDEC](https://help.github.com/articles/fork-a-repo) and create a branch with a descriptive name.

A good branch name would be (where issue #325 is the ticket you're working on):

```bash
git checkout -b 325-add-japanese-localisation
```

## Implement your fix or feature

At this point, you're ready to make your changes! Feel free to ask for help; everyone is a beginner at first.

## Get the code

The first thing you'll need to do is get the PyEDEC code. To do this, you'll need to fork the repository.

## Make a Pull Request

At this point, you should switch back to your master branch and make sure it's up to date with PyEDEC's master branch:

```bash
git remote add upstream https://github.com/your-username/PyEDEC.git
git checkout master
git pull upstream master
```

Then update your feature branch from your local copy of master, and push it!

```bash
git checkout 325-add-japanese-localisation
git rebase master
git push --set-upstream origin 325-add-japanese-localisation
```

Finally, go to GitHub and [make a Pull Request](https://help.github.com/articles/creating-a-pull-request) :D

## Keeping your Pull Request updated

If a maintainer asks you to "rebase" your PR, they're saying that a lot of code has changed, and that you need to update your branch so it's easier to merge.

To learn more about rebasing in Git, there are a lot of [good](https://git-scm.com/book/en/v2/Git-Branching-Rebasing) [resources](https://www.atlassian.com/git/tutorials/merging-vs-rebasing) but here's the suggested workflow:

```bash
git checkout 325-add-japanese-localisation
git pull --rebase upstream master
git push --force-with-lease 325-add-japanese-localisation
```

## Merging a PR (maintainers only)

A PR can only be merged into master by a maintainer if:

1. It is passing CI.
2. It has been approved by at least two maintainers. If it was a maintainer who opened the PR, only one extra approval is needed.
3. It has no requested changes.
4. It is up to date with current master.

Any maintainer is allowed to merge a PR if all of these conditions are met.

## Thank you!

Your contributions to community-driven projects like PyEDEC help to improve the software development ecosystem as a whole. We appreciate your effort and celebrate your contribution, no matter how large or small.
