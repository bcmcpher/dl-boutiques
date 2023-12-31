# datalad-boutiques
OHBM 2023 hackathon Project

## Boutiques Integration to Datalad

## Description and the goals for the OHBM BrainHack

The idea is to create a datalad plugin for boutiques functionality.

Datalad has a lot of useful functionality already, specifically: rerunning commands or scripts and "installing" containers to a dataset.

Boutiques is a tool for annotating an analysis script. It documents the inputs, outputs, and container to run a specific script. It's basically a .json sidecar for your analysis.

The goal of the plugin will be to create a `datalad boutiques` command that can streamline:
 - installing a boutiques command / container from zenodo to a datalad dataset
 - call the installed container on data within the dataset
 - provide useful ways of tracking the outputs 
 - stringing multiple pipelines together

## Participants

### Project Proposer (lead?)

- Brent McPherson (bcmcpher)

### Contributors

- Jacob Sanz-Robinson

## Skills

- python (both tools are python based)

some experience (or interest in learning the mechanics of)
- datalad
- boutiques

## Short name for the Discord chat channel (~15 chars)

dl-boutiques

# DataLad Extension Template

[![Build status](https://ci.appveyor.com/api/projects/status/g9von5wtpoidcecy/branch/main?svg=true)](https://ci.appveyor.com/project/mih/datalad-extension-template/branch/main) [![codecov.io](https://codecov.io/github/datalad/datalad-extension-template/coverage.svg?branch=main)](https://codecov.io/github/datalad/datalad-extension-template?branch=main) [![crippled-filesystems](https://github.com/datalad/datalad-extension-template/workflows/crippled-filesystems/badge.svg)](https://github.com/datalad/datalad-extension-template/actions?query=workflow%3Acrippled-filesystems) [![docs](https://github.com/datalad/datalad-extension-template/workflows/docs/badge.svg)](https://github.com/datalad/datalad-extension-template/actions?query=workflow%3Adocs)

This repository contains an extension template that can serve as a starting point
for implementing a [DataLad](http://datalad.org) extension. An extension can
provide any number of additional DataLad commands that are automatically
included in DataLad's command line and Python API.

For a demo, clone this repository and install the demo extension via

    pip install -e .

DataLad will now expose a new command suite with a `hello...` command.

    % datalad --help |grep -B2 -A2 hello
    *Demo DataLad command suite*

      hello-cmd
          Short description of the command

To start implementing your own extension, [use this
template](https://github.com/datalad/datalad-extension-template/generate), and
adjust as necessary. A good approach is to

- ~~Pick a name for the new extension.~~
- ~~Look through the sources and replace `helloworld` with `<newname>` (hint: `git grep helloworld` should find all spots).~~
- Delete the example command implementation in `datalad_helloworld/hello_cmd.py`.
- Implement a new command, and adjust the `command_suite` in
  `datalad_helloworld/__init__.py` to point to it.
- Replace `hello_cmd` with the name of the new command in
  `datalad_helloworld/tests/test_register.py` to automatically test whether the
  new extension installs correctly.
- Adjust the documentation in `docs/source/index.rst`. Refer to [`docs/README.md`](docs/README.md) for more information on documentation building, testing and publishing.
- Replace this README, and/or update the links in the badges at the top.
- Update `setup.cfg` with appropriate metadata on the new extension.
- Generate GitHub labels for use by the "Add changelog.d snippet" and
  "Auto-release on PR merge" workflows by using the code in the
  `datalad/release-action` repository [as described in its
  README](https://github.com/datalad/release-action#command-labels).

You can consider filling in the provided [.zenodo.json](.zenodo.json) file with
contributor information and [meta data](https://developers.zenodo.org/#representation)
to acknowledge contributors and describe the publication record that is created when
[you make your code citeable](https://guides.github.com/activities/citable-code/)
by archiving it using [zenodo.org](https://zenodo.org/). You may also want to
consider acknowledging contributors with the
[allcontributors bot](https://allcontributors.org/docs/en/bot/overview).

# Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) if you are interested in internals or
contributing to the project.
