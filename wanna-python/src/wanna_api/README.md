# Wanna API
This is the base Wanna API where all of our primary endpoints live for the Wanna app. Running
the API is really easy and can be done with the following once everything is setup:

```
uv run wanna_api
```

## Development Setup
In order to get started with development with the `wanna_api` you have to install our package 
manager of choice: `uv`. This can be done with `pip` (hopefully the only time you have to ever 
use pip).

```
pip install uv
```

Once you have `uv` installed, you can navigate to the top level of this project and run the following:

```
uv sync
```

This will create a new local `.venv` that you should then point at for all further development work in 
the project.

## Build & Deploy
This will be docker stuff in the future, have not gotten there yet.