# Automated Repos
Automated Repos is a command line tool to handle multiple Git repositories.
Instead of performing the actions like `git push` for each directory, this tool can do this automatically for each directory.

Jobs can be grouped into jobs. A job can contain multiple commands like "git push". With the command "aure exec" all jobs in the current folder and subfolders will be executed.

**Inspired by Fabioz's mu-repo** (https://github.com/fabioz/mu-repo)  
When searching for existing solutions for managing multiple git repos, the mu-repo project from fabioz came to the fore. However, this has not been updated since 2018.  
His implementation was a great foundation for the command line tool.

## Config file
The hidden file `.aure` contains the configuration for the subfolders and uses the [TOML file format](https://en.wikipedia.org/wiki/TOML).
The file can be change by hand or by using the command line tool.

## Usage
