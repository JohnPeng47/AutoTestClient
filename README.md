In order to activate the githook in this repo, run the following command while in this directory:

```git config --local core.hooksPath .githooks/```

This will configure the local path for githooks to look for it in .githooks

Then run ```sh test_commit.sh``` to do a test run of the post-commit hook