# FLOCX Commit Message Best Practices

Commits to FLOCX projects should follow these best practices:

1. **<a name="separate"></a>A commit messages should have a subject line and
   body separated by a blank line.**

    The first line of your commit message is displayed by itself in various
    circumstances (e.g., `git log --oneline`, variously on GitHub, and so
    forth. The subject should provide a succinct summary of the commit in order
    to make these displays useful.

1. **<a name="subject50"></a>The subject message should be limited to 60
   characters or less.**

    The subject line should be kept short, since it is often displayed on
    screen after a commit id.

1. **<a name="subcaps"></a>The subject line should start with a capital
   letter.**

    Readers generally expect the first word in a sentence to be capitalized.

1. **<a name="subperiod"></a>The subject line should not end with a period.**

    This is a common convention for summary descriptions in many situations.

1. **<a name="mood"></a>The subject line should be written in the imperative
   mood.**

    - Instead of: `This commit adds tests for the api class`

        Use: `Add tests for the api class`

    - Instead of: `New widget feature`

        Use: `Implement new widget feature`

1. **<a name="body72"></a>Lines in the body should be wrapped at 72
   characters.**

    Many terminals default to 80 characters in width. Keeping lines wrapped at
    72 characters leaves room for git to indent messages without overflowing
    the width of the terminal.

1. **<a name="explain"></a>The commit message should explain the purpose of the
   commit.**

    We want the git log to be a useful source of information about the project.
    Your commit message should explain *why* you made the changes and should
    summarize the nature of the changes. For example, this isn't a great commit
    message:

    ```
    New configuration code
    ```

    This is a better one:

    ```
    Add standard configuration handling code (TG-1234)
    
    In order to operate properly, our service requires a number of
    configuration values to be provided by the operator. This commit introduces
    a standard mechanism for handling configuration options (oslo_config) and
    defines a number of configuration options.
    ```

1. **<a name="bugref"></a>The commit message should reference the
   bug/issue/task/user story to which it applies.**

    Referencing the related bug/issue/etc in your commit message provides
    information about *why* the changes were made. In many situations, the
    reference can be used to automatically update the referenced issue with
    information about the commit or even apply status changes.

    For [GitHub][] issues, use the format `#nnn`, where `nnn` is the GitHub
    issue number. For more information, see [Closing issues using keywords][].

    For [Taiga][] tasks/user stories, use the format `TG-nnn`, where `nnn` is
    the task or user story number. For more information, see [Attach commits to
    elements via commit message][] and [Changing elements status via commit
    message][].

[github]: https://github.com/
[taiga]: https://taiga.io/
[closing issues using keywords]: https://help.github.com/en/articles/closing-issues-using-keywords
[attach commits to elements via commit message]: https://tree.taiga.io/support/integrations/attach-commits-to-elements-via-commit-message/
[changing elements status via commit message]: https://tree.taiga.io/support/integrations/changing-elements-status-via-commit-message/
