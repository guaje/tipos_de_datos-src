# Reveal.js template (Independent version)

This repository contains a modified version of [Reveal.js Template](https://github.com/mbrochh/reveal-template), which can be used to kickstart [reveal.js](http://lab.hakim.se/reveal-js/) presentations.

It also uses [Jinja](http://jinja.pocoo.org/) in order to split up the `index.html` into smaller sub-files (e.g. one file per slide) and it uses [Fabric](http://docs.fabfile.org/) to render your Jinja templates.

## Setting up

First, you need the following python packages:

    Fabric
    Jinja2

Additionally, you need to set up your [reveal.js](https://github.com/hakimel/reveal.js#installation) directory in the file settings.cfg.

For further convenience, you should install [observr](https://github.com/kevinburke/observr/).

## Usage

To build your presentation, you should create and manipulate files in the `src` folder. If you want to use Jinja templates to split up your
presentation, it would be cool to render the template into the [reveal.js](https://github.com/hakimel/reveal.js#installation) directory every time you change something. 

In order to run the file system watcher, execute:

    ./src-watcher.sh

If you don't want to use the file system watcher, you can trigger a build via

    fab build

Now make your changes in the source directory. When you are done, review your changes:

    fab build
    open [reveal.js](https://github.com/hakimel/reveal.js#installation) directory/index.html
