# Library architecture
TimeXAI is organized in modules (the folders in [TimeXAI directory](https://github.com/TimeXAI-devs/TimeXAI/tree/main/TimeXAI)).
The main 3 modules are `data`, `plots` and `stats`.
Then we have 3 more folders. The [tests](https://github.com/TimeXAI-devs/TimeXAI/tree/main/TimeXAI/tests)
folder contains tests for all these 3 modules.

The [static](https://github.com/TimeXAI-devs/TimeXAI/tree/main/TimeXAI/static)
folder is only used to store style and CSS files to get HTML output for `InferenceData`.
Finally we have the [wrappers](https://github.com/TimeXAI-devs/TimeXAI/tree/main/TimeXAI/wrappers)
folder that contains experimental (not tested yet either) features
and interacts closely with both [data](https://github.com/TimeXAI-devs/TimeXAI/tree/main/TimeXAI/data)
and [stats](https://github.com/TimeXAI-devs/TimeXAI/tree/main/TimeXAI/stats) modules.

In addition, there are some files on the higher level directory: `utils.py`, `sel_utils.py`,
`rcparams.py` and `labels.py`.
