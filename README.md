# docker_semantic_versioning_demo
```
   _         _                 
  | |_ _   _| |_ ___  ___ ___  
  | __| | | | __/ _ \/ __/ _ \ 
  | |_| |_| | ||  __/ (_| (_) |
 (_)__|\__,_|\__\___|\___\___/ 
 
 -- data & knowledge experts --                              
```

demo project for semantic versioning with docker hub

[Conventional commits](https://www.conventionalcommits.org/en/v1.0.0/) are used to determine the next relase version. 
Use the following style in your commit messages: 

- "fix: ..." --> creates a patch release
- "feat: ..." --> creates a minor relase
- "feat!: ..." --> creates a major release

any other type like build: or docs: does not create any new release.

## docker example
There is a hello world container app to demonstrate the functionality to integrate a docker build and push 
to semantic versioning workflow.

For local testing, you need to have python and the package `invoke` installed.

To build the local container, run:
```
invoke build-local
```


## Changelog
please see [changelog file](CHANGELOG.md)
