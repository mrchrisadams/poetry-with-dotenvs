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


## Another advantage of this approach

One handy side effect of decoupling the two steps here is that switching env vars,or env files once you're in a virtual environment managed by Poetry is pretty straightforward, because python-dotenv, and it's accompanying CLI support is good.


```
# run the same command in a different environment
poetry run dotenv -e prod.env run YOUR_COMMAND

```

If you've used poetry shell to spin up a shell, then changing environment variables is faster too - you don't need to exit the virtual environment each time.

```

dotenv run python ./example.py # returns "my value"

dotenv set MY_ENV_VAR "a new value"

dotenv run python ./example.py # returns "a new value"
```


