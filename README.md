# Using poetry and .env files together

Have you come Poetry, the increasginyl Python packaging and dependency management, from Pipenv and found yourself missing the ablity to read from ..env files?

I know I did.

It's not on the developer's roadmap, but it turns out that adding the handling of .env files wasn't so hard.

The downside is that your final invocation ends up with a goofy looking 'run' twice.

So instead of having something minimal like so:

```

poetry run YOUR_COMMAND

```

You end up with something like this instead, to run a command using variables in an envfile at `.env`.

```
poetry run dotenv run YOUR_COMMAND
```


