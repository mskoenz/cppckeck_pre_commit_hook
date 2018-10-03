# cppcheck hook for pre-commit

[cppcheck](https://github.com/danmar/cppcheck/) package for [pre-commit](http://pre-commit.com).

## Using cppcheck with pre-commit

```yaml
-   repo: git://github.com/mskoenz/pre-commit-cppcheck
    sha: master
    hooks:
    -   id: cppcheck
```
