# Updating the example data

Metadata for TimeXAI's example `InferenceData` objects (which are loadable by {func}`~TimeXAI.load_TimeXAI_data`) is stored in the [`TimeXAI_example_data`](https://github.com/TimeXAI-devs/TimeXAI_example_data) repository.
This repo has been embedded into the `TimeXAI` repo at `/TimeXAI/data/example_data` using [git subtree](https://www.atlassian.com/git/tutorials/git-subtree) with the following command:

```bash
$ git subtree add --prefix TimeXAI/data/example_data https://github.com/TimeXAI-devs/TimeXAI_example_data.git main --squash
```

When `TimeXAI_example_data` is updated, the subtree within the `TimeXAI` repo also needs to be updated with the following command:

```bash
$ git subtree pull --prefix TimeXAI/data/example_data https://github.com/TimeXAI-devs/TimeXAI_example_data.git main --squash
```
